# 🍒 ai_desire_bot

一款以 MythoMax-L2 為核心、可本地部署的色情角色扮演 AI 聊天機器人，支援使用者自訂角色卡、持續對話記憶、語音輸入與輸出。專為打造虛擬動漫伴侶與情境互動體驗而設計。

---

## ✨ 特色功能

- 💬 **角色扮演聊天**：支援自訂語氣、背景、興趣等角色設定（支援 SillyTavern 格式 JSON）
- 🧠 **持續記憶**：可選擇開啟記憶模組，讓 AI 記住你們之間的過去互動
- 🔧 **可自行訓練／微調**：支援 LoRA 微調，強化角色個性一致性
- 🗣️ **語音輸入／TTS 輸出**：可接收語音並回應語音（選配）
- 🧩 **模組化架構**：乾淨可維護的程式結構，便於擴充

---

## 📦 安裝方式

1. 安裝 Python 依賴

```bash
pip install -r requirements.txt
````

2. 下載並啟用模型（使用 Ollama）

```bash
ollama run mythomax
```

3. 執行主程式（CLI 測試）

```bash
python main.py
```

4. 或使用 SillyTavern 前端連接模型，取得視覺化 UI 體驗

---

## 🗂 專案結構

```
ai_desire_bot/
├── characters/           # 角色卡 JSON 設定
├── logs/                 # 聊天紀錄與錯誤 log
├── scripts/              # 測試、自動化腳本
├── src/ai_desire_bot/    # 核心程式碼
├── audio/                # 語音檔案儲存（可選）
├── tests/                # 單元測試模組
├── main.py               # 程式入口
├── config.yaml           # 模型與角色設定
├── requirements.txt      # 所需套件
├── .gitignore
└── README.md
```

---

## 💡 使用說明

* 編輯 `config.yaml` 指定預設角色與模型名稱
* 將角色卡放入 `characters/` 資料夾中
* 執行 `main.py` 啟動對話流程（CLI 測試），或串接 SillyTavern 作為前端 UI

---

## 📌 備註

* 本專案僅供學術研究與個人用途，請勿用於違反當地法規之行為。
* 模型內容包含成人語料，使用請審慎評估風險。

---

## 🛠️ TODO

* [ ] 整合 Web UI（Gradio / Streamlit）
* [ ] 自訂記憶系統與情緒管理
* [ ] 聲音轉文本與回話音色變換（voice cloning）


