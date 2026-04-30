goods = [
    {"product":"键盘","price":299,"remain":50},
    {"product":"鼠标","price":99,"remain":0},
    {"product":"显示器","price":1999,"remain":10}
]
def check_stock(good):
    if good["remain"]>0:
        return "有货"
    else:
        return"缺货"

for good in goods:
    print(f"{good['product']}价格{good['price']}元，库存{good['remain']}个,{check_stock(good)}")

