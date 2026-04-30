import requests
from config import API_KEY

URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

print("=== AI 聊天机器人 ===")
print("输入问题开始聊天，输入 退出 结束\n")

while True:
    msg = input("你：")
    if msg == "退出":
        print("再见！")
        break

    data = {"contents": [{"parts": [{"text": msg}]}]}

    try:
        response = requests.post(URL, json=data, timeout=30)
        result = response.json()
        answer = result["candidates"][0]["content"]["parts"][0]["text"]
        print(f"AI：{answer}\n")
    except Exception as e:
        print(f"出错了：{e}\n")