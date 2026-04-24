# DealSniper Pro 💰

Automated marketplace monitoring system that detects underpriced deals in real time and sends instant alerts via Telegram.

---

## 💡 Why This Matters

Manually browsing marketplaces to find good deals is time-consuming and inefficient.

DealSniper Pro automates this process by continuously monitoring listings, filtering irrelevant results, and alerting only when a real opportunity appears.

This allows users to act faster and gain an advantage in competitive marketplaces.

---

## 🚀 Overview

DealSniper Pro is a Python-based automation system designed to monitor online marketplaces and identify valuable opportunities based on price.

Instead of manually browsing listings, the system continuously scans new items, filters irrelevant results, and alerts you only when a potential deal appears.

---

## ⚡ Features

* 🔎 Real-time product monitoring
* 🤖 Anti-bot scraping using Playwright (browser automation)
* 🧠 Smart filtering (removes irrelevant items like accessories)
* 💰 Price-based deal detection
* 🔁 Duplicate prevention system
* 📩 Telegram alert integration
* ⚙️ Modular and scalable architecture

---

## 📸 Example Alert (Telegram)

```
🔥 CHOLLO
🔎 Fender Jazz Bass
📌 Fender Jazz Bass Mexico
💰 450 €
🔗 https://...
```

---

## ⚙️ How It Works

1. Performs automated searches on marketplaces
2. Extracts product data using a headless browser
3. Cleans and structures the data
4. Filters out irrelevant items
5. Detects deals based on price thresholds
6. Sends real-time alerts via Telegram

---

## 🧰 Tech Stack

* Python
* Playwright
* BeautifulSoup
* Requests / HTTPX
* Telegram Bot API
* JSON (data persistence)

---

## 📂 Project Structure

```
deal_sniper/
│
├── app/
│   ├── main.py
│   ├── scraper/
│   ├── parser/
│   ├── services/
│   ├── storage/
│   ├── utils/
│   └── config/
│
├── data/
├── requirements.txt
└── README.md
```

---

## ▶️ Installation

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuration

Create a `.env` file in the root directory:

```
TELEGRAM_TOKEN=your_token_here
CHAT_ID=your_chat_id_here
```

---

## ▶️ Run

```bash
python -m app.main
```

---

## 🎯 Use Cases

* 💰 Detect underpriced products for reselling
* ⚡ Monitor marketplaces without manual effort
* 📊 Track new listings in real time
* 🤖 Automate repetitive search workflows
* 🛠️ Build custom monitoring tools for clients

---

## 🚀 Future Improvements

* Multi-marketplace support
* Async scraping
* Price history tracking
* Advanced deal scoring system
* Deployment on VPS / Docker

---

## 📌 Notes

This project is designed as a practical automation system and can be adapted to different industries and use cases.

---

## 👤 Author

Developed as a real-world automation project focused on marketplace monitoring and opportunity detection.
