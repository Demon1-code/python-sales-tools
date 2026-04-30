import gradio as gr
from gtts import gTTS
import os

def read_english(text):
    tts = gTTS(text=text, lang="en")
    tts.save("output.mp3")
    return "output.mp3"

with gr.Blocks(title="英语朗读工具") as app:
    gr.Markdown("# 英语朗读工具")
    gr.Markdown("输入英文单词、短语或句子，点击朗读")

    text_input = gr.Textbox(label="输入英文", placeholder="例如：The economy is growing rapidly")
    audio_output = gr.Audio(label="朗读结果")
    btn = gr.Button("朗读")

    btn.click(fn=read_english, inputs=text_input, outputs=audio_output)

app.launch()
