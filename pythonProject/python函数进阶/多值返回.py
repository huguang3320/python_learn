def re_met():
    return 1, 2, 3


x, y, z = re_met()
print(f"{x}\t{y}\t{z}")


# 使用键=值的形式传参
def user_name(name, age, gender):
    print(f"您的名字是{name},年龄是{age},性别是{gender}")

user_name(name="张三", age=20, gender="女")

# 缺省参数(可以定义一个参数的默认值，如果某个参数不传值，则该参数会自动使用默认值)
# 默认值必须放在最后，(name, age, gender="男")没问题，但是(name, age=18, gender)
def user_name(name, age, gender="男"):
    print(f"您的名字是{name},年龄是{age},性别是{gender}")

user_name("李斯",20)

#位置不定长参数，类型是元组类
def user_name(*rgs):
    print(f"不定长参数的类型{type(rgs)},值是：{rgs}")

user_name(1,2,3,'aaa','张三')

# 关键字不定长参数，得到的类型是字典类型
def user_name(**kwrgs):
    print(f"不定长参数的类型{type(kwrgs)},值是：{kwrgs}")

user_name(id1=1,id2=2,id3=3,name1='aaa',name2='张三')

#函数的传递
# 1.定义主函数内容
def test_func(compute):
     result = compute(1,2)
     print(f"函数类型：{type(compute)}")
     print(f"返回结果值：{result}")

#2.定义被调用函数内容
def compute(x,y):
      return x+y

#3、调用主函数
test_func(compute)


# 使用lamda匿名函数形式，将匿名函数作为参数传入
test_func(lambda x,y: x+y)
