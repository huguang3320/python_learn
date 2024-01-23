#基础模拟
# age = 10
# print(f"我已经{age}岁了")
# if age >= 18:
#     print("我成功进入到循环了")
# print("我在循环外面")

#练习题
# ages = input("请输入你的年龄：")
# age = int(ages)
# if age >= 18:
#     print("您已成年，需要补票10元")
# elif 10 <= age < 18:
#     print("祝您玩得愉快")
# else:
#     print("赶紧回家吧")

# 练习题

ture_age = 18
if int(input("输入猜想数字：")) == ture_age:
    print("恭喜第一次就猜对了")
elif int(input("猜错了，再猜一次：")) == ture_age:
    input("猜对了！")
elif int(input("猜错了，再猜一次：")) == ture_age:
    print(f"终于猜对了！:{ture_age}")


