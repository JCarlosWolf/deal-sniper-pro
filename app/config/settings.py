import os
from dotenv import load_dotenv

# ==============================
# 🔐 LOAD ENV VARIABLES
# ==============================
load_dotenv()

# ==============================
# 🔎 SEARCH CONFIG
# ==============================
SEARCHES = [
    {
        "query": "Fender Jazz Bass",
        "max_price": 600,
        "target_price": 500
    }
]

# ==============================
# 📣 TELEGRAM CONFIG
# ==============================
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "YOUR_TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID", "YOUR_CHAT_ID")

# ==============================
# ⏱️ SYSTEM CONFIG
# ==============================
INTERVAL = 60  # segundos entre búsquedas