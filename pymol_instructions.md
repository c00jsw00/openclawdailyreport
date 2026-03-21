
# PyMOL 可視化指令

## 15-PGDH 複合體可視化

```python
# 載入結構
load docking_15pgdh_complex.pdbqt, complex
remove solvent
hide everything
show stick, complex
show sphere, complex and not resn NAD
show cartoon, complex and polymer.protein

# 突出顯示配體
select ligand, resn LIG
color orange, ligand
show sphere, ligand
set sphere_scale, 0.3, ligand

# 突出顯示關鍵殘基
select active_site, resn HIS199+SER197+TYR198+THR200+LEU196
color cyan, active_site
show stick, active_site

# 顯示相互作用
dist h_bonds, ligand and not name C+, active_site and name O+N, mode=2
dist salt_bridge, ligand and name O, active_site and name N, mode=2

# 設置視圖
orient complex
zoom ligand, 10
ray 1920,1080
png docking_15pgdh.png, dpi=300
```

## TP Receptor 複合體可視化

```python
# 載入結構
load docking_tpxr_complex.pdbqt, complex
remove solvent
hide everything
show stick, complex
show cartoon, complex and polymer.protein

# 突出顯示跨膜螺旋
show cartoon, complex and chain A
color grey, complex and polymer.protein
color red, complex and (name CA and resi 100-110)  # TM3
color blue, complex and (name CA and resi 190-200)  # TM5
color green, complex and (name CA and resi 290-310)  # TM6-7

# 突出顯示配體
select ligand, resn LIG
color yellow, ligand
show sphere, ligand
set sphere_scale, 0.3, ligand

# 突出顯示關鍵殘基
select key_residues, resn ASP101+SER195+PHE298+TYR305
color magenta, key_residues
show stick, key_residues

# 顯示相互作用
dist h_bonds, ligand and not name C+, key_residues and name O+N, mode=2
dist salt_bridge, ligand and name O, key_residues and name N, mode=2

# 設置視圖
orient complex
zoom ligand, 10
ray 1920,1080
png docking_tpxr.png, dpi=300
```
