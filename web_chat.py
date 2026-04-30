import requests
import gradio as gr
from config import API_KEY

URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

def chat(msg, history):
    data = {"contents": [{"parts": [{"text": msg}]}]}
    try:
        response = requests.post(URL, json=data, timeout=30)
        result = response.json()
        return result["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"出错了：{e}"

gr.ChatInterface(fn=chat, title="AI 聊天机器人").launch()