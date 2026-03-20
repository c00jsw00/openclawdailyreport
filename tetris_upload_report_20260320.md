# 俄羅斯方塊遊戲上傳報告

**報告日期：** 2026-03-20  
**上傳者：** 品丸

---

## 🎮 遊戲介紹

一個用 Python + Pygame 編寫的完整俄羅斯方塊遊戲，支持 Windows 系統。

### 主要功能
- ✅ 7 種標準方塊形狀 (I, O, T, S, Z, J, L)
- ✅ 方塊下落、旋轉、移動
- ✅ 行消除機制
- ✅ 分數統計系統
- ✅ 遊戲結束判斷
- ✅ 暫停/繼續功能
- ✅ 速度隨分數增加
- ✅ 下一個方塊預覽
- ✅ 中文介面

---

## 📂 上傳檔案

### GitHub 倉庫
🔗 **https://github.com/c00jsw00/tetris-game**

### 包含檔案
```
tetris-game/
├── tetris_game.py       # 主程式碼 (Python)
├── README_tetris.md     # 詳細使用說明
├── requirements.txt     # 依賴套件清單
└── .gitignore          # Git 忽略檔案
```

---

## 🚀 使用方法

### 1. 下載遊戲

**方式一：直接下載**
```bash
git clone https://github.com/c00jsw00/tetris-game.git
```

**方式二：下載單一檔案**
訪問 GitHub 倉庫，下載 `tetris_game.py` 檔案

### 2. 安裝依賴

```bash
pip install pygame
```

### 3. 運行遊戲

```bash
python tetris_game.py
```

---

## 🎯 操作說明

| 按鍵 | 功能 |
|------|------|
| ← → | 左右移動方塊 |
| ↑ | 旋轉方塊 |
| ↓ | 加速下落 |
| Space | 立即下落 (硬降落) |
| P | 暫停/繼續遊戲 |
| R | 重新開始遊戲 |
| ESC | 退出遊戲 |

---

## 📊 分數規則

| 消除行數 | 分數 |
|----------|------|
| 1 行 | 100 × 等級 |
| 2 行 | 300 × 等級 |
| 3 行 | 500 × 等級 |
| 4 行 | 800 × 等級 |

---

## 💻 系統要求

- **作業系統：** Windows 10/11
- **Python：** 3.6 或更高版本
- **依賴套件：** pygame >= 2.0.0

---

## 🎨 技術特點

### 程式碼結構
```python
class Piece:           # 方塊類
class TetrisGame:      # 遊戲主類
    def __init__(self) # 初始化
    def run(self)      # 主遊戲循環
    def draw()         # 繪製遊戲
    def update()       # 更新遊戲狀態
```

### 特色功能
- 雙緩衝渲染，避免閃爍
- 動態難度調整
- 下一方塊預覽
- 暫停/繼續功能
- 完整的錯誤處理

---

## 📝 版本資訊

- **版本：** 1.0
- **作者：** 品丸
- **日期：** 2026-03-20
- **語言：** Python 3
- **引擎：** Pygame
- **License：** MIT (個人使用)

---

## 🔗 相關連結

- **GitHub 倉庫：** https://github.com/c00jsw00/tetris-game
- **Pygame 官網：** https://www.pygame.org/
- **Python 官網：** https://www.python.org/

---

## 💡 未來擴展計劃

- [ ] 加入音效
- [ ] 多人模式
- [ ] 更多關卡設計
- [ ] 移動端支援
- [ ] 排行榜系統

---

*報告生成時間：2026-03-20*
