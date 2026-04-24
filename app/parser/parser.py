# app/parser/parser.py

from typing import List, Dict
from app.utils.id_generator import generate_id


def parse_wallapop(items: List[Dict]) -> List[Dict]:
    results = []

    for item in items:
        try:
            title = item.get("title", "")
            price = float(item.get("price", 0))

            web_slug = item.get("web_slug", "")
            link = f"https://es.wallapop.com/item/{web_slug}" if web_slug else ""

            item_id = generate_id(link)

            results.append({
                "title": title,
                "price": price,
                "link": link,
                "id": item_id
            })

        except:
            continue

    return results