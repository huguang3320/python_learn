"""
文件读取中的read方法是带有指针属性的，读取后指针会跟着改变
"""
import time

# 文件打开的方法，第一个参数为文件路径，第二个参数为模式，此处为读模式，第三个参数为打开文件编码
f = open("F:/123.txt","r",encoding="utf-8")
# 读取指定字节数据
# print(f.read(10))
# 读取文件中全部数据，返回值类型为字符串
# print(f.read())
# 读取所有行数据，返回值类型为list列表类型
# line = f.readlines()
# print(f"读取后的数据类型：{type(line)},读取数据：{line}")
 # 读取单行数据（一次读取一行）
# print(f.readline())
# print(f.readline())
# print(f.readline())

# 使用for循环获取每行数据
# for line in f:
#     print(line)

# 关闭文件
# f.close()

# 自带关闭的打开文件方法
with open("F:/123.txt","r",encoding="utf-8") as f:
    for line in f:
        print(line)