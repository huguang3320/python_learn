if int(input("您的身高是多少？：")) > 120:
    print("身高超出限制，不可免费")
    print("如果您是vip会员，级别大于3，则无需购票")
    if int(input("您的vip级别是多少？：")) > 3:
        print("恭喜您，可以通过")
    else:
        print("您好，需要补票价10元")
else:
    print("欢迎您进入游玩")
