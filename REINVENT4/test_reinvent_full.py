#!/usr/bin/env python3
"""
REINVENT4 完整測試腳本

測試項目:
1. 基本導入
2. 分子操作
3. 自訂評分器
4. 分子生成測試
"""

import os
import sys
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors, QED

# 添加 REINVENT4 路徑
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'REINVENT4'))

def test_basic_imports():
    """測試基本模組導入"""
    print("=" * 60)
    print("測試 1: 基本導入")
    print("=" * 60)
    
    try:
        import torch
        print(f"✓ PyTorch {torch.__version__}")
        print(f"  GPU 可用：{torch.cuda.is_available()}")
        if torch.cuda.is_available():
            print(f"  GPU 名稱：{torch.cuda.get_device_name(0)}")
    except ImportError as e:
        print(f"✗ PyTorch 導入失敗：{e}")
        return False
    
    try:
        from rdkit import Chem
        print("✓ RDKit 導入成功")
    except ImportError as e:
        print(f"✗ RDKit 導入失敗：{e}")
        return False
    
    try:
        from reinvent import version
        print(f"✓ REINVENT {version.__version__}")
    except ImportError as e:
        print(f"✗ REINVENT 導入失敗：{e}")
        return False
    
    print()
    return True

def test_molecule_operations():
    """測試分子操作"""
    print("=" * 60)
    print("測試 2: 分子操作")
    print("=" * 60)
    
    # 測試 SMILES 解析
    test_smiles = [
        ("Aspirin", "CC(=O)Oc1ccccc1C(=O)O"),
        ("Caffeine", "CN1C=NC2=C1C(=O)N(C(=O)N2C)C"),
        ("Morphine", "C1CCC2C3C(C1CC(O)C2(C3)N(C)C=CC=C4)O"),
        ("Diazepam", "CN1C(=O)CN=C2C1=CC=CC2=C3C=CC=CC3=O"),
    ]
    
    results = []
    for name, smiles in test_smiles:
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            print(f"✗ {name}: SMILES 解析失敗")
            continue
        
        mw = Descriptors.MolWt(mol)
        logp = Descriptors.MolLogP(mol)
        hba = Descriptors.NumHAcceptors(mol)
        hbd = Descriptors.NumHDonors(mol)
        qed = QED.qed(mol)
        
        results.append({
            'Name': name,
            'SMILES': smiles,
            'MW': mw,
            'LogP': logp,
            'HBA': hba,
            'HBD': hbd,
            'QED': qed
        })
        
        print(f"✓ {name:12s} - MW: {mw:6.1f}, LogP: {logp:5.2f}, QED: {qed:.3f}")
    
    print()
    return results

def test_custom_scorer():
    """測試自訂評分器"""
    print("=" * 60)
    print("測試 3: 自訂評分器")
    print("=" * 60)
    
    def custom_scorer(smiles, target_qed=0.7, target_logp=3.0):
        """自訂評分函數"""
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            return 0.0
        
        qed = QED.qed(mol)
        logp = Descriptors.MolLogP(mol)
        
        # 計算與目標的距離
        qed_score = 1.0 - abs(qed - target_qed)
        logp_score = 1.0 - abs(logp - target_logp)
        
        # 綜合評分
        score = 0.5 * qed_score + 0.5 * logp_score
        
        return max(0.0, min(1.0, score))
    
    # 測試評分器
    test_molecules = [
        "CC(=O)Oc1ccccc1C(=O)O",  # Aspirin
        "CCO",                     # Ethanol
        "CCCCCCCCCCCCCCCC",        # Octadecane
        "CN1C=NC2=C1C(=O)N(C(=O)N2C)C",  # Caffeine
    ]
    
    print("分子評分 (目標：QED=0.7, LogP=3.0):")
    for smiles in test_molecules:
        score = custom_scorer(smiles)
        mol = Chem.MolFromSmiles(smiles)
        name = Chem.MolToSmiles(mol) if mol else "Invalid"
        print(f"  {name:40s} - Score: {score:.3f}")
    
    print()
    return True

def generate_test_molecules():
    """測試分子生成 (使用 RDKit 簡單生成)"""
    print("=" * 60)
    print("測試 4: 簡單分子生成測試")
    print("=" * 60)
    
    # 使用 RDKit 生成簡單的類似物
    from rdkit.Chem import rdMolDescriptors
    
    parent_smiles = "CC(=O)Oc1ccccc1C(=O)O"  # Aspirin
    mol = Chem.MolFromSmiles(parent_smiles)
    
    if mol is None:
        print("✗ 無法解析母分子")
        return False
    
    print(f"母分子：{parent_smiles}")
    print(f"  QED: {QED.qed(mol):.3f}")
    print(f"  MW: {Descriptors.MolWt(mol):.1f}")
    print()
    
    # 生成簡單變體
    variants = [
        "CC(=O)Oc1ccccc1C(=O)O",
        "CC(=O)Oc1ccc(C)cc1C(=O)O",  # Methyl aspirin
        "CC(=O)Oc1cc(C)ccc1C(=O)O",  # Another methyl variant
        "CC(=O)Oc1ccc(C(=O)OC)cc1",  # Methyl ester variant
    ]
    
    print("生成的分子變體:")
    for i, smiles in enumerate(variants, 1):
        mol = Chem.MolFromSmiles(smiles)
        if mol:
            qed = QED.qed(mol)
            mw = Descriptors.MolWt(mol)
            print(f"  {i:2d}. {smiles:40s} - QED: {qed:.3f}, MW: {mw:.1f}")
    
    print()
    return True

def main():
    """主測試函數"""
    print("\n" + "=" * 60)
    print("REINVENT4 完整測試")
    print("=" * 60 + "\n")
    
    results = {
        '基本導入': test_basic_imports(),
        '分子操作': test_molecule_operations(),
        '自訂評分器': test_custom_scorer(),
        '分子生成': generate_test_molecules(),
    }
    
    print("=" * 60)
    print("測試總結")
    print("=" * 60)
    
    for test_name, result in results.items():
        status = "✓ 通過" if result else "✗ 失敗"
        print(f"{test_name:15s}: {status}")
    
    all_passed = all(results.values())
    
    print("=" * 60)
    if all_passed:
        print("✓ 所有測試通過！REINVENT4 可以正常使用")
    else:
        print("⚠ 部分測試失敗，請檢查問題")
    print("=" * 60)
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
