student = {
    "name": "Echo",
    "age": 25,
    "city": "重庆",
    "rank": "master",

}
print(student)
print(type(student))
print(student["name"])
print(student["age"])
print(student["city"])
student["age"] = 26
print(f"改了年龄:{student['age']}")
student["game"] = "街霸6"
print(f"加了游戏:{student['game']}")
del student["rank"]
print(student)
print(len(student))

student2 = {
    "name" : "echo",
    "address": {
        "city": "重庆",
        "district": "渝北区"
    }
}
print(student2["name"])
print(student2["address"])
print(student2["address"]["city"])