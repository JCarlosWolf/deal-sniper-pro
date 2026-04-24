# app/storage/storage.py

import json
import os
from typing import Dict, List


DATA_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    "data",
    "seen_items.json"
)


def _ensure_file_exists():
    """
    Crea el archivo JSON si no existe
    """
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)

    if not os.path.exists(DATA_PATH):
        with open(DATA_PATH, "w", encoding="utf-8") as f:
            json.dump({}, f)


def load_data() -> Dict[str, List[str]]:
    """
    Carga el JSON completo
    """
    _ensure_file_exists()

    try:
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}


def save_data(data: Dict[str, List[str]]):
    """
    Guarda el JSON completo
    """
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def is_new_item(query: str, item_id: str) -> bool:
    """
    Verifica si el item ya fue visto
    """
    data = load_data()

    if query not in data:
        data[query] = []

    return item_id not in data[query]


def save_item(query: str, item_id: str):
    """
    Guarda un item como visto
    """
    data = load_data()

    if query not in data:
        data[query] = []

    if item_id not in data[query]:
        data[query].append(item_id)
        save_data(data)