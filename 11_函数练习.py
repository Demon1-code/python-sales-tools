def analyze(lead):
    name = lead["name"]
    budget = lead["budget"]
    if budget > 10000:
        return f"{name},预算{budget}元,值得跟进"
    else:
        return f"{name},预算{budget}元，暂时观望"


leads = [
    {"name":"张总","budget":50000},
    {"name":"李姐","budget":8000},
    {"name":"王哥","budget":30000},
    {"name":"赵姐","budget":5000}
]
for lead in leads:
    result = analyze(lead)
    print(result)