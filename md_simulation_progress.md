# OpenMM MD Simulation - 進度報告

**日期：** 2026-03-21 23:55  
**測試對象：** Boltz-2 預測結構  
**目標：** 10ns MD 模擬在 GPU 2 上

---

## 📊 目前進度

### ✅ 已完成

1. **系統資源檢查**
   - GPU: 3 個 (2x AMD Radeon AI PRO R9700, 1x Ryzen 7 9700X)
   - OpenMM 8.5 ✅
   - AmberTools 24.8 ✅
   - PyTorch 2.10.0 + ROCm 7.1 ✅

2. **Boltz-2 結構預測**
   - 文件：`boltz2_input_model_0.cif`
   - pLDDT: 90.61 (Excellent)
   - 原子數：1730

3. **技能創建**
   - `openmm-md` 技能 ✅
   - `boltz2-visualizer` 技能 ✅

---

### ⚠️ 遇到的問題

#### 問題 1: tleap 無法讀取 Boltz-2 CIF 格式

**錯誤：**
```
FATAL:  Atom .R<AL 177>.A<N 2> does not have a type.
Failed to generate parameters
```

**原因：** Boltz-2 輸出的 CIF 文件格式與 AmberTools 不兼容

**解決方案：** 使用 OpenMM 直接讀取，跳過 tleap

#### 問題 2: OpenMM 無法讀取 Boltz-2 CIF

**錯誤：**
```
Misaligned residue name: HETATM 1696 C C61 . LIG1 . 1
```

**原因：** Boltz-2 的 CIF 格式包含非標準的配體命名

**解決方案：** 需要預處理 CIF 文件或創建簡化測試系統

---

## 🔧 已創建的腳本

### 1. 簡化 MD 模擬腳本
**路徑：** `md_simulation_direct.py`

**功能：**
- 直接從 PDB/CIF 讀取
- 使用 OpenMM 創建系統
- GB/SA 隱含溶劑模型
- GPU 加速

**限制：** 需要標準 PDB 格式

### 2. 簡易測試腳本
**路徑：** `simple_md.py`

**使用方式：**
```bash
python3 simple_md.py <pdb_file> <output_dir> <time_ns> <temperature>
```

**例子：**
```bash
python3 simple_md.py structure.pdb md_output 10.0 300.0
```

---

## 📝 建議解決方案

### 方案 A: 使用簡化測試系統 (推薦)

創建一個小型測試系統，不依賴 Boltz-2 的 CIF 文件：

1. 從 PDB 庫下載小型蛋白質結構
2. 運行 MD 測試
3. 驗證 OpenMM + GPU 配置正確

**優點：**
- 快速驗證
- 排除格式問題
- 確認 GPU 工作正常

**命令：**
```bash
# 下載測試結構
wget https://www.rcsb.edu/pdb/files/1TIM.pdb

# 運行 MD
python3 simple_md.py 1TIM.pdb md_test 0.1 300.0
```

### 方案 B: 預處理 Boltz-2 CIF

使用 Python 轉換 CIF 為標準 PDB：

```python
from Bio.PDB import PDBParser, PDBIO, Select

# 讀取 CIF (需要 mmCIF 解析器)
# 轉換為標準 PDB
# 保存為 clean.pdb
```

**優點：**
- 保持 Boltz-2 結構
- 可重複使用

**挑戰：**
- 需要處理配體命名
- 可能需要手動修正

### 方案 C: 使用 PyMOL 轉換

如果 PyMOL 可用：

```python
import pymol
from pymol import cmd

cmd.load("boltz2_input_model_0.cif")
cmd.save("clean_structure.pdb")
```

---

## 🎯 下一步行動

### 立即行動

1. **測試簡化系統** (5 分鐘)
   ```bash
   cd /home/c00jsw00/.openclaw/workspace/protein_ligand_analysis
   wget https://www.rcsb.edu/pdb/files/1TIM.pdb
   python3 simple_md.py 1TIM.pdb md_test 0.1 300.0
   ```

2. **驗證 GPU 工作**
   - 檢查 CUDA/ROCm 平台
   - 確認能量計算正確

3. **運行完整 10ns 模擬**
   - 使用測試系統驗證
   - 然後應用到 Boltz-2 結構

### 中期行動

4. **修復 Boltz-2 CIF 轉換**
   - 開發 CIF → PDB 轉換工具
   - 處理配體命名問題

5. **整合完整流程**
   - Boltz-2 → 轉換 → OpenMM MD → MMPBSA

### 長期行動

6. **建立自動化流程**
   - 批處理多結構
   - 自動上傳 GitHub

---

## 📁 相關文件

| 文件 | 路徑 | 說明 |
|------|------|------|
| `md_simulation_direct.py` | `/protein_ligand_analysis/` | 完整 MD 腳本 |
| `simple_md.py` | `/protein_ligand_analysis/` | 簡易測試腳本 |
| `openmm_md_simulator.py` | `/skills/openmm-md/` | OpenMM 技能 |
| `SKILL.md` | `/skills/openmm-md/` | 技能文檔 |

---

## 💡 總結

**當前狀態：** 需要簡化測試系統以驗證 OpenMM + GPU 配置

**主要障礙：** Boltz-2 CIF 格式不兼容 AmberTools 和 OpenMM

**推薦方案：** 使用簡化測試系統 (1TIM.pdb) 先驗證流程，然後再處理 Boltz-2 結構

**預計時間：**
- 簡化測試：5-10 分鐘
- 完整 10ns 模擬：2-4 小時 (GPU 2)
- Boltz-2 轉換：1-2 小時

---

*報告生成時間：2026-03-21 23:55*  
*OpenClaw Protein-Ligand Analysis Project*
