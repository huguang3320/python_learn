# i = 1
# while i < 10:
#     print("测试while循环")
#     i+=1

#计算1加到100的和
"""
num = 1
sum_num = 0
while num <= 100:
    sum_num += num
    num+= 1
print(sum_num)
"""
# 猜测数字
import random
num = random.randint(1,100)
# 记录猜测次数
guess_count = 1
guess_num = int(input("请输入一个数字："))
while True:
    guess_count += 1
    if num == guess_num:
        print(f"恭喜您猜对了")
        break
    if guess_num > num:
        guess_num = int(input("您猜大了，请重新输入:"))
    else:
        guess_num = int(input("您猜小了，请重新输入:"))
print(f"猜测次数：{guess_count}")