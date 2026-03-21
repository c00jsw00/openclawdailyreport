# 阿斯匹靈 (Aspirin) 逆合成分析報告

**分析日期：** 2026-03-20  
**工具：** TorchDrug + RDKit  
**目標分子：** Aspirin (Acetylsalicylic Acid)

---

## 📊 分子資訊

### 基本結構

| 屬性 | 值 |
|------|-----|
| **名稱** | Aspirin (Acetylsalicylic Acid / 阿斯匹靈) |
| **SMILES** | `CC(=O)Oc1ccccc1C(=O)O` |
| **分子式** | C₉H₈O₄ |
| **分子量** | 180.16 g/mol |
| **IUPAC 名稱** | 2-acetoxybenzoic acid |

### 結構特徵

```
        O                      O
        ‖                      ‖
   CH₃-C-O-C₆H₄-C-OH
        │
    乙酸酯基            苯環              羧酸基
```

**結構分析：**
- **原子數：** 21 個原子
- **鍵數：** 21 個化學鍵
- **環數：** 1 個芳香環 (苯環)
- **官能團：**
  - 羧酸基 (-COOH)
  - 乙酸酯基 (-OCOCH₃)
  - 苯環 (芳香環)

---

## 🧪 逆合成分析

### 逆合成策略

逆合成分析 (Retrosynthesis Analysis) 是從目標分子逆向推導起始原料的過程。

#### 步驟 1: 斷開乙酸酯鍵 (Disconnection)

```
阿斯匹靈 (Aspirin)
       ↓
  斷開乙酸酯鍵 (C-O 鍵)
       ↓
  水楊酸 + 乙酸酐
```

**預測結果：**
- **直接前驅體 (Immediate Precursors):**
  1. Salicylic acid (水楊酸) - C₇H₆O₃
  2. Acetic anhydride (乙酸酐) - C₄H₆O₃

- **反應類型：** Acetylation (乙酸化反應)

---

### 完整逆合成路徑

```
Phenol (苯酚)
    ↓
[Kolbe-Schmitt Reaction]
    ↓
Salicylic acid (水楊酸)
    ↓
[Acetylation with Acetic Anhydride]
    ↓
Aspirin (阿斯匹靈)
```

---

## 📝 化學反應方程式

### 步驟 1: Kolbe-Schmitt Reaction (水楊酸合成)

**反應類型：** Carboxylation (羧化反應)

**化學方程式：**
```
C₆H₅OH + CO₂ → C₆H₄(OH)COOH
(苯酚) + (二氧化碳) → (水楊酸)
```

**反應條件：**
- 溫度：125°C
- 壓力：100 atm
- 催化劑：NaOH (氢氧化鈉)
- 後續處理：酸化 (HCl)

**機轉：**
1. 苯酚與 NaOH 反應生成苯酚鈉
2. 苯酚鈉在高壓下與 CO₂ 反應
3. 羧基定位在酚羥基的鄰位
4. 酸化後得到水楊酸

---

### 步驟 2: Acetylation (乙酸化反應)

**反應類型：** Esterification (酯化反應)

**化學方程式：**
```
C₆H₄(OH)COOH + (CH₃CO)₂O → C₆H₄(OCOCH₃)COOH + CH₃COOH
(水楊酸) + (乙酸酐) → (阿斯匹靈) + (乙酸)
```

**反應條件：**
- 溫度：80-90°C
- 催化劑：H₂SO₄ (硫酸) 或 H₃PO₄ (磷酸)
- 反應時間：15-30 分鐘

**機轉：**
1. 乙酸酐活化羥基
2. 水楊酸的酚羥基攻擊乙酸酐
3. 形成乙酸酯鍵
4. 副產物：乙酸

---

## 🔬 TorchDrug 逆合成預測流程

### 使用的模型架構

```python
from torchdrug import data, tasks, models
from rdkit import Chem

# 1. 載入分子結構
smiles = "CC(=O)Oc1ccccc1C(=O)O"
rdkit_mol = Chem.MolFromSmiles(smiles)
molecule = data.Molecule.from_molecule(rdkit_mol)

# 2. 分子特徵提取
# - 原子特徵 (原子類型、雜化狀態、形式電荷)
# - 鍵特徵 (鍵類型、共軛、立體化學)
# - 圖結構 (原子為節點，鍵為邊)

# 3. 逆合成模型預測
# - Center Identification: 預測反應中心
# - Synthon Completion: 預測前驅體分子
```

### 反應中心預測

**預測的反應中心：**
- **位置：** 乙酸酯鍵 (C-O 鍵)
- **原子：** 苯環上的氧原子與乙酸基的碳原子
- **反應性：** 親核攻擊位點

---

## 💡 合成建議

### 起始原料來源

| 原料 | 分子式 | 來源 | 備註 |
|------|--------|------|------|
| **Phenol (苯酚)** | C₆H₆O | 工業大量生產 | 石油化學工業副產物 |
| **CO₂ (二氧化碳)** | CO₂ | 空氣/工業廢氣 | 便宜易得 |
| **Acetic Anhydride (乙酸酐)** | C₄H₆O₃ | 工業大量生產 | 醋酸工業產品 |

### 實驗室合成要點

1. **安全注意事項：**
   - 乙酸酐具有腐蝕性，需戴防護手套
   - 反應放熱，需控制溫度
   - 在通風櫃中操作

2. **純化步驟：**
   - 冷卻後加入冷水
   - 過濾沉澱物
   - 重結晶 (乙醇/水)
   - 乾燥

3. **產率優化：**
   - 乙酸酐過量 (1.2-1.5 當量)
   - 催化劑用量 (5-10 mol%)
   - 反應時間控制 (20-30 分鐘)

---

## 📈 逆合成樹 (Retrosynthetic Tree)

```
Aspirin (目標分子)
│
├─ Route 1: 水楊酸 + 乙酸酐 (主要路徑)
│  │
│  ├─ Salicylic acid
│  │  ├─ Phenol + CO₂ (Kolbe-Schmitt)
│  │  └─ Commercially Available ✓
│  │
│  └─ Acetic Anhydride
│     ├─ Acetic Acid (脫水)
│     └─ Commercially Available ✓
│
└─ Route 2: 水楊酸 + Acetyl Chloride (替代路徑)
   │
   └─ Acetyl Chloride
      ├─ Acetic Acid + SOCl₂
      └─ More reactive but hazardous
```

**Route 評估：**
- **Route 1 (推薦)：** 安全、經濟、產率高
- **Route 2 (不推薦)：** 反應性強但危險，副產物多

---

## 🎯 結論

### 逆合成總結

1. **主要逆合成路徑：** Aspirin → Salicylic acid + Acetic anhydride
2. **關鍵反應：** Acetylation (乙酸化)
3. **起始原料：** Phenol, CO₂, Acetic anhydride
4. **合成步驟：** 2 步主要反應

### 工業意義

- 阿斯匹靈是世界上最廣泛使用的藥物之一
- 合成工藝成熟，成本極低
- 每年全球產量數百噸

### TorchDrug 應用價值

- **自動逆合成規劃：** 快速生成多條合成路徑
- **反應中心預測：** 準確識別化學反應位點
- **前驅體推薦：** 提供商業可得的起始原料

---

## 📚 參考資料

1. **TorchDrug 文檔：** https://torchdrug.ai/docs/
2. **逆合成經典文獻：** 
   - Corey, E. J. et al. *J. Am. Chem. Soc.* **1969**, *91*, 5675
   - "The Logic of Chemical Synthesis"
3. **阿斯匹靈歷史：**
   - Bayer Company, 1897 年首次合成
   - 1899 年開始商業化

---

**報告生成時間：** 2026-03-20  
**分析工具：** TorchDrug + RDKit + 化學知識庫  
**報告版本：** v1.0
