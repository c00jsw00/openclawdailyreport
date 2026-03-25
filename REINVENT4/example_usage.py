"""
REINVENT4 實際使用範例

示範如何使用 REINVENT4 進行分子設計
"""

import os
import sys
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors, QED

# 添加 REINVENT4 路徑
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'REINVENT4'))

def create_sample_config():
    """創建測試用的 sampling.toml 配置文件"""
    config_content = """# REINVENT4 測試配置
run_type = "sampling"
device = "cpu"  # 使用 CPU 進行測試
json_out_config = "_sampling_test.json"

[parameters]

## 使用內部模型 (如果可用)
# 如果無法下載預訓練模型，可以使用內部模型
# model_file = "reinvent.prior"  # 內部模型

## 或者使用自訂模型
# model_file = "my_custom_model.prior"

# 輸出檔案
output_file = 'sampling_test.csv'

# 生成 10 個分子 (測試用少量)
num_smiles = 10

# 去除重複分子
unique_molecules = true

# 隨機化 SMILES 表示
randomize_smiles = true

# 採樣策略：multinomial 或 beamsearch
sample_strategy = "multinomial"

# 溫度參數 (越高越多樣)
temperature = 1.0

# TensorBoard 日誌目錄 (可選)
# tb_logdir = "tb_logs"
"""
    
    config_path = 'sampling_test.toml'
    with open(config_path, 'w') as f:
        f.write(config_content)
    
    print(f"✓ 創建配置文件：{config_path}")
    return config_path

def analyze_generated_molecules(csv_path):
    """分析生成的分子"""
    if not os.path.exists(csv_path):
        print(f"✗ 檔案不存在：{csv_path}")
        return None
    
    try:
        df = pd.read_csv(csv_path)
        print(f"✓ 讀取 {len(df)} 個分子")
        
        # 計算描述符
        results = []
        for idx, row in df.iterrows():
            smiles = row.get('SMILES', '')
            if not smiles:
                continue
            
            mol = Chem.MolFromSmiles(smiles)
            if mol is None:
                continue
            
            mw = Descriptors.MolWt(mol)
            logp = Descriptors.MolLogP(mol)
            hba = Descriptors.NumHAcceptors(mol)
            hbd = Descriptors.NumHDonors(mol)
            qed = QED.qed(mol)
            tpsa = Descriptors.TPSA(mol)
            
            results.append({
                'SMILES': smiles,
                'MW': mw,
                'LogP': logp,
                'HBA': hba,
                'HBD': hbd,
                'QED': qed,
                'TPSA': tpsa
            })
        
        results_df = pd.DataFrame(results)
        
        if len(results_df) > 0:
            print("\n統計分析:")
            print(f"  平均 QED:  {results_df['QED'].mean():.3f}")
            print(f"  平均 MW:   {results_df['MW'].mean():.1f}")
            print(f"  平均 LogP: {results_df['LogP'].mean():.2f}")
            print(f"  QED > 0.5: {len(results_df[results_df['QED'] > 0.5])} ({100*results_df['QED'].mean():.0f}%)")
        
        return results_df
        
    except Exception as e:
        print(f"✗ 分析失敗：{e}")
        return None

def custom_scorer_example():
    """自訂評分器範例"""
    print("\n" + "=" * 60)
    print("自訂評分器範例")
    print("=" * 60)
    
    def multi_objective_scorer(smiles, weights=None):
        """
        多目標評分器
        
        Args:
            smiles: SMILES 字符串
            weights: 權重字典 {'qed': 0.4, 'logp': 0.3, 'mw': 0.3}
        
        Returns:
            綜合評分 (0-1)
        """
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            return 0.0
        
        if weights is None:
            weights = {'qed': 0.4, 'logp': 0.3, 'mw': 0.3}
        
        # 計算各指標
        qed = QED.qed(mol)
        logp = Descriptors.MolLogP(mol)
        mw = Descriptors.MolWt(mol)
        
        # 歸一化評分
        qed_score = qed  # 0-1 已歸一化
        
        # LogP 評分 (目標 2-3)
        if logp < 2:
            logp_score = 1.0 - (2 - logp) * 0.5
        elif logp > 3:
            logp_score = 1.0 - (logp - 3) * 0.3
        else:
            logp_score = 1.0
        
        # MW 評分 (目標 < 400)
        if mw < 300:
            mw_score = 1.0
        elif mw < 400:
            mw_score = 1.0 - (mw - 300) / 100
        else:
            mw_score = 0.0
        
        # 綜合評分
        score = (weights['qed'] * qed_score + 
                weights['logp'] * logp_score + 
                weights['mw'] * mw_score)
        
        return max(0.0, min(1.0, score))
    
    # 測試評分器
    test_smiles = [
        "CC(=O)Oc1ccccc1C(=O)O",  # Aspirin
        "CCO",                     # Ethanol
        "CN1C=NC2=C1C(=O)N(C(=O)N2C)C",  # Caffeine
        "CC(=O)Oc1ccc(C)cc1C(=O)O",  # Methyl aspirin
    ]
    
    print("多目標評分 (QED:0.4, LogP:0.3, MW:0.3):")
    for smiles in test_smiles:
        score = multi_objective_scorer(smiles)
        mol = Chem.MolFromSmiles(smiles)
        if mol:
            info = f"MW:{Descriptors.MolWt(mol):.0f} LogP:{Descriptors.MolLogP(mol):.1f} QED:{QED.qed(mol):.2f}"
            print(f"  {smiles:45s} - Score: {score:.3f} {info}")

def create_training_data():
    """創建用於遷移學習的訓練數據"""
    print("\n" + "=" * 60)
    print("創建遷移學習訓練數據")
    print("=" * 60)
    
    # 定義一組種子分子 (模擬藥物分子)
    seed_smiles = [
        "CC(=O)Oc1ccccc1C(=O)O",           # Aspirin
        "CC(C)Cc1ccccc1NC(=O)C",            # Ibuprofen
        "CC(C)Nc1ccccc1C(=O)O",            # Phenylpropanolamine
        "CN1C=NC2=C1C(=O)N(C(=O)N2C)C",    # Caffeine
        "CC1=C(C(=O)O)C=CC=C1C(=O)O",      # Phthalic acid
        "CC(=O)Oc1ccc(C(=O)O)cc1",          # Aspirin derivative
        "CC(C)Cc1ccc(C(=O)O)cc1",           # Ibuprofen derivative
        "CC1=C(C(=O)OC)C=CC=C1C(=O)OC",     # Dimethyl phthalate
    ]
    
    # 寫入文件
    output_file = 'training_seeds.smi'
    with open(output_file, 'w') as f:
        for smiles in seed_smiles:
            f.write(smiles + '\n')
    
    print(f"✓ 創建訓練數據：{output_file}")
    print(f"  種子分子數：{len(seed_smiles)}")
    
    # 分析種子分子
    print("\n種子分子分析:")
    for smiles in seed_smiles:
        mol = Chem.MolFromSmiles(smiles)
        if mol:
            qed = QED.qed(mol)
            mw = Descriptors.MolWt(mol)
            print(f"  {smiles:50s} - QED: {qed:.2f}, MW: {mw:.0f}")
    
    return output_file

def main():
    """主函數"""
    print("\n" + "=" * 60)
    print("REINVENT4 實際使用範例")
    print("=" * 60)
    
    # 1. 創建配置文件
    print("\n[1/4] 創建配置文件...")
    config_path = create_sample_config()
    
    # 2. 創建訓練數據
    print("\n[2/4] 創建遷移學習數據...")
    training_file = create_training_data()
    
    # 3. 測試自訂評分器
    print("\n[3/4] 測試自訂評分器...")
    custom_scorer_example()
    
    # 4. 說明下一步
    print("\n" + "=" * 60)
    print("下一步建議:")
    print("=" * 60)
    print("""
REINVENT4 基本使用流程:

1. De Novo 分子生成 (需要預訓練模型):
   reinvent -l sampling.log sampling.toml

2. 遷移學習訓練:
   reinvent -l tl.log transfer_learning.toml

3. 分子優化:
   reinvent -l rl.log staged_learning.toml

4. 使用 Python API:
   python test_reinvent_full.py

注意：預訓練模型目前無法從 Zenodo 下載，
建議使用自訂模型或等待官方更新。
    """)
    
    print("=" * 60)
    print("✓ 範例完成！")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
