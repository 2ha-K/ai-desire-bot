# src/ai_desire_bot/character_loader.py
import json

def load_character_card(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["name"], data["personality"], data.get("greeting", "")
