import json
from app.config import settings


def load_tasks_from_file() -> list[dict]:
    try:
        with open(settings.TASKS_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []


def save_tasks_to_file(tasks_list: list[dict]):
    with open(settings.TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks_list, file, ensure_ascii=False, indent=2)
