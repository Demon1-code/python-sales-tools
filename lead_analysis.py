import requests

# ---- 配置区 ----
from config import API_KEY
MODEL = "gemini-2.5-flash"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

# ---- 模拟 3 条销售线索 ----
leads = [
    {"name": "王妈妈", "child_age": 15, "score": 65, "concern": "数学很差，中考怕考不上高中"},
    {"name": "李爸爸", "child_age": 10, "score": 90, "concern": "成绩还行但想冲名校"},
    {"name": "张妈妈", "child_age": 8, "score": 75, "concern": "孩子注意力不集中，坐不住"},
]

# ---- 逐条分析 ----
for lead in leads:
    prompt = f"""你是一个教育培训行业的销售顾问。请分析以下家长线索，给出：
1. 购买意愿评分（1-10分）
2. 推荐课程类型
3. 沟通话术建议（一句话）

家长信息：
- 姓名：{lead['name']}
- 孩子年龄：{lead['child_age']}岁
- 当前成绩：{lead['score']}分
- 主要顾虑：{lead['concern']}
"""

    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    try:
        response = requests.post(URL, json=data)
        result = response.json()
        answer = result["candidates"][0]["content"]["parts"][0]["text"]
        print(f"\n{'='*40}")
        print(f"【{lead['name']}】的分析结果：")
        print(answer)
    except Exception as e:
        print(f"分析 {lead['name']} 时出错：{e}")

print("\n全部分析完成！")