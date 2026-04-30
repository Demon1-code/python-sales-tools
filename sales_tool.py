import requests
import pandas as pd
from config import API_KEY
from datetime import datetime

# ---- 配置区 ----
MODEL = "gemini-2.5-flash"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"
INPUT_FILE = "学员线索.xlsx"


def analyze_one(row):
    """分析单条线索，返回 AI 回复。失败返回 None"""
    prompt = f"""你是教育培训行业的资深销售顾问。请简洁分析这位家长，给出：
1. 购买意愿（高/中/低）
2. 推荐课程
3. 跟进话术（一句话）

家长：{row['姓名']}，孩子{row['孩子年龄']}岁，{row['科目']}，成绩{row['当前成绩']}分，已咨询{row['咨询次数']}次"""

    data = {"contents": [{"parts": [{"text": prompt}]}]}

    try:
        response = requests.post(URL, json=data, timeout=30)
        result = response.json()
        return result["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        print(f"  ⚠️ API 调用失败：{e}")
        return None


def run_report():
    """主流程：读取 → 统计 → 筛选 → AI分析 → 生成报告"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{'='*50}")
    print(f"  销售线索智能分析工具")
    print(f"  运行时间：{now}")
    print(f"{'='*50}\n")

    # ---- 1. 读取数据 ----
    try:
        df = pd.read_excel(INPUT_FILE)
    except FileNotFoundError:
        print(f"❌ 找不到文件：{INPUT_FILE}")
        print(f"   请把 Excel 文件放到和代码同一个文件夹下")
        return
    except Exception as e:
        print(f"❌ 读取文件失败：{e}")
        return

    print(f"📊 读取到 {len(df)} 条线索\n")

    # ---- 2. 数据概览 ----
    print("--- 数据概览 ---")
    print(f"  平均成绩：{df['当前成绩'].mean().round(1)} 分")
    print(f"  已付费：{len(df[df['是否付费'] == '是'])} 人")
    print(f"  未付费：{len(df[df['是否付费'] == '否'])} 人")

    # ---- 3. 筛选高意向客户 ----
    hot = df[(df["咨询次数"] >= 2) & (df["是否付费"] == "否")]
    print(f"\n🔥 高意向客户（咨询≥2次 + 未付费）：{len(hot)} 人\n")

    if len(hot) == 0:
        print("没有符合条件的高意向客户")
        return

    # ---- 4. AI 逐条分析 ----
    filename = f"分析报告_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    success = 0
    fail = 0

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"===== 销售线索智能分析报告 =====\n")
        f.write(f"生成时间：{now}\n")
        f.write(f"数据来源：{INPUT_FILE}\n")
        f.write(f"总线索数：{len(df)} | 高意向：{len(hot)}\n\n")

        for _, row in hot.iterrows():
            answer = analyze_one(row)

            if answer:
                success += 1
                print(f"  ✅ {row['姓名']}")
                f.write(f"【{row['姓名']}】\n")
                f.write(f"  {row['科目']} | 成绩{row['当前成绩']}分 | 咨询{row['咨询次数']}次\n\n")
                f.write(f"{answer}\n")
                f.write(f"\n{'='*40}\n\n")
            else:
                fail += 1
                print(f"  ❌ {row['姓名']}（已跳过）")
                f.write(f"【{row['姓名']}】分析失败，已跳过\n\n")

        f.write(f"===== 报告结束 =====\n")
        f.write(f"成功：{success} | 失败：{fail}\n")

    # ---- 5. 运行总结 ----
    print(f"\n--- 运行总结 ---")
    print(f"  ✅ 成功：{success} 条")
    if fail > 0:
        print(f"  ❌ 失败：{fail} 条")
    print(f"  📄 报告已保存：{filename}")


# ---- 启动 ----
run_report()