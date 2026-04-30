





leads = [
    {"name":"张总","company":"火锅店","budget":50000},
    {"name":"李姐","company":"奶茶店","budget":8000},
    {"name":"王哥","company":"健身房","budget":30000},
    {"name":"赵姐","company":"花店","budget":3000}
]
def analyze(lead):
    if lead["budget"]>10000:
        return "重点用户"
    else:
        return "普通用户"
with open("result.txt","w",encoding="utf-8") as f:
    for lead in leads:
        level = analyze(lead)
        line = f"{lead['name']}{lead['company']}月预算{lead['budget']}元，是{level}"
        print(line)
        f.write(line+"\n")


