# scripts/test_chat.py
from src.ai_desire_bot.chat import chat_with_model

if __name__ == "__main__":
    print("🔹 測試與模型對話功能")
    test_prompt = "你是誰？"
    result = chat_with_model("/bye")
    print("🧠 AI 回覆：")
    print(result)

