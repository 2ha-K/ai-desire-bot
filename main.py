# main.py
from src.ai_desire_bot.chat import chat_with_model
from src.ai_desire_bot.character_loader import load_character_card

if __name__ == "__main__":
    name, personality, greeting = load_character_card("characters/sakura.json")
    print(f"[角色：{name}] {greeting}")

    while True:
        user_input = input("你說：")
        full_prompt = f"{personality}\n使用者說：{user_input}\n{name}："
        print(full_prompt)
        reply = chat_with_model(full_prompt)
        print(f"{name}：{reply}")
