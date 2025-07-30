import requests

#Shell code: ollama run HammerAI/mythomax-l2
def chat_with_model(prompt: str, model: str = "HammerAI/mythomax-l2") -> str:
    """
    與本地 Ollama 模型對話（使用 Chat API 格式）

    Args:
        prompt (str): 使用者輸入
        model (str): 模型名稱，例如 "mythomax"

    Returns:
        str: 模型回應內容
    """
    try:
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": model,
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "stream": False
            },
            timeout=60
        )
        response.raise_for_status()
        data = response.json()
        return data.get("message", {}).get("content", "[WARNING] 無回應內容")
    except requests.exceptions.RequestException as e:
        return f"[ERROR] 無法連線模型 API：{e}"
