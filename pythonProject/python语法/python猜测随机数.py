import random
num = random.randint(1,10)
guess_num = int(input('输入一个您猜测的数字：'))
if guess_num == num:
    print("恭喜您一次就猜对了")
else:
    if guess_num < num:
        print("您猜小了")
    else:
        print("您猜大了")
    guess_num = int(input('请再输入一个您猜测的数字：'))
    if guess_num == num:
        print("恭喜您猜对了")
    else:
        if guess_num < num:
            print("您猜小了")
        else:
            print("您猜大了")
        guess_num = int(input('请再输入一个您猜测的数字：'))
    if guess_num == num:
        print("恭喜您第三次猜对了")
    else:
        print("三次机会都用完了，没有猜中")