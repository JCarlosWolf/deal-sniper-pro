# app/config/settings.py

"""
Configuración central del sistema DealSniper Pro
"""

import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env (si existe)
load_dotenv()

# ==============================
# 🔎 BÚSQUEDAS ACTIVAS
# ==============================

SEARCHES = [
    {
        "query": "Fender Jazz Bass",
        "max_price": 600
    }
]

# ==============================
# 📣 TELEGRAM CONFIG
# ==============================

TELEGRAM_TOKEN = "8657336891:AAFWm3-DpM53AdUaVUvYtJVJFnC3ol5KpQc"
CHAT_ID = "1293778019"

# ==============================
# ⏱ INTERVALO DE EJECUCIÓN
# ==============================

# Tiempo en segundos entre cada ciclo
INTERVAL = int(os.getenv("INTERVAL", 60))

