from typing import List, Dict


# ❌ PALABRAS A BLOQUEAR (basura)
EXCLUDE_KEYWORDS = [
    "pastilla",
    "pastillas",
    "golpeador",
    "batipenna",
    "mástil",
    "mastil",
    "pickup",
    "cover",
    "cejuela",
    "clavijas",
    "cuerdas",
    "puente"
]


def filter_deals(items: List[Dict], query: str, max_price: float) -> List[Dict]:
    """
    Filtra productos:
    - Matching flexible por palabras
    - Precio máximo
    - Excluye accesorios (muy importante)
    """

    deals = []

    query_words = query.lower().split()

    for item in items:
        try:
            title = item.get("title", "").lower()
            price = item.get("price", 0)

            # 🔥 FILTRO 1 — excluir basura
            if any(word in title for word in EXCLUDE_KEYWORDS):
                continue

            # 🔥 FILTRO 2 — matching flexible
            matches = sum(1 for word in query_words if word in title)

            if matches < 2:
                continue

            # 🔥 FILTRO 3 — precio
            if price <= max_price:
                deals.append(item)

        except Exception:
            continue

    return deals