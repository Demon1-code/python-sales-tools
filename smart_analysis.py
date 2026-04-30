import pandas as pd
import requests
from config import API_KEY

# ---- 配置区 ----
MODEL = "gemini-2.5-flash"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

# ---- 1. 读取数据 ----
df = pd.read_excel("学员线索.xlsx")
print(f"共 {len(df)} 条线索\n")

# ---- 2. 用 pandas 筛选高意向客户 ----
hot = df[(df["咨询次数"] >= 3) & (df["是否付费"] == "否")]
print(f"筛选出 {len(hot)} 条高意向客户（咨询≥3次 + 未付费）\n")

# ---- 3. 对高意向客户逐个调 AI 分析 ----
with open("高意向客户分析.txt", "w", encoding="utf-8") as f:
    f.write("===== 高意向客户 AI 分析报告 =====\n\n")

    for _, row in hot.iterrows():
        prompt = f"""你是教育培训行业的资深销售顾问。请针对这位家长，给出：
1. 成交可能性评估（高/中/低）
2. 最可能的成交障碍
3. 推荐的跟进策略（具体到第一句话怎么说）

家长信息：
- 姓名：{row['姓名']}
- 孩子年龄：{row['孩子年龄']}岁
- 咨询科目：{row['科目']}
- 当前成绩：{row['当前成绩']}分
- 已咨询次数：{row['咨询次数']}次
- 尚未付费
"""

        data = {
            "contents": [{"parts": [{"text": prompt}]}]
        }

        try:
            response = requests.post(URL, json=data)
            result = response.json()
            answer = result["candidates"][0]["content"]["parts"][0]["text"]
            print(f"✅ {row['姓名']} 分析完成")
            f.write(f"【{row['姓名']}】\n")
            f.write(f"咨询{row['咨询次数']}次 | {row['科目']} | 成绩{row['当前成绩']}分\n\n")
            f.write(f"{answer}\n")
            f.write(f"\n{'='*40}\n\n")
        except Exception as e:
            print(f"❌ {row['姓名']} 分析失败：{e}")

    f.write("===== 报告结束 =====\n")

print("\n完成！结果已保存到：高意向客户分析.txt")