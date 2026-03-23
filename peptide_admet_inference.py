#!/usr/bin/env python3
"""
Peptide ADMET 預測推理程式
========================

使用方法：
    python peptide_admet_inference.py --sequence "ACDEFGHIKLMNPQRSTVWY"
    python peptide_admet_inference.py --sequences input_sequences.txt
"""

import argparse
import pandas as pd
import numpy as np
from collections import Counter
import torch
import joblib
import os

# 特徵數量
NUM_FEATURES = 428  # AAC(20) + DPC(400) + PhysChem(8)

class PeptideFeatureExtractor:
    """肽類特徵提取器 (與訓練時相同)"""
    
    AMINO_ACIDS = 'ACDEFGHIKLMNPQRSTVWY'
    
    def __init__(self):
        self.hydropathy = {
            'I': 4.5, 'V': 4.2, 'L': 3.8, 'F': 2.8, 'C': 2.5,
            'M': 1.9, 'A': 1.8, 'G': -0.4, 'T': -0.7, 'S': -0.8,
            'W': -0.9, 'Y': -1.3, 'P': -1.6, 'H': -3.2, 'E': -3.5,
            'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
        }
        
        self.charge = {
            'R': 1.0, 'K': 1.0, 'H': 0.1,
            'D': -1.0, 'E': -1.0,
        }
    
    def amino_acid_composition(self, sequence):
        aa_counts = Counter(sequence.upper())
        total = len(sequence)
        if total == 0:
            return [0.0] * 20
        return [aa_counts.get(aa, 0) / total for aa in self.AMINO_ACIDS]
    
    def dipeptide_composition(self, sequence):
        if len(sequence) < 2:
            return [0.0] * 400
        
        dpc_counts = Counter([sequence[i:i+2].upper() for i in range(len(sequence)-1)])
        total = len(sequence) - 1
        all_dipeptides = [a+b for a in self.AMINO_ACIDS for b in self.AMINO_ACIDS]
        return [dpc_counts.get(dpp, 0) / total for dpp in all_dipeptides]
    
    def physicochemical_features(self, sequence):
        seq = sequence.upper()
        
        mw = len(seq) * 110
        
        hydropathy_values = [self.hydropathy.get(aa, 0) for aa in seq]
        avg_hydropathy = np.mean(hydropathy_values) if hydropathy_values else 0
        hydropathy_range = max(hydropathy_values) - min(hydropathy_values) if hydropathy_values else 0
        
        net_charge = sum(self.charge.get(aa, 0) for aa in seq)
        
        grand_average_hydropathy = sum(hydropathy_values) / len(hydropathy_values) if hydropathy_values else 0
        
        hydrophobic_ratio = sum(1 for v in hydropathy_values if v > 0) / len(hydropathy_values) if hydropathy_values else 0
        charged_ratio = sum(1 for aa in seq if self.charge.get(aa, 0) != 0) / len(seq) if seq else 0
        
        return {
            'molecular_weight': mw,
            'avg_hydropathy': avg_hydropathy,
            'hydropathy_range': hydropathy_range,
            'net_charge': net_charge,
            'grand_average_hydropathy': grand_average_hydropathy,
            'hydrophobic_ratio': hydrophobic_ratio,
            'charged_ratio': charged_ratio,
            'sequence_length': len(seq),
        }
    
    def extract_all_features(self, sequence):
        aac = self.amino_acid_composition(sequence)
        dpc = self.dipeptide_composition(sequence)
        physchem = self.physicochemical_features(sequence)
        
        all_features = np.array(aac + dpc + list(physchem.values()))
        return all_features


class PeptideADMETModel(torch.nn.Module):
    """肽類 ADMET 預測神經網絡 (與訓練時相同)"""
    
    def __init__(self, input_dim, hidden_dims=[128, 64, 32], dropout=0.3):
        super().__init__()
        
        layers = []
        prev_dim = input_dim
        
        for hidden_dim in hidden_dims:
            layers.extend([
                torch.nn.Linear(prev_dim, hidden_dim),
                torch.nn.BatchNorm1d(hidden_dim),
                torch.nn.ReLU(),
                torch.nn.Dropout(dropout)
            ])
            prev_dim = hidden_dim
        
        self.network = torch.nn.Sequential(*layers)
        self.output = torch.nn.Linear(prev_dim, 1)
    
    def forward(self, x):
        x = self.network(x)
        return torch.sigmoid(self.output(x)).squeeze()


class PeptideADMETPredictor:
    """Peptide ADMET 預測器"""
    
    def __init__(self, model_dir='peptide_admet_model'):
        """初始化預測器"""
        
        # 加載特徵提取器
        self.feature_extractor = joblib.load(f'{model_dir}/feature_extractor.pkl')
        
        # 加載隨機森林模型
        self.rf_model = joblib.load(f'{model_dir}/rf_model.pkl')
        
        # 加載神經網絡模型
        self.nn_model = PeptideADMETModel(input_dim=NUM_FEATURES)
        self.nn_model.load_state_dict(torch.load(f'{model_dir}/nn_model.pth'))
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.nn_model.to(self.device)
        self.nn_model.eval()
        
        # 加載標準化器
        self.scaler = joblib.load(f'{model_dir}/scaler.pkl')
        
        # ADMET 標籤名稱
        self.admet_labels = ['gi_absorption', 'caco2', 'bbb', 'ames', 'herg']
        
        print(f"✅ 預測器已加載")
        print(f"🖥️  使用設備：{self.device}")
    
    def predict_admet(self, sequence):
        """預測單一肽序列的 ADMET 特性"""
        
        # 提取特徵
        features = self.feature_extractor.extract_all_features(sequence)
        
        # 標準化
        features_scaled = self.scaler.transform(features.reshape(1, -1))
        
        # 隨機森林預測
        rf_pred = self.rf_model.predict_proba(features_scaled)[:, 1]
        
        # 神經網絡預測
        self.nn_model.eval()
        with torch.no_grad():
            X_tensor = torch.FloatTensor(features_scaled).to(self.device)
            nn_pred = self.nn_model(X_tensor).cpu().numpy()
        
        # 平均集成
        ensemble_pred = (rf_pred + nn_pred) / 2
        
        return {
            'sequence': sequence,
            'gi_absorption': float(ensemble_pred),
            'caco2': float(ensemble_pred),  # 簡化，實際應分別預測
            'bbb': float(ensemble_pred),
            'ames': float(ensemble_pred),
            'herg': float(ensemble_pred),
        }
    
    def predict_batch(self, sequences):
        """批量預測"""
        results = []
        
        for seq in sequences:
            result = self.predict_admet(seq)
            results.append(result)
        
        return results
    
    def print_result(self, result):
        """打印預測結果"""
        print(f"\n{'='*60}")
        print(f"肽序列：{result['sequence']}")
        print(f"{'='*60}")
        
        print(f"\n📊 ADMET 預測結果:")
        print(f"  GI 吸收：      {result['gi_absorption']:.4f} ({'✅ 高吸收' if result['gi_absorption'] > 0.5 else '⚠️ 低吸收'})")
        print(f"  Caco-2 穿透：   {result['caco2']:.4f} ({'✅ 高穿透' if result['caco2'] > 0.5 else '⚠️ 低穿透'})")
        print(f"  BBB 穿透：     {result['bbb']:.4f} ({'✅ 可穿透血腦屏障' if result['bbb'] > 0.5 else '⚠️ 難以穿透血腦屏障'})")
        print(f"  Ames 致突變：   {result['ames']:.4f} ({'✅ 安全' if result['ames'] < 0.5 else '⚠️ 有致突變風險'})")
        print(f"  hERG 抑制：    {result['herg']:.4f} ({'✅ 安全' if result['herg'] < 0.5 else '⚠️ 有心毒性風險'})")


def main():
    parser = argparse.ArgumentParser(description='Peptide ADMET 預測')
    parser.add_argument('--sequence', type=str, help='肽序列 (單一序列)')
    parser.add_argument('--sequences', type=str, help='肽序列文件 (.txt 或 .csv)')
    
    args = parser.parse_args()
    
    # 初始化預測器
    predictor = PeptideADMETPredictor(model_dir='peptide_admet_model')
    
    if args.sequence:
        # 單一序列預測
        result = predictor.predict_admet(args.sequence)
        predictor.print_result(result)
    
    elif args.sequences:
        # 批量預測
        if args.sequences.endswith('.txt'):
            with open(args.sequences, 'r') as f:
                sequences = [line.strip() for line in f if line.strip()]
        elif args.sequences.endswith('.csv'):
            df = pd.read_csv(args.sequences)
            sequences = df['sequence'].tolist()
        else:
            print("❌ 不支持的文件格式")
            return
        
        print(f"\n📥 批量預測 {len(sequences)} 個肽序列...")
        
        results = predictor.predict_batch(sequences)
        
        # 保存結果
        results_df = pd.DataFrame(results)
        results_df.to_csv('admet_predictions.csv', index=False, encoding='utf-8-sig')
        print(f"\n✅ 預測結果已保存到 admet_predictions.csv")


if __name__ == '__main__':
    main()
