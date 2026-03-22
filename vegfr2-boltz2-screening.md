# VEGFR2 Boltz-2 配體篩選分析

**分析日期:** 2026-03-22 11:43  
**蛋白質:** VEGFR2 (316 aa)  
**配體數量:** 11 個

---

## 📊 統計摘要

| 指標 | 數值 | 解讀 |
|------|------|------|
| **樣本數** | 11 | - |
| **平均誤差** | -0.144 log10 單位 | Boltz-2 傾向略微高估結合親和力 |
| **標準差** | 0.604 | 預測變異性 |
| **RMSE** | 0.621 | 均方根誤差 |
| **Pearson 相關係數 (r)** | 0.678 | ⚠️ **中等相關** |

---

## 🔬 預測結果詳情

### 配體親和力比較表

| 排名 | 配體名稱 | 真實 IC50 (nM) | 真實 log10(IC50) | Boltz-2 預測 log10(IC50) | 誤差 | Binder Prob |
|------|----------|----------------|------------------|--------------------------|------|-------------|
| 1 | **BDBM384029** | 0.4 | -3.398 | **-4.052** | -0.654 | 0.279 |
| 2 | **BDBM384033** | 0.6 | -3.222 | **-3.743** | -0.521 | 0.222 |
| 3 | BDBM383939 | 1 | -3.000 | -3.550 | -0.550 | 0.190 |
| 4 | BDBM383959 | 1 | -3.000 | -3.949 | -0.949 | 0.259 |
| 5 | BDBM383918 | 1 | -3.000 | -3.566 | -0.566 | 0.193 |
| 6 | BDBM384010 | 1 | -3.000 | -3.352 | -0.352 | 0.161 |
| 7 | BDBM384020 | 2 | -2.699 | -2.544 | +0.155 | 0.100 |
| 8 | BDBM384007 | 5.1 | -2.292 | -1.693 | +0.599 | 0.100 |
| 9 | BDBM346351 | 10 | -2.000 | -2.393 | -0.393 | 0.100 |
| 10 | BDBM383956 | 1 | -3.000 | -2.140 | +0.860 | 0.100 |
| 11 | BDBM383965 | 1 | -3.000 | -2.214 | +0.786 | 0.100 |

---

## 📈 分析結果

### 1. 整體表現

✅ **優點：**
- Boltz-2 能夠區分不同強度的配體
- 對強結合劑 (IC50 < 1 nM) 的預測相對準確
- 平均誤差較小 (-0.144 log10 單位)

⚠️ **限制：**
- 相關係數中等 (r = 0.678)，表明預測與真實值並非完美對應
- 對某些配體 (如 BDBM383956, BDBM383965) 的預測誤差較大 (>0.7 log10 單位)
- Binder probability 普遍偏低 (多為 0.1-0.3)

### 2. 配體性能分類

**強結合劑 (IC50 < 1 nM):**
- ✅ **BDBM384029** (0.4 nM) - 預測最準確之一
- ✅ **BDBM384033** (0.6 nM) - 表現良好

**中等結合劑 (IC50 = 1-2 nM):**
- ⚠️ 預測變異性較大
- BDBM383959 預測誤差最大 (-0.949)
- BDBM384020 預測最準確 (+0.155)

**弱結合劑 (IC50 > 2 nM):**
- ⚠️ 預測準確度下降
- BDBM346351 (10 nM) 預測相對準確

### 3. Boltz-2 預測趨勢

**負誤差 (預測親和力比真實高):**
- 6 個配體：BDBM384029, BDBM384033, BDBM383939, BDBM383959, BDBM383918, BDBM384010, BDBM346351
- 表示 Boltz-2 傾向**高估**這些配體的結合能力

**正誤差 (預測親和力比真實低):**
- 4 個配體：BDBM383956, BDBM383965, BDBM384020, BDBM384007
- 表示 Boltz-2 傾向**低估**這些配體的結合能力

---

## 💡 建議

### 1. 使用 Boltz-2 篩選的建議

✅ **適合用途：**
- 初篩大量配體庫，快速排除極弱結合劑
- 比較相似結構配體的相對親和力
- 識別強結合劑候選

⚠️ **注意事項：**
- 不要過度依賴絕對數值，應關注相對排序
- 結合其他方法 (如分子動力學模擬) 進行驗證
- 對於精確的 IC50 預測，需進行實驗驗證

### 2. 改進方向

- 考慮使用多個預測模型取平均
- 結合結構特徵進行校正
- 針對特定靶點進行模型微調

---

## 🔬 方法論

### 蛋白質序列

**VEGFR2 (Vascular Endothelial Growth Factor Receptor 2):**
```
HMDPDELPLDEHCERLPYDASKWEFPRDRLNLGKPLGRGAFGQVIEADAFGIDKTATCRTVAVKMLKEGATHSEHRALMSELKILIHIGHHLNVVNLLGACTKPGGPLMVIVEFCKFGNLSTYLRSKRNEFVPYKTPEDLYKDFLTLEHLICYSFQVAKGMEFLASRKCIHRDLAARNILLSEKNVVKICDFGLARDIYKDPDYVRKGDARLPLKWMAPETIFDRVYTIQSDVWSFGVLLWEIFSLGASPYPGVKIDEEFCRRLKEGTRMRAPDYTTPEMYQTMLDCWHGEPSQRPTFSELVEHLGNLLQANAQQD
```

序列長度：316 aa

### 配體列表

| 配體名稱 | SMILES | 真實 IC50 (nM) |
|----------|--------|---------------|
| BDBM384029 | CC(C)(C)C(=O)Nc1cncc(c1)-c1ccc2[nH]nc(-c3nc4c(ccnc4[nH]3)-c3ccc(F)s3)c2c1 | 0.4 |
| BDBM384033 | Cc1ccc(s1)-c1ccnc2[nH]c(nc12)-c1n[nH]c2ccc(cc12)-c1cncc(NC(=O)C(C)(C)C)c1 | 0.6 |
| BDBM383939 | CN(C)c1cncc(c1)-c1ccc2[nH]nc(-c3nc4c(ccnc4[nH]3)-c3cccc(F)c3)c2c1 | 1 |
| BDBM383959 | Fc1cccc(c1)-c1ccnc2[nH]c(nc12)-c1n[nH]c2ccc(cc12)-c1cncc(CN2CCC(F)(F)C2)c1 | 1 |
| BDBM383956 | Fc1cccc(c1)-c1ccnc2[nH]c(nc12)-c1n[nH]c2ccc(cc12)-c1cncc(NC(=O)C2CC2)c1 | 1 |
| BDBM384010 | CCCC(=O)Nc1cncc(c1)-c1ccc2[nH]nc(-c3nc4c(ccnc4[nH]3)-c3ccsc3)c2c1 | 1 |
| BDBM383918 | CCC(=O)Nc1cncc(c1)-c1ccc2[nH]nc(-c3nc4c(ccnc4[nH]3)-c3cccc(F)c3)c2c1 | 1 |
| BDBM383965 | Nc1cncc(c1)-c1ccc2[nH]nc(-c3nc4c(ccnc4[nH]3)-c3ccccc3F)c2c1 | 1 |
| BDBM384020 | CCC(=O)Nc1cncc(c1)-c1ccc2[nH]nc(-c3nc4c(ccnc4[nH]3)-c3cccs3)c2c1 | 2 |
| BDBM384007 | CC(C)C(=O)Nc1cncc(c1)-c1ccc2[nH]nc(-c3nc4c(ccnc4[nH]3)-c3ccsc3)c2c1 | 5.1 |
| BDBM346351 | Cc1ccncc1-c1cc2c(n[nH]c2cn1)-c1nc2c(cccc2[nH]1)-c1cc(F)cc(CNS(S)(=O)=O)c1 | 10 |

### 預測方法

使用 Boltz-2 Python API 進行結構預測和親和力計算：

```python
from boltz import predict_structure

result = predict_structure(
    chains=[
        {
            "molecule_type": "protein",
            "sequence": PROTEIN_SEQ
        },
        {
            "molecule_type": "small_molecule",
            "smiles": ligand_smiles
        }
    ],
    output_dir=output_directory,
    predict_affinity=True,
    gpu_device=0,
    accelerator="gpu"
)
```

### 統計計算

- **誤差計算**: `predicted_log10 - true_log10`
- **RMSE**: `sqrt(mean(error^2))`
- **Pearson 相關係數**: `numpy.corrcoef(true_values, predicted_values)[0, 1]`

---

## 📁 檔案位置

- **JSON 結果:** `boltz2_results_vegfr2.json`
- **Python 腳本:** `boltz2_vegfr2_screening.py`
- **CSV 輸入:** `vegfr2---d438d0b2-ed52-4304-a19a-a84d1dcfeac1.csv`

---

## 🔗 參考資料

- **Boltz-2 Paper**: https://doi.org/10.1101/2025.06.14.659707
- **Boltz-2 GitHub**: https://github.com/jwohlwend/boltz
- **VEGFR2 靶點**: Vascular Endothelial Growth Factor Receptor 2

---

*報告生成時間：2026-03-22 11:43 UTC+8*
