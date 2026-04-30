import requests

# ---- 配置区 ----
API_KEY = "AIzaSyC3YS8T-JHq_3lqq0Sv0NwvkO3wFftln6c"
MODEL = "gemini-2.5-flash"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

# ---- 给 AI 发一条消息 ----
data = {
    "contents": [
        {
            "parts": [
                {"text": "你好，请用一句话介绍你自己"}
            ]
        }
    ]
}

# ---- 发送请求，拿到回复 ----
try:
    response = requests.post(URL, json=data)
    result = response.json()
    answer = result["candidates"][0]["content"]["parts"][0]["text"]
    print("AI 回复：", answer)
except Exception as e:
    print("出错了：", e)