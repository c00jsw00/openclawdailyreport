# Boltz-2 蛋白質 - 配體複合體分析報告

**日期：** 2026-03-21 22:50  
**工具：** Boltz-2 v2.2.1 (CPU 模式)  
**狀態：** ✅ 完成

---

## 1. 輸入數據

### 蛋白質序列
**長度：** 234 個氨基酸殘基

```
ASAMFRKLAAESFGTFWLVFGGSGSAVLAAGFPELGIGFAGVALAFGLTVLTMAFAVGHISGGHFNPAVTIGLWAGGRFPAKEVVGYVIAQVVGGIVAAALLYLIASGKTGFDAAASGFASNGYGEHSPGGYSMLSALVVELVLSAGFLLVIHGATDKFAPAGFAPIAIGLALTLIHLISIPVTNCSVNPARSTAVAIFQGGWALEQLWFFWVVPIVGGIIGGLIYRTLLEKRD
```

### 配體
**SMILES:** `CC(=CCOc1ccc(\C=C\C(=O)c2ccc(OCC=C(C)C)cc2OCCCC(=O)O)cc1)C`

**基本性質：**
- **分子量 (MW):** 478.59 Da
- **LogP:** 6.52
- **氫鍵 acceptors:** 5
- **氫鍵 donors:** 1
- **TPSA:** 82.06 Å²
- **可旋轉鍵:** 14

---

## 2. Boltz-2 執行結果

### 執行配置
```bash
/home/c00jsw00/anaconda3/envs/boltz2/bin/boltz predict \
  input/boltz2_input.yaml \
  --out_dir structures \
  --accelerator cpu \
  --model boltz2 \
  --use_msa_server \
  --diffusion_samples 1 \
  --recycling_steps 3 \
  --no_kernels
```

### 執行狀態
- ✅ **MSA 生成完成** - 使用 ColabFold 服务器
- ✅ **結構預測完成** - 3.21 分鐘 (CPU 模式)
- ✅ **親和力預測完成** - 5 分鐘 (CPU 模式)
- ✅ **總執行時間：** ~8.5 分鐘

---

## 3. 結構預測結果

### 結構置信度評分

| 指標 | 數值 | 說明 |
|------|------|------|
| **pLDDT** | 90.61 | 局部結構置信度 (0-100) |
| **pTM** | 0.874 | 全局結構置信度 |
| **ipTM** | 0.697 | 複合體相互作用置信度 |
| **ligand_iptm** | 0.697 | 配體結合界面置信度 |

### 結構質量評估

| pLDDT 範圍 | 質量等級 | 說明 |
|------------|----------|------|
| > 90 | **Excellent** | 極高置信度 |
| 70-90 | **Good** | 高置信度 |
| 50-70 | **Acceptable** | 中等置信度 |
| < 50 | **Poor** | 低置信度 |

**您的結果：** pLDDT = 90.61 → **Excellent (極高置信度)** ⭐

### 鏈間相互作用

| 鏈 | pTM |
|----|-----|
| 蛋白質 (鏈 0) | 0.905 |
| 配體 (鏈 1) | 0.724 |

**複合體 ipTM:** 0.697 - 表示配體結合界面有良好置信度

---

## 4. 結合親和力預測結果

### 預測結果摘要

| 指標 | 數值 | 說明 |
|------|------|------|
| **Predicted log10(IC50)** | 0.455 | 預測親和力 (μM) |
| **IC50** | 2.85 μM | 抑制濃度 |
| **Binder Probability** | 10.74% | 結合概率 |
| **Classification** | **Non-binder** | 分類 |

### 多模型預測結果

Boltz-2 使用 3 個模型進行預測，結果如下：

| 模型 | log10(IC50) | IC50 (μM) | Binder Probability |
|------|-------------|-----------|-------------------|
| Model 0 | 0.455 | 2.85 | 10.74% |
| Model 1 | 0.578 | 3.78 | 10.50% |
| Model 2 | 0.332 | 2.15 | 10.99% |

**平均 IC50:** ~2.93 μM  
**平均 Binder Probability:** 10.74%

### 親和力解釋

| IC50 範圍 | 結合強度 | 分類 |
|----------|----------|------|
| < 1 nM | 極強結合 | Extremely tight |
| 1-10 nM | 很強結合 | Very tight |
| 10-100 nM | 強結合 | Tight |
| 100 nM - 1 μM | 中等結合 | Moderate |
| **1-10 μM** | **弱結合** | **Weak** |
| > 10 μM | 極弱結合 | Very weak |

**您的結果：** IC50 = 2.85 μM → **弱結合 (Weak)**

### 結合概率分類

| 概率範圍 | 分類 | 說明 |
|----------|------|------|
| > 80% | **Strong Binder** | 強結合劑 |
| 50-80% | **Binder** | 結合劑 |
| 30-50% | **Weak Binder** | 弱結合劑 |
| **< 30%** | **Non-binder** | **非結合劑** |

**您的結果：** 10.74% → **Non-binder (非結合劑)** ⚠️

**結論：** 根據 Boltz-2 預測，此配體與蛋白質的結合概率較低 (10.74%)，屬於**非結合劑 (Non-binder)**。建議考慮優化配體結構以增強結合親和力。

---

## 5. 結構輸出文件

```
/home/c00jsw00/.openclaw/workspace/protein_ligand_analysis/structures/boltz_results_boltz2_input/
├── predictions/
│   └── boltz2_input/
│       ├── boltz2_input_model_0.cif       ✅ 預測結構 (MMCIF 格式)
│       ├── boltz2_input_model_0.pdb       ✅ 預測結構 (PDB 格式)
│       ├── confidence_boltz2_input_model_0.json  ✅ 置信度評分
│       └── affinity_boltz2_input.json     ✅ 親和力預測結果
├── processed/
│   ├── records/
│   │   └── boltz2_input.json              ✅ 處理後的輸入
│   └── manifest.json                      ✅ 輸出清單
└── lightning_logs/                        ✅ 訓練日誌
```

### 結構文件
- **model_0.cif:** AlphaFold/Boltz-2 標準 MMCIF 格式
- **model_0.pdb:** 標準 PDB 格式，可用於 PyMOL/ChimeraX 等軟體

---

## 6. 結果分析

### 結構質量
- **pLDDT = 90.61** - 結構預測質量**極佳** (Excellent)
- **pTM = 0.874** - 全局結構置信度高
- **ipTM = 0.697** - 複合體結合界面置信度良好

### 親和力預測
- **IC50 = 2.85 μM** - 弱結合
- **Binder Probability = 10.74%** - 非結合劑

### 綜合評估

雖然結構預測質量很高 (pLDDT > 90)，但親和力預測顯示此配體與蛋白質的結合概率較低。這可能表示：

1. **配體設計需要優化** - 考慮增加與蛋白質的相互作用
2. **結合模式可能不正確** - 可能需要探索其他結合模式
3. **假陽性/假陰性** - ML 模型可能存在誤差

### 建議後續步驟

1. **配體優化**
   - 增加氫鍵供體/受體
   - 優化疏水相互作用
   - 減少可旋轉鍵以提高結合熵

2. **結構驗證**
   - 使用 PyMOL/ChimeraX 查看結構
   - 分析結合口袋
   - 檢查配體位置

3. **其他預測方法**
   - 使用 RFdiffusion 重新設計
   - 嘗試其他 ML 模型 (AlphaFold-Multimer)
   - 進行分子動力學模擬驗證

---

## 7. 結構視覺化

### 使用 PyMOL
```bash
pymol boltz2_input_model_0.pdb
```

### 使用 ChimeraX
```bash
chimerax boltz2_input_model_0.pdb
```

### 使用 Jupyter + NGL
```python
from nglview import show_pdb
show_pdb('boltz2_input_model_0.pdb')
```

---

## 8. 技術細節

### MSA 生成
- **服務器:** ColabFold API
- **策略:** Greedy pairing
- **生成時間:** ~1.63 秒

### 結構預測
- **模型:** Boltz-2
- **加速:** CPU
- **Recycling 步驟:** 3
- **採樣次數:** 1
- **結構預測時間:** ~3.21 分鐘

### 親和力預測
- **採樣次數:** 5
- **預測時間:** ~5 分鐘
- **模型數量:** 3

### 總執行時間
- **CPU 模式:** ~8.5 分鐘
- **GPU 模式 (預估):** ~2-3 分鐘

---

## 9. 注意事項

### CPU 模式限制
- 執行速度較慢 (~8.5 分鐘 vs ~2-3 分鐘)
- 使用了 `--no_kernels` 參數以避免 cuEquivariance 依賴問題
- 功能完整，所有預測均成功完成

### 親和力預測準確性
- Boltz-2 親和力預測基於 ML 模型
- 對於訓練數據中的類似配體較準確
- 對於新結構的配體可能有誤差
- 建議使用實驗驗證

### 置信度解讀
- **pLDDT > 90:** 極高置信度
- **pTM > 0.8:** 高置信度
- **ipTM > 0.6:** 良好結合界面置信度

---

## 10. 資源

- **Boltz-2 GitHub:** https://github.com/jwohlwend/boltz
- **Boltz-2 Paper:** https://doi.org/10.1101/2025.06.14.659707
- **OpenClaw Boltz-2 Skill:** `/home/c00jsw00/.openclaw/workspace/skills/boltz2/`
- **GitHub Repository:** https://github.com/c00jsw00/openclawdailyreport

---

## 11. 報告檔案

- **本報告:** `analysis_report_2026-03-21_boltz2.md`
- **結構文件:** `boltz2_input_model_0.cif` / `.pdb`
- **置信度評分:** `confidence_boltz2_input_model_0.json`
- **親和力結果:** `affinity_boltz2_input.json`

---

*報告生成時間：2026-03-21 22:50*  
*Boltz-2 版本：2.2.1 (CPU 模式，--no_kernels)*  
*OpenClaw 自動化分析流程*
