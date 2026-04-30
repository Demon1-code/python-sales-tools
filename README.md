# Python Sales Tools | Python 销售自动化工具集

AI-powered sales automation tools built with Python — lead analysis, Excel data processing, chatbot, and more.

基于 Python 的 AI 销售自动化工具集，包含线索分析、Excel 数据处理、聊天机器人等。

---

## Features | 功能

- **Lead Analysis** — Call AI API (Google Gemini) to analyze sales leads from CSV, generate reports automatically | 调用 AI API 分析销售线索，自动生成分析报告
- **Excel Data Processing** — Filter, sort, group and analyze Excel data with pandas | 使用 pandas 对 Excel 数据进行筛选、排序、分组统计
- **Scheduled Automation** — Run analysis tasks on a timer, auto-generate reports | 定时执行分析任务，自动生成报告
- **AI Chatbot** — Command-line and web-based chatbot (Gradio UI) | 命令行 + 网页版 AI 聊天机器人
- **English Reader** — Text-to-speech tool for English learning (gTTS + Gradio) | 英语朗读工具

## Project Files | 项目文件

| File | Description |
|------|-------------|
| `call_ai.py` | Minimal AI API call |
| `lead_analysis.py` | Batch lead analysis |
| `lead_analysis_v2.py` | Analysis with file output |
| `lead_analysis_v3.py` | Analysis from CSV input |
| `excel_analysis.py` | pandas data analysis |
| `pandas_essentials.py` | Sort, group, add columns |
| `smart_analysis.py` | pandas + AI combined |
| `auto_report.py` | Scheduled automation |
| `sales_tool.py` | Complete sales tool |
| `chatbot.py` | Command-line chatbot |
| `web_chat.py` | Web chatbot (Gradio) |
| `english_reader.py` | English text-to-speech |

## Tech Stack | 技术栈

Python 3 · requests · pandas · schedule · Gradio · gTTS · Google Gemini API

## Setup | 使用方法

1. Clone this repo | 克隆仓库
```bash
git clone https://github.com/Demon1-code/python-sales-tools.git
```

2. Install dependencies | 安装依赖
```bash
pip install requests pandas openpyxl schedule gradio gtts
```

3. Create `config.py` with your API key | 创建 config.py 并填入你的 API Key
```python
API_KEY = "your-gemini-api-key-here"
```

4. Run any script | 运行任意脚本
```bash
python sales_tool.py
```

## Author | 作者

**Demon1-code** — Sales professional transitioning into AI & automation | 从销售转型 AI 自动化的实践者
