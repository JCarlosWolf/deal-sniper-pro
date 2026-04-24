# app/utils/id_generator.py

import hashlib


def generate_id(url: str) -> str:
    """
    Genera un ID único basado en la URL del producto.
    Se usa para evitar duplicados.
    """

    if not url:
        return ""

    return hashlib.md5(url.encode("utf-8")).hexdigest()