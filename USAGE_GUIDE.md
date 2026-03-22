# Boltz-2 Skill 使用指南

## 🎯 如何呼叫品丸使用 Boltz-2

### 基本語法

```
品丸，請用 boltz-2 [分析任務]

[提供必要的參數]
```

---

## 📋 使用範例

### 範例 1：單個配體結合親和力預測

**指令：**
```
品丸，請幫我預測蛋白質與配體的複合物結構並計算結合親和力

蛋白質序列：HMDPDELPLDEHCERLPYDASKWEFPRDRLNLGKPLGRGAFGQVIEADAFGIDKTATCRTVAVKMLKEGATHSEHRALMSELKILIHIGHHLNVVNLLGACTKPGGPLMVIVEFCKFGNLSTYLRSKRNEFVPYKTPEDLYKDFLTLEHLICYSFQVAKGMEFLASRKCIHRDLAARNILLSEKNVVKICDFGLARDIYKDPDYVRKGDARLPLKWMAPETIFDRVYTIQSDVWSFGVLLWEIFSLGASPYPGVKIDEEFCRRLKEGTRMRAPDYTTPEMYQTMLDCWHGEPSQRPTFSELVEHLGNLLQANAQQD
配體 SMILES: N[C@@H](Cc1ccc(O)cc1)C(=O)O  (多巴胺)
```

**預期輸出：**
- 3D 結構預測 (PDB/CIF 檔案)
- 結合親和力預測 (log10(IC50) in μM)
- Binder probability
- 置信度指標 (pLDDT, pTM)

---

### 範例 2：多個配體篩選比較

**指令：**
```
品丸，請幫我測試這 3 個配體與蛋白質的結合能力，比較誰的親和力最好

蛋白質序列：HMDPDELPLDEHCERLPYDASKWEFPRDRLNLGKPLGRGAFGQVIEADAFGIDKTATCRTVAVKMLKEGATHSEHRALMSELKILIHIGHHLNVVNLLGACTKPGGPLMVIVEFCKFGNLSTYLRSKRNEFVPYKTPEDLYKDFLTLEHLICYSFQVAKGMEFLASRKCIHRDLAARNILLSEKNVVKICDFGLARDIYKDPDYVRKGDARLPLKWMAPETIFDRVYTIQSDVWSFGVLLWEIFSLGASPYPGVKIDEEFCRRLKEGTRMRAPDYTTPEMYQTMLDCWHGEPSQRPTFSELVEHLGNLLQANAQQD

配體列表：
1. N[C@@H](Cc1ccc(O)cc1)C(=O)O  (多巴胺)
2. CC(=O)Oc1ccccc1C(=O)O  (阿斯匹靈)
3. CCO  (乙醇)

請預測所有複合物結構並計算親和力，給我比較報告
```

**預期輸出：**
- 所有配體的預測結果
- 親和力排名
- 統計分析 (平均誤差、相關係數等)

---

### 範例 3：從 CSV 批量篩選

**指令：**
```
品丸，我有一個 CSV 檔案，包含配體名稱、SMILES 和真實 IC50 值

請幫我：
1. 讀取 CSV 檔案
2. 用 boltz-2 預測每個配體與蛋白質的結合能力
3. 比較 boltz-2 預測值與真實 IC50 的差異
4. 計算統計指標 (相關係數、RMSE 等)
5. 生成分析報告

蛋白質序列：[提供序列]
CSV 檔案：[上傳檔案]
```

---

### 範例 4：結構視覺化

**指令：**
```
品丸，請將 boltz-2 計算結果轉成結構圖

輸入檔案：/home/c00jsw00/.openclaw/workspace/protein_ligand_analysis/structures/boltz_results_boltz2_input/predictions/boltz2_input/boltz2_input_model_0.cif
輸出檔案：structure.png
視圖類型：cartoon
解析度：1920x1080
背景：白色
```

**預期輸出：**
- 高品質的蛋白質 - 配體複合物結構圖
- 可包含配體、蛋白質骨架、結合口袋等

---

### 範例 5：生成旋轉動畫

**指令：**
```
品丸，請將 boltz-2 預測的結構轉成 360°旋轉動畫 GIF

輸入檔案：boltz2_input_model_0.cif
輸出檔案：structure_rotation.gif
幀數：36 幀
解析度：1280x720
```

---

### 範例 6：RNA/DNA 結構預測

**指令：**
```
品丸，請預測這段 RNA 序列的 3D 結構

RNA 序列：GCGCGCGCGC
輸出目錄：./rna_structure
```

---

## 🔧 參數說明

### 必要參數

| 參數 | 類型 | 說明 |
|------|------|------|
| `蛋白質序列` | string | 單字母氨基酸序列 |
| `配體 SMILES` | string | 小分子 SMILES 格式 |
| `輸出目錄` | string | 結果保存路徑 |

### 可選參數

| 參數 | 類型 | 預設值 | 說明 |
|------|------|--------|------|
| `predict_affinity` | bool | True | 是否計算親和力 |
| `gpu_device` | int | 0 | GPU 設備索引 |
| `accelerator` | string | "gpu" | "gpu" 或 "cpu" |
| `diffusion_samples` | int | 1 | 結構採樣數量 |
| `recycling_steps` | int | 3 | 回收迭代次數 |

---

## 📊 結果解讀

### 親和力指標

**log10(IC50) in μM:**
- 值越小，結合越強
- -9 = 1 nM (極強結合)
- -6 = 1 μM (中等結合)
- -4 = 100 μM (弱結合)

**Binder Probability (0-1):**
- >0.8: 強結合劑
- 0.5-0.8: 可能結合
- 0.3-0.5: 弱結合 / 不確定
- <0.3: 不結合

### 結構置信度

**pLDDT (per-residue confidence):**
- >90: 非常高信度
- 70-90: 高信度
- 50-70: 低信度
- <50: 非常低信度

**pTM (predicted Template Modeling):**
- >0.8: 高質量預測
- 0.5-0.8: 中等質量
- <0.5: 低質量

---

## 💡 最佳實踐

### ✅ 推薦做法

1. **預篩大量配體**：使用 Boltz-2 快速排除極弱結合劑
2. **比較相對排序**：關注配體之間的相對差異，而非絕對數值
3. **結合多種方法**：與分子動力學模擬、實驗驗證結合
4. **檢查置信度**：注意 pLDDT 和 pTM 指標

### ⚠️ 注意事項

1. **誤差範圍**：Boltz-2 通常有 0.5-1.0 log10 的誤差
2. **不要過度依賴**：預測結果需實驗驗證
3. **注意結構特徵**：某些特殊結構可能影響預測準確性
4. **GPU 需求**：建議使用 RTX 3080/3090/4090 或更高

---

## 📁 實際案例

### VEGFR2 配體篩選 (2026-03-22)

**完整報告：** [vegfr2-boltz2-screening.md](./vegfr2-boltz2-screening.md)

**分析結果：**
- 測試 11 個配體
- Pearson 相關係數：r = 0.678 (中等相關)
- 最佳配體：BDBM384029 (0.4 nM)

**指令範例：**
```
品丸，csv 檔案上欄位分別為 name, smile and IC50(nM)，name 是配體名稱，smile 為配體的 smile 格式，IC50(nM) 是配體真實的 IC50 (nM) 的數值，用 boltz-2 預測請幫我測試 csv 檔案的配體與蛋白質的結合能力，並分析 boltz-2 的親和力與真實的 IC50 (nM) 的數值差異

蛋白質序列：HMDPDELPLDEHCERLPYDASKWEFPRDRLNLGKPLGRGAFGQVIEADAFGIDKTATCRTVAVKMLKEGATHSEHRALMSELKILIHIGHHLNVVNLLGACTKPGGPLMVIVEFCKFGNLSTYLRSKRNEFVPYKTPEDLYKDFLTLEHLICYSFQVAKGMEFLASRKCIHRDLAARNILLSEKNVVKICDFGLARDIYKDPDYVRKGDARLPLKWMAPETIFDRVYTIQSDVWSFGVLLWEIFSLGASPYPGVKIDEEFCRRLKEGTRMRAPDYTTPEMYQTMLDCWHGEPSQRPTFSELVEHLGNLLQANAQQD
```

---

## 🔗 相關資源

- **Boltz-2 Paper**: https://doi.org/10.1101/2025.06.14.659707
- **Boltz-2 GitHub**: https://github.com/jwohlwend/boltz
- **Boltz-2 Slack**: https://boltz.bio/join-slack

---

*最後更新：2026-03-22*
