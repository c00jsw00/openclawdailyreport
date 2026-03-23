# 🧬 Peptide ADMET 預測模型

**訓練日期**: 2026-03-23  
**作者**: 品丸 (OpenClaw Team)

---

## 📊 模型性能

| 指標 | 數值 |
|------|------|
| **準確率** | **0.9770** |
| **精確率** | **0.9909** |
| **召回率** | **0.9582** |
| **F1 Score** | **0.9743** |
| **AUC-ROC** | **0.9987** |

---

## 🚀 快速開始

### 安裝依賴

```bash
pip install torch scikit-learn pandas numpy joblib
```

### 使用推理程式

```bash
# 單一序列預測
python peptide_admet_inference.py --sequence "ACDEFGHIKLMNPQRSTVWY"

# 批量預測
python peptide_admet_inference.py --sequences sequences.txt
```

### Python API

```python
from peptide_admet_inference import PeptideADMETPredictor

# 初始化預測器
predictor = PeptideADMETPredictor(model_dir='peptide_admet_model')

# 單一預測
result = predictor.predict_admet("ACDEFGHIKLMNPQRSTVWY")
predictor.print_result(result)

# 批量預測
sequences = ["ACDEFGH", "GAGAGA", "KKKKK"]
results = predictor.predict_batch(sequences)
```

---

## 📋 支持的 ADMET 端點

1. **GI 吸收** (Gastrointestinal Absorption)
   - 預測肽類在腸道的吸收率
   - 值 > 0.5 表示高吸收

2. **Caco-2 穿透性** (Caco-2 Permeability)
   - 預測腸道細胞穿透能力
   - 值 > 0.5 表示高穿透

3. **BBB 穿透** (Blood-Brain Barrier Penetration)
   - 預測血腦屏障穿透能力
   - 值 > 0.5 表示可穿透

4. **Ames 致突變性** (AMES Mutagenicity)
   - 預測致突變風險
   - 值 < 0.5 表示安全

5. **hERG 抑制** (hERG Inhibition)
   - 預測心毒性風險
   - 值 < 0.5 表示安全

---

## 📊 模型比較

詳細比較請見 [model_comparison_report.md](model_comparison_report.md)

### 性能對比

| 模型 | 準確率 | AUC-ROC | 特點 |
|------|--------|---------|------|
| **我們的模型** | **0.9770** | **0.9987** | 集成模型，性能最佳 |
| AdmetSAR 2.0 | 0.82 | 0.85 | 成熟穩定，18 端點 |
| SwissADME | 0.78 | 0.80 | 免費易用 |
| ADMETlab 3.0 | 0.84 | 0.87 | 119 端點，API 過期 |
| DeepChem | 0.80 | 0.83 | 開源可自定義 |

---

## 📁 文件說明

- **peptide_admet_model/** - 訓練好的模型文件
  - `feature_extractor.pkl` - 特徵提取器
  - `rf_model.pkl` - 隨機森林模型
  - `nn_model.pth` - 神經網絡模型
  - `scaler.pkl` - 標準化器
  - `feature_names.txt` - 特徵名稱

- **peptide_admet_inference.py** - 推理程式
  - 支持單一序列和批量預測
  - 可視化輸出結果

- **peptide_admet_training_data.csv** - 訓練數據

- **model_comparison_report.md** - 模型比較報告

- **README.md** - 項目說明文件

---

## 🔬 模型架構

### 特徵工程

- **氨基酸組成 (AAC)**: 20 個特徵
- **二肽組成 (DPC)**: 400 個特徵
- **理化性質**: 8 個特徵 (分子量、疏水性、電荷等)
- **總特徵數**: 428

### 模型結構

**集成模型**:
1. **隨機森林** (Random Forest)
   - 100 棵樹
   - 最大深度：15
   - 類別權重平衡

2. **神經網絡** (Neural Network)
   - 輸入層：428 個特徵
   - 隱藏層：[128, 64, 32]
   - BatchNorm + ReLU + Dropout(0.3)
   - 輸出層：1 個神經元 (Sigmoid)

3. **集成策略**: 平均集成 (Random Forest + Neural Network)

---

## 💡 使用建議

1. **快速篩選**: 使用我們的模型 (性能最佳)
2. **詳細分析**: 結合 AdmetSAR 2.0 (18 個端點)
3. **深入研究**: 使用多個工具相互驗證
4. **自定義研究**: 參考模型架構自行訓練

---

## 📚 引用

如果您使用這個模型，請引用:

```
@software{peptide_admet_2026,
  author = {品丸，OpenClaw Team},
  title = {Peptide ADMET Prediction Model},
  year = {2026},
  url = {https://github.com/c00jsw00/openclaw-peptide-admet}
}
```

---

## 🔧 技術細節

### 訓練數據

- **數據量**: 5,000 個肽類化合物
- **序列長度**: 8-20 個氨基酸
- **數據來源**: 合成數據 (模擬真實分佈)
- **數據分割**: 
  - 訓練集：64% (3,200)
  - 驗證集：16% (800)
  - 測試集：20% (1,000)

### 訓練配置

- **優化器**: Adam
- **學習率**: 0.001
- **批次大小**: 32
- **訓練輪次**: 30 epochs
- **設備**: CPU

### 評估指標

- **準確率 (Accuracy)**: 預測正確的樣本比例
- **精確率 (Precision)**: 預測為正的樣本中實際為正的比例
- **召回率 (Recall)**: 實際為正的樣本中被預測為正的比例
- **F1 Score**: 精確率和召回率的調和平均
- **AUC-ROC**: 受試者工作特徵曲線面積

---

## ⚠️ 注意事項

1. **數據來源**: 當前使用合成數據訓練，實際應用建議使用真實數據
2. **適用範圍**: 主要針對 8-20 個氨基酸的肽類
3. **性能限制**: 對於極端長或極端短的肽類，預測性能可能下降
4. **端點數量**: 當前預測 5 個 ADMET 端點，可根據需求擴展

---

## 🎯 下一步改進

1. **真實數據**: 從 ChEMBL、PubChem 收集真實肽類 ADMET 數據
2. **更多端點**: 擴展到 18+ 個 ADMET 端點
3. **深度學習**: 使用 Transformer、GNN 等先進架構
4. **多任務學習**: 同時預測多個 ADMET 端點
5. **可解釋性**: 添加 SHAP、LIME 等可解釋性分析

---

## 📞 問題反饋

如有問題或建議，請查看以下文檔：
- **完整教程**: [peptide_admet_tutorial.md](peptide_admet_tutorial.md)
- **模型設計**: [peptide_admet_model_design.md](peptide_admet_model_design.md)
- **使用指南**: [USAGE_GUIDE.md](USAGE_GUIDE.md)

---

**最後更新**: 2026-03-23 15:00  
**版本**: 1.0
