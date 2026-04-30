leads= [
    {"name": "张总","company": "火锅店","budget": 50000},
    {"name": "李姐","company": "奶茶店","budget": 8000},
    {"name": "王哥","company": "健身房","budget": 30000},
]
for lead in leads:
    if lead["budget"] > 10000:
        print(f"{lead['name']}{lead['company']}预算{lead['budget']}元，值得跟进！")