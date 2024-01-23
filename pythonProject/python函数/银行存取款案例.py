money = 5000000
name = "张三"

def query():
    print(f"{name},您的剩余存款为：{money}")

# 存款
def save(num):
    global money
    money += num
    print("----------------存款---------------")
    print(f"存款金额为：{num}")
    query()

# 取款
def get(num):
    global money
    money -= num
    print("----------------取款---------------")
    print(f"取款金额为：{num}")
    query()

def main():
    print("----------------主菜单---------------")
    print("查询余额\t[输入1]")
    print("存款\t[输入2]")
    print("取款\t[输入3]")
    print("退出\t[输入4]")
    return input("请输入您的选择：")

while(True):
    keybord_input = main()
    if keybord_input == "1":
        query()
        continue
    elif keybord_input == "2":
        num = int(input("请输入您要存入的金额"))
        save(num)
        continue
    elif keybord_input == "3":
        num = int(input("请输入您要取出的金额"))
        get(num)
        continue
    else:
        print("您已退出系统")
        break







