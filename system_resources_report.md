# 系統資源檢查報告

**日期：** 2026-03-21 23:00  
**檢查內容：** GPU、OpenMM、AmberTools

---

## 🎮 GPU 資源

### AMD ROCm GPU 檢測

**狀態：** ✅ 已檢測到 AMD GPU

**工具：** `rocm-smi`

### GPU 詳細信息

| GPU ID | 設備名稱 | 設備 ID | 狀態 |
|--------|----------|---------|------|
| **GPU 0** | AMD Radeon AI PRO R9700 | 0x7551 | ⚠️ 低電力模式 |
| **GPU 1** | AMD Radeon AI PRO R9700 | 0x7551 | ⚠️ 低電力模式 |
| **GPU 2** | AMD Ryzen 7 9700X 8-Core | 0x13c0 | 整合圖形 |

**總計：** 3 個 GPU 設備  
**高階 GPU：** 2 個 AMD Radeon AI PRO R9700

### PyTorch GPU 支援

**PyTorch 版本：** 2.10.0+rocm7.1  
**CUDA 可用：** ✅ True  
**裝置數量：** 3

```python
GPU 0: AMD Radeon AI PRO R9700
GPU 1: AMD Radeon AI PRO R9700
GPU 2: AMD Ryzen 7 9700X 8-Core Processor
```

### ROCm 支援

**ROCm 工具：** ✅ 已安裝 (`/usr/bin/rocm-smi`)  
**ROCm 版本：** 7.1

---

## 🔬 分子動力學工具

### OpenMM

**狀態：** ✅ 已安裝  
**版本：** 8.5  
**安裝路徑：** `/home/c00jsw00/anaconda3/envs/openclaw/bin/python`

**可用模組：**
- ✅ `openmm` - 核心庫
- ✅ `openmm.app` - 應用程式模組
- ✅ `openmm.unit` - 單位模組

**GPU 支援：**
- ✅ ROCm 7.1 (AMD GPU)
- ⚠️ 需要配置 ROCm 環境變數

### AmberTools

**狀態：** ✅ 已安裝  
**版本：** 24.8  
**安裝路徑：** `/home/c00jsw00/anaconda3/envs/openclaw`

**可用工具：**
- ✅ `tleap` - 分子系統準備
- ✅ `MMPBSA.py` - 結合自由能分析

**AmberTools 路徑：**
```
/home/c00jsw00/anaconda3/envs/openclaw/dat/leap/prep
/home/c00jsw00/anaconda3/envs/openclaw/dat/leap/lib
/home/c00jsw00/anaconda3/envs/openclaw/dat/leap/parm
/home/c00jsw00/anaconda3/envs/openclaw/dat/leap/cmd
```

**MMPBSA.py 位置：** `/home/c00jsw00/anaconda3/envs/openclaw/bin/MMPBSA.py`

---

## 🤖 Boltz-2 環境

**環境路徑：** `/home/c00jsw00/anaconda3/envs/boltz2`

**PyTorch 版本：** 2.10.0+rocm7.1  
**ROCm 支援：** ✅ 已啟用

**Boltz-2 GPU 檢測：**
- GPU 0: AMD Radeon AI PRO R9700
- GPU 1: AMD Radeon AI PRO R9700
- GPU 2: AMD Ryzen 7 9700X 8-Core

---

## 📊 系統配置建議

### GPU 使用建議

1. **Boltz-2 預測**
   - 使用 GPU 0 或 GPU 1 (AMD Radeon AI PRO R9700)
   - 記憶體需求：16-24 GB
   - 建議設置：`CUDA_VISIBLE_DEVICES=0`

2. **OpenMM MD 模擬**
   - 使用 GPU 0 或 GPU 1
   - 需要配置 ROCm 平台
   - 建議設置：`CUDA_VISIBLE_DEVICES=0`

3. **MMPBSA 分析**
   - 可使用 CPU 或 GPU
   - GPU 加速可顯著提升速度

### 環境變數設置

```bash
# ROCm 環境變數
export ROCM_HOME=/opt/rocm
export PATH=$ROCM_HOME/bin:$PATH
export LD_LIBRARY_PATH=$ROCM_HOME/lib:$LD_LIBRARY_PATH

# 選擇 GPU
export CUDA_VISIBLE_DEVICES=0

# OpenMM ROCm 平台
export OPENMM_CUDA_COMPILER=hipcc
```

---

## ⚠️ 注意事項

### GPU 低電力模式

**警告：** AMD GPU 處於低電力模式  
**解決方案：**
```bash
# 檢查電源管理狀態
rocm-smi --showpwrcontrol

# 啟用高性能模式（需要 root 權限）
sudo rocm-smi --setpwrstate high
```

### ROCm 配置

**OpenMM ROCm 支援：**
- 需要安裝 `openmm-rocm` 或配置 ROCm 平台
- 可能需要額外安裝 `hipBLAS` 和 `hipFFT`

### AmberTools 配置

**tleap 路徑確認：**
```bash
/home/c00jsw00/anaconda3/envs/openclaw/bin/tleap
```

**MMPBSA.py 路徑確認：**
```bash
/home/c00jsw00/anaconda3/envs/openclaw/bin/MMPBSA.py
```

---

## 🎯 可用工具總結

| 工具 | 狀態 | 版本 | 用途 |
|------|------|------|------|
| **Boltz-2** | ✅ | 2.2.1 | 結構預測 + 親和力 |
| **OpenMM** | ✅ | 8.5 | 分子動力學模擬 |
| **AmberTools** | ✅ | 24.8 | MD 系統準備 |
| **MMPBSA.py** | ✅ | 24.8 | 結合自由能分析 |
| **PyTorch** | ✅ | 2.10.0+rocm7.1 | GPU 加速 |
| **ROCm** | ✅ | 7.1 | AMD GPU 支援 |

---

## 🚀 下一步建議

### 1. 啟用 GPU 高性能模式
```bash
sudo rocm-smi --setpwrstate high
```

### 2. 驗證 OpenMM GPU 支援
```bash
python -c "
import openmm
import openmm.unit as unit
# 測試 GPU 平台
try:
    platform = openmm.Platform.getPlatformByName('CUDA')
    print('CUDA platform available')
except:
    print('CUDA platform not available, trying ROCm')
    try:
        platform = openmm.Platform.getPlatformByName('OpenCL')
        print('OpenCL platform available')
    except:
        print('GPU platform not available')
"
```

### 3. 重新運行完整流程
```bash
cd /home/c00jsw00/.openclaw/workspace/protein_ligand_analysis

# 使用 GPU 運行 Boltz-2
export CUDA_VISIBLE_DEVICES=0
/home/c00jsw00/anaconda3/envs/boltz2/bin/boltz predict \
  input/boltz2_input.yaml \
  --out_dir structures \
  --accelerator gpu \
  --model boltz2 \
  --use_msa_server

# 運行 MD 模擬
# (需要配置 ROCm 平台)

# 運行 MMPBSA 分析
MMPBSA.py -i mmpbsa_input.in -cp complex.prmtop -rp receptor.prmtop -lp ligand.prmtop -y md_traj.nc
```

---

*報告生成時間：2026-03-21 23:00*  
*OpenClaw 系統檢查*
