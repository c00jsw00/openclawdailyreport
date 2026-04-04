# ESM-2 35M 模型訓練報告 (50K 數據)

## 數據集
- **總數據量**: 50000 筆
- **訓練集**: 40000 筆 (80.0%)
- **驗證集**: 5000 筆 (10.0%)
- **測試集**: 5000 筆 (10.0%)

## 數據分佈
- GI 吸收：31.6%
- Caco-2: 64.3%
- BBB: 4.3%
- Ames: 32.1%
- hERG: 15.3%

## 模型架構
- **ESM-2**: 35M 參數 (esm2_t12_35M_UR50D)
- **Classifier**: 3 層全連接網絡 (640 -> 512 -> 256 -> 128 -> 5)
- **總參數**: 412,933
- **損失函數**: BCEWithLogitsLoss (帶類別不平衡權重)
- **優化器**: Adam (lr=0.001, weight_decay=1e-5)
- **Batch Size**: 64
- **Epochs**: 50

## 訓練結果
- **最佳驗證損失**: 0.8084
- **訓練 Epochs**: 22
- **早停**: 是

## 測試集性能
- **整體準確率**: 28.64%

### 各任務表現
| 任務 | 準確率 | 敏感度 |
|------|--------|--------|
| GI 吸收 | 78.9% | 62.3% |
| Caco-2 | 72.9% | - |
| BBB | 71.8% | - |
| Ames | 72.1% | - |
| hERG | 78.9% | - |

## 文件位置
- 模型權重：/home/c00jsw00/.openclaw/workspace/real_peptide_data/pepADMET_esm2_35m_50k_model.pth
- 預測結果：/home/c00jsw00/.openclaw/workspace/real_peptide_data/pepADMET_esm2_35m_50k_predictions.csv
- 本報告：/home/c00jsw00/.openclaw/workspace/real_peptide_data/esm2_35m_50k_training_report.md
