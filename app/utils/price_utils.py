# app/utils/price_utils.py

import re


def clean_price(price_text: str) -> float:
    """
    Limpia un string de precio y lo convierte a float.

    Ejemplos:
    "600 €" -> 600.0
    "1.200€" -> 1200.0
    "450,99 €" -> 450.99
    """

    if not price_text:
        return 0.0

    # Eliminar espacios
    price_text = price_text.strip()

    # Reemplazar coma por punto (formato europeo)
    price_text = price_text.replace(",", ".")

    # Eliminar cualquier carácter que no sea número o punto
    price_text = re.sub(r"[^\d.]", "", price_text)

    try:
        return float(price_text)
    except ValueError:
        return 0.0