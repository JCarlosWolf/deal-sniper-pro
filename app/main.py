# app/main.py

import time
import logging

from app.config.settings import SEARCHES, INTERVAL
from app.scraper.wallapop import fetch_wallapop_results
from app.parser.parser import parse_wallapop
from app.services.deal_filter import filter_deals
from app.services.notifier import send_telegram_message, format_message
from app.storage.storage import is_new_item, save_item


# ==============================
# 🔧 CONFIGURACIÓN LOGGING
# ==============================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


def run():
    """
    Loop principal del sistema
    """

    logging.info("🚀 DealSniper Pro iniciado")

    while True:
        try:
            for search in SEARCHES:
                query = search["query"]
                max_price = search["max_price"]

                logging.info(f"[SEARCH] {query}")

                # 1. SCRAPING
                html = fetch_wallapop_results(query)

                # 2. PARSER
                items = parse_wallapop(html)

                # 3. FILTRADO
                deals = filter_deals(items, query, max_price)

                logging.info(f"[RESULTS] {len(deals)} deals encontrados")

                # 4. PROCESAMIENTO
                for item in deals:
                    item_id = item["id"]

                    if is_new_item(query, item_id):
                        message = format_message(item, query)

                        send_telegram_message(message)
                        save_item(query, item_id)

                        logging.info(f"[DEAL] Enviado → {item['title']}")

                    else:
                        logging.info(f"[SKIP] Duplicado → {item['title']}")

            logging.info(f"[SLEEP] Esperando {INTERVAL}s...\n")
            time.sleep(INTERVAL)

        except Exception as e:
            logging.error(f"[FATAL ERROR] {e}")
            time.sleep(10)


if __name__ == "__main__":
    run()