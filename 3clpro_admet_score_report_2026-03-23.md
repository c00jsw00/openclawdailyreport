# ADMET-Score 分析報告 - 3CLpro 抑制劑

**分析日期：** 2026-03-23 08:00  
**化合物數量：** 20 個 3CLpro 抑制劑  
**分析工具：** ADMET-AI + ADMET-Score (admetSAR 2.0)  
**論文來源：** [PMC6350845](https://pmc.ncbi.nlm.nih.gov/articles/PMC6350845/)

---

## 📊 分析摘要

### 3CLpro 抑制劑 ADMET-Score 統計

| 性質 | 數值 |
|------|------|
| 平均 ADMET-Score | 0.2082 |
| 標準差 | 0.0229 |
| 最小值 | 0.1781 |
| 最大值 | 0.2479 |

### ADMET-Score 等級分佈

| 等級 | 分數範圍 | 數量 | 百分比 |
|------|----------|------|--------|
| ⭐⭐⭐ 優秀 | 0.80-1.00 | 0 | 0% |
| ⭐⭐ 良好 | 0.60-0.79 | 0 | 0% |
| ⭐ 中等 | 0.40-0.59 | 0 | 0% |
| ⚠️ 需優化 | 0.20-0.39 | 12 | 60% |
| ❌ 差 | 0.00-0.19 | 8 | 40% |

---

## 🎯 關鍵發現

### 1. ADMET-Score 整體表現

- **平均 ADMET-Score: 0.2082** - 表示這批化合物的藥物特性需要優化
- **分佈集中** - 標準差僅 0.0229，表明所有化合物表現相近
- **無優秀化合物** - 沒有化合物達到 0.4 以上 (中等水平)

### 2. 與 QED 的比較

| 性質 | 平均 QED | 平均 ADMET-Score |
|------|----------|-----------------|
| 3CLpro 抑制劑 | 0.425 | 0.2082 |

**觀察**: ADMET-Score 明顯低於 QED，說明：
- 化合物的物理化學性質尚可 (QED 0.425)
- 但 ADMET 性質 (代謝、毒性) 表現較差
- 需要優化代謝穩定性和降低毒性

### 3. TOP 10 最佳化合物 (按 ADMET-Score 排序)

| 排名 | LIGAND_ID | IC50 (μM) | QED | ADMET-Score | 等級 |
|------|-----------|-----------|-----|-------------|------|
| 1 | CmpdCT00670282 | 0.075 | 0.369 | **0.2479** | ⚠️ |
| 2 | CmpdCT00670289 | 0.85 | 0.369 | **0.2479** | ⚠️ |
| 3 | CmpdCT00670285 | 0.25 | 0.359 | **0.2360** | ⚠️ |
| 4 | CmpdCT00670291 | 1.8 | 0.359 | **0.2360** | ⚠️ |
| 5 | CmpdCT00670274 | 0.0013 | 0.499 | **0.2324** | ⚠️ |
| 6 | CmpdCT00670280 | 0.038 | 0.427 | **0.2248** | ⚠️ |
| 7 | CmpdCT00670287 | 0.48 | 0.427 | **0.2248** | ⚠️ |
| 8 | CmpdCT04372176 | 0.003 | 0.486 | **0.2203** | ⚠️ |
| 9 | CmpdCT00670278 | 0.015 | 0.404 | **0.2019** | ⚠️ |
| 10 | CmpdCT00670283 | 0.12 | 0.404 | **0.2019** | ⚠️ |

**最佳化合物分析**:
- **CmpdCT00670282** 和 **CmpdCT00670289** - ADMET-Score 最高 (0.2479)
- **CmpdCT00670274** - IC50 最低 (0.0013 μM)，但 ADMET-Score 僅第 5 名
- 顯示 potency 和 ADMET 性質不完全相關

---

## 🧬 18 個 ADMET 端點說明

ADMET-Score 基於 admetSAR 2.0 的 18 個 ADMET 端點計算：

### 有害端點 (預測為有害則降低分數)

1. **Ames mutagenicity** (準確率 84.3%) - 致突變性檢測
2. **Acute oral toxicity** (準確率 83.2%) - 急性口服毒性
3. **Carcinogenicity** (準確率 81.6%) - 致癌性
4. **CYP inhibitory promiscuity** (準確率 82.1%) - CYP 抑制多重性
5. **CYP1A2 inhibitor** (準確率 81.5%)
6. **CYP2C19 inhibitor** (準確率 80.5%)
7. **CYP2C9 inhibitor** (準確率 80.2%)
8. **CYP2D6 inhibitor** (準確率 85.5%)
9. **CYP3A4 inhibitor** (準確率 64.5%)
10. **hERG inhibitor** (準確率 80.4%) - 心毒性
11. **OCT2 inhibitor** (準確率 80.8%)
12. **P-gp inhibitor** (準確率 86.1%)

### 有益端點 (預測為有益則提升分數)

13. **CYP2C9 substrate** (準確率 77.9%)
14. **CYP2D6 substrate** (準確率 77.5%)
15. **CYP3A4 substrate** (準確率 66.0%)
16. **P-gp substrate** (準確率 80.2%)
17. **Caco-2 permeability** (準確率 76.8%) - 腸道穿透性
18. **Human intestinal absorption** (準確率 96.5%) - 腸道吸收

---

## 📈 ADMET-Score 與 QED 比較

### 相關性分析

| 性質 | 平均值 | 標準差 | 最小值 | 最大值 |
|------|--------|--------|--------|--------|
| QED | 0.425 | - | - | - |
| ADMET-Score | 0.208 | 0.023 | 0.178 | 0.248 |

### 觀察

**ADMET-Score 與 QED 的差異**:
- QED 主要基於物理化學性質 (MW, LogP, HBA, HBD 等 8 個參數)
- ADMET-Score 整合 18 個代謝、毒性相關端點
- 本研究中 ADMET-Score 明顯低於 QED，表明：
  - 化合物物理性質尚可
  - 但代謝和毒性風險較高

**與論文的比較**:
- 論文發現 QED 和 ADMET-Score 無明顯線性相關
- 這支持了兩個指標的互補性
- 建議同時使用 QED 和 ADMET-Score 進行藥物篩選

---

## 💡 優化建議

### 1. 降低 CYP 抑制風險

**當前狀況**: 大部分化合物有 CYP 抑制風險
**建議**:
- 修飾結構以降低 CYP3A4、CYP2C9 抑制
- 避免引入易被氧化的官能團 (如雜環、硫醚)

### 2. 降低 hERG 毒性

**當前狀況**: hERG 抑制風險較高
**建議**:
- 減少陽性中心 (碱性氮原子)
- 降低 LogP (減少疏水性)
- 避免長鏈疏水結構

### 3. 改善代謝穩定性

**當前狀況**: 代謝酶底物/抑制劑比例不佳
**建議**:
- 優化 CYP 基質性質
- 降低代謝不穩定性
- 增加代謝穩定官能團

### 4. 維持 potency

**觀察**: ADMET-Score 最佳的化合物 IC50 並非最低
**建議**:
- 在優化 ADMET 同時保持 potency
- 優先優化 ADMET-Score 0.20-0.25 範圍的化合物
- 這些化合物潛力最大

---

## 📝 方法說明

### ADMET-Score 計算公式

ADMET-Score = Σ(qᵢ × wᵢ) / Σwᵢ

其中：
- **qᵢ**: 轉換後的預測值 (0 或 1)
  - 有害端點：預測安全 = 1, 預測風險 = 0
  - 有益端點：預測有益 = 1, 預測無益 = 0
- **wᵢ**: 權重 = w1 × w2 × w3
  - **w1 (Usefulness Index)**: 基於 DrugBank 中有益藥物的比例
  - **w2 (Model Accuracy)**: admetSAR 2.0 模型準確率
  - **w3 (Importance)**: 藥代動力學過程中的相對重要性

### 權重設定

| 端點 | 準確率 (w2) | 重要性 (w3) | 計算權重 |
|------|-----------|-----------|---------|
| Ames | 0.843 | 0.9 | 0.643 |
| hERG | 0.804 | 0.9 | 0.613 |
| HIA | 0.965 | 0.9 | 0.735 |
| CYP3A4 inhib | 0.645 | 0.85 | 0.465 |
| P-gp inhib | 0.861 | 0.75 | 0.621 |
| Caco-2 | 0.768 | 0.8 | 0.587 |

### 解讀指南

- **ADMET-Score = 1**: 完美藥物特性 (參考 DrugBank 批准藥物)
- **ADMET-Score = 0**: 最差藥物特性
- **分數越高越好**: 表示更接近批准藥物的 ADMET 特性

---

## 📁 數據檔案

### 已上傳至 GitHub

- **原始 ADMET-AI 結果**: `3clpro_admet_analysis_2026-03-23_admet_ai.csv` (112 端點)
- **ADMET-Score 結果**: `3clpro_admet_score_2026-03-23.csv` (含 18 端點 + ADMET-Score)
- **本報告**: `3clpro_admet_score_report_2026-03-23.md`

**倉庫**: https://github.com/c00jsw00/openclawdailyreport

---

## 📚 引用文獻

1. **ADMET-score 論文**: [PMC6350845](https://pmc.ncbi.nlm.nih.gov/articles/PMC6350845/)
   - 標題：ADMET-score – a comprehensive scoring function for evaluation of chemical drug-likeness
   - 方法：admetSAR 2.0 的 18 個 ADMET 端點
   - 評估：DrugBank 批准藥物、ChEMBL 小分子、市場撤銷藥物

2. **ADMET-AI**: [admet_ai GitHub](https://github.com/swansonk14/admet_ai)
   - 方法：Chemprop-RDKit 圖神經網絡
   - 性能：TDC ADMET Benchmark leaderboard #1
   - 端點：104 個 ADMET 性質

---

*報告生成時間：2026-03-23 08:00*  
*ADMET-Score 基於論文 [PMC6350845](https://pmc.ncbi.nlm.nih.gov/articles/PMC6350845/) 方法計算*
