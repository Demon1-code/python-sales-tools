a= [
    {"name": "街霸6","type": "格斗","time": 500},
    {"name": "apex","type": "射击","time": 200},
    {"name": "圆神","type": "RPG","time": 50}
]
for i in a :
    if i["time"]>100:
        print(f"{i['name']}是{i['type']}类型游戏，我玩了{i['time']}小时")