# app/services/notifier.py

import logging
import asyncio
from telegram import Bot
from telegram.error import TelegramError

from app.config.settings import TELEGRAM_TOKEN, CHAT_ID


def send_telegram_message(message: str):
    """
    Envía mensaje a Telegram (compatible con async internamente).
    """

    async def _send():
        bot = Bot(token=TELEGRAM_TOKEN)
        await bot.send_message(chat_id=CHAT_ID, text=message)

    try:
        asyncio.run(_send())
        logging.info("[TELEGRAM] Mensaje enviado correctamente")

    except TelegramError as e:
        logging.error(f"[TELEGRAM ERROR] {e}")


def format_message(item: dict, query: str) -> str:
    """
    Formatea el mensaje de alerta.
    """

    return (
        f"🔥 DEAL DETECTADO\n"
        f"🔎 {query}\n"
        f"📌 {item.get('title')}\n"
        f"💰 {item.get('price')} €\n"
        f"🔗 {item.get('link')}"
    )