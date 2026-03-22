# Boltz-2 配體篩選分析

本倉庫記錄使用 Boltz-2 進行蛋白質 - 配體結合親和力預測的實驗結果和使用方法。

---

## 📌 最新分析

### VEGFR2 配體篩選 (2026-03-22)

**分析對象：** VEGFR2 蛋白質 (316 aa) 與 11 個配體

**統計結果：**
- Pearson 相關係數：r = 0.678 (中等相關)
- 平均誤差：-0.144 log10 單位
- RMSE: 0.621

**詳細報告：** [VEGFR2 Analysis Report](./vegfr2-boltz2-screening.md)

---

## 🧬 Boltz-2 Skill 使用方法

### 如何呼叫品丸使用 Boltz-2

#### 範例 1：單個配體預測

```
品丸，請用 boltz-2 預測蛋白質與配體的複合物結構並計算親和力

蛋白質序列：MKTVRQERLKSIVRILERSKEPVSGAQLAEELSVSRQVIVQDIAYLRSLGYNIVATPRGYVLAGG
配體 SMILES: N[C@@H](Cc1ccc(O)cc1)C(=O)O  (多巴胺)
```

#### 範例 2：多個配體篩選

```
品丸，請幫我測試這 3 個配體與蛋白質的結合能力

蛋白質序列：[蛋白質序列]
配體列表：
1. SMILES1
2. SMILES2
3. SMILES3

請預測所有複合物結構並計算親和力，給我比較報告
```

#### 範例 3：結構視覺化

```
品丸，請將 boltz-2 結果轉成結構圖

輸入：boltz2_input_model_0.cif
輸出：structure.png
視圖：cartoon，解析度 1920x1080
```

---

## 🔬 Boltz-2 功能

- **3D 結構預測**：蛋白質、RNA、DNA、配體複合物
- **結合親和力預測**：log10(IC50) in μM
- **結合劑檢測**：binder probability (0-1)
- **結構視覺化**：CIF/PDB → PNG/GIF
- **360°旋轉動畫**
- **1000x 快**於傳統 FEP 方法
- **NVIDIA GPU 加速**

---

## 📊 親和力解讀

### log10(IC50) 對應 IC50 值

| log10(IC50) | IC50 | 結合強度 |
|-------------|------|----------|
| -9 | 1 nM | 極強 |
| -8 | 10 nM | 很強 |
| -7 | 100 nM | 強 |
| -6 | 1 μM | 中等 |
| -5 | 10 μM | 弱 |
| -4 | 100 μM | 很弱 |

### Binder Probability

- **>0.8**: 強結合劑
- **0.5-0.8**: 可能結合
- **0.3-0.5**: 弱結合 / 不確定
- **<0.3**: 不結合

---

## 📁 文件說明

### 分析結果

- **vegfr2-boltz2-screening.md**: VEGFR2 配體篩選完整分析報告
- **boltz2_results_vegfr2.json**: 原始 JSON 格式預測結果

### 工具腳本

- **boltz2_vegfr2_screening.py**: Boltz-2 批量篩選 Python 腳本

---

## 💡 使用建議

### ✅ 適合用途

- 初篩大量配體庫，快速排除極弱結合劑
- 比較相似結構配體的相對親和力
- 識別強結合劑候選

### ⚠️ 注意事項

- 不要過度依賴絕對數值，應關注相對排序
- 結合其他方法 (如分子動力學模擬) 進行驗證
- 對於精確的 IC50 預測，需進行實驗驗證

---

## 🔗 參考資源

- **Boltz-2 Paper**: https://doi.org/10.1101/2025.06.14.659707
- **Boltz-2 GitHub**: https://github.com/jwohlwend/boltz
- **Boltz-2 Slack**: https://boltz.bio/join-slack

---

*最後更新：2026-03-22*
