# for i in range(1,16):
#     print("语句1")
#     # 将本次循环结束，跳到下一次循环当中，并且只针对所属的当前的内层循环
#     continue
#     print("语句2")

# 演示continue
# for i in range(1,6):
#     print("语句1")
#     for j in range(1,6):
#         print("语句2")
#         continue
#         print("语句3")
#     print("语句4")

# 演示break
for i in range(1,6):
    print("语句1")
    for j in range(1,6):
        print("语句2")
        break
        print("语句3")
print("语句4")