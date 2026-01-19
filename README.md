# Chemical Bottle Scanner - Ultimate Edition 🧪📦

這是一個基於 **Python** 與 **OpenCV** 開發的實驗室藥品盤點系統。
透過 Webcam 掃描藥罐上的 **CAS Number**，自動比對庫存清單，並在盤點結束後自動產生缺漏報告。

---

## ✨ 核心功能 (Key Features)

* 🎥 **即時掃描 (Live Scanning)**
    透過鏡頭讀取藥罐標籤，支援模糊比對。
* ⏳ **視覺暫留 (Smart Freeze)**
    掃描成功後，綠色結果框會鎖定螢幕 **3 秒**，方便您確認資訊，不用怕手晃。
* 📝 **歷史清單 (History Sidebar)**
    螢幕右側面板會顯示**最近掃描的 8 筆紀錄**，防止漏看。
* 📂 **GUI 檔案選擇**
    程式啟動時彈出視窗選擇 CSV，無需修改程式碼即可切換不同藥冊。
* 🌏 **中文支援**
    完美支援中文 CSV 標題（如：`上層藥品名稱`、`廠牌`）與 UTF-8 編碼。
* 📊 **自動報告**
    盤點結束時，自動匯出 `missing_report.csv` 缺漏清單。

---

## 🛠️ 安裝需求 (Requirements)

在使用本系統前，請確保您的電腦已安裝以下軟體：

### 1. Python 3.x
請確保已安裝 Python 環境。

### 2. Tesseract OCR (關鍵!) 👁️
這是文字辨識引擎，**必須額外安裝**，否則程式無法運作。
* **下載位址**: [Tesseract-OCR Windows Installer](https://github.com/UB-Mannheim/tesseract/wiki)
* **安裝路徑**: 預設建議安裝於 `C:\Program Files\Tesseract-OCR`
* **設定**: 請確認 Python 程式碼中的 `TESSERACT_PATH` 指向您的 `tesseract.exe`。

### 3. Python 套件
請打開終端機 (Terminal / CMD)，執行以下指令安裝所需套件：

```bash
pip install opencv-python pytesseract pandas numpy thefuzz python-Levenshtein