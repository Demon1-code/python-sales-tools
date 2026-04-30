def greet(name):
    print(f"你好{name}!欢迎咨询，我是echo，很高兴为您服务！")
greet("张总")
greet("李姐")
greet("王哥")

def analyze_lead(name,budget):
    if budget > 10000:
        return f"{name},预算{budget}元，值得跟进"
    else:
        return f"{name},预算{budget}元，暂时观望"
result1 = analyze_lead("张总",50000)
result2 = analyze_lead("李姐",8000)
print(result1)
print(result2)

