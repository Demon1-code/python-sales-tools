colleagues = ["张三","李四","王五","赵六","钱七",]
print(colleagues)
print(type(colleagues))
print(colleagues[0])
print(colleagues[1])
print(colleagues[4])
print(colleagues[-1])
print(colleagues[-2])
colleagues[0] = "赵总"
print(colleagues)
colleagues.append("孙八")
print(colleagues)
colleagues.remove("李四")
print(colleagues)
print(len(colleagues))
for name in colleagues:
    print(f"你好，{name}")

