with open("text.txt","w",encoding="utf-8")as f:
    f.write("你好，我是echo\n")
    f.write("这是我用Python写的第一个文件\n")
    f.write("今天学会了文件读写！\n")
print("文件写入成功")

with open("text.txt","r",encoding="utf-8")as f:
    content = f.read()
print(content)

try:
    with open("不存在的文件.txt","r",encoding="utf-8")as f:
        content = f.read()
    print(content)
except FileNotFoundError:
    print("文件不存在，请检查文件名")
