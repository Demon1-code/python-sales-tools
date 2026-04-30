import pandas as pd

df = pd.read_excel("学员线索.xlsx")

# ---- 1. 排序 ----
print("===== 按成绩从低到高排序 =====")
sorted_df = df.sort_values("当前成绩")
print(sorted_df[["姓名", "当前成绩"]])

# ---- 2. 分组统计 ----
print("\n===== 按科目统计平均分 =====")
group = df.groupby("科目")["当前成绩"].mean().round(3)
print(group)

# ---- 3. 添加新列 ----
print("\n===== 添加优先级列 =====")
df["优先级"] = df["当前成绩"].apply(lambda x: "高" if x < 70 else "低")
print(df[["姓名", "当前成绩", "优先级"]])