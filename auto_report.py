import requests
import pandas as pd
from config import API_KEY
from datetime import datetime

# ---- 配置区 ----
MODEL = "gemini-2.5-flash"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"


def analyze_one(row):
    """分析单条线索，返回 AI 的回复文字"""
    prompt = f"""你是教育培训行业的资深销售顾问。请简洁分析这位家长，给出：
1. 购买意愿（高/中/低）
2. 推荐课程
3. 跟进话术（一句话）

家长：{row['姓名']}，孩子{row['孩子年龄']}岁，{row['科目']}，成绩{row['当前成绩']}分，已咨询{row['咨询次数']}次"""

    data = {"contents": [{"parts": [{"text": prompt}]}]}
    response = requests.post(URL, json=data)
    result = response.json()
    return result["candidates"][0]["content"]["parts"][0]["text"]


def run_report():
    """主函数：读取数据 → 筛选 → AI分析 → 生成报告"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n[{now}] 开始生成报告...")

    # 读取数据
    df = pd.read_excel("学员线索.xlsx")
    hot = df[(df["咨询次数"] >= 2) & (df["是否付费"] == "否")]
    print(f"共 {len(df)} 条线索，筛出 {len(hot)} 条高意向")

    # 生成带时间戳的文件名
    filename = f"报告_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"===== 自动分析报告 =====\n")
        f.write(f"生成时间：{now}\n\n")

        for _, row in hot.iterrows():
            try:
                answer = analyze_one(row)
                print(f"  ✅ {row['姓名']}")
                f.write(f"【{row['姓名']}】{row['科目']} | 成绩{row['当前成绩']}分\n")
                f.write(f"{answer}\n")
                f.write(f"{'='*40}\n\n")
            except Exception as e:
                print(f"  ❌ {row['姓名']}：{e}")

    print(f"报告已保存：{filename}")


# ---- 先手动跑一次测试 ----
import schedule
import time

# 每隔 30 秒跑一次（测试用，确认能用后再改成每天定时）
schedule.every(30).seconds.do(run_report)

print("定时任务已启动，每 30 秒运行一次（按 Ctrl+C 停止）")

while True:
    schedule.run_pending()
    time.sleep(1)
