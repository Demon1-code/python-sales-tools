price = input("请输入商品价格：")
count = input("请输入购买数量：")
total = int(price)*int(count)
print(f"总价是{total}元")
#列表循环条件
scores = [45,78,92,33,88,61,55,100]
a = 0
b = 0
for score in scores:
    if score >= 60 :
        a+=1
    else:
        b+=1
print(a)
print(b)
#字典取值

order = {
    "customer": "张总",
    "product": "ai分析系统",
    "price": 15000,
    "paid": True
}

if order["paid"]== True:
    status = "已付款"
else:
    status = "未付款"



print(f"{order['customer']} 购买了{order['product']}，价格 {order['price']}元{status}")
#函数
def calc_discount(price):
    if price > 10000:
        return price*0.8
    elif price >5000:
        return price*0.9
    else:
        return price

print(calc_discount(15000))
print(calc_discount(3000))
#文件写入
with open("names.txt","w",encoding="utf-8") as f:
    f.write("echo""\n")
    f.write("张总""\n")
    f.write("李姐""\n")
    f.write("王哥""\n")
