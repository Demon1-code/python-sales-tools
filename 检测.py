#1
a = "2000"
b = 3500
c = b+int(a)
print(c)

#字典与列表
students = [
    {"name": "小明", "score": 85, "status": "未跟进"},
    {"name": "小红", "score": 92, "status": "跟进中"},
    {"name": "小刚", "score": 78, "status": "未跟进"}
]
for student in students:
    if student["score"] > 80 and student["status"] == "未跟进":
        print(f"{student['name']}是高价值用户，请立即联系")

#函数模块化思维


def sed_notif(name,reason):
    if name =="王总" and reason == "合同到期":
        return f"【提醒】亲爱的{name},您的项目由于{reason},需要处理"
    elif name =="李老师" and reason == "课程排满":
        return f"【提醒】亲爱的{name},您由于{reason},需要处理"



