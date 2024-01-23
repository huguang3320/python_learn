# str1 = "abcd"
# str2 = "abcde"
# str3 = "111222333"


# def my_len(data):
#     count = 0
#     for i in data:
#         count += 1
#     print(f"字符串{data}的长度是：{count}")
#
#
# my_len(str1)
# my_len(str2)
# my_len(str3)

# def add(x,y):
#     result =  x+y
#     print(f"x+y的值是 {result}")
#
# add(1,5)

# def add(a,b):
#     return a+b
#
# r = add(1,5)
# print(r)


# def check_age(age):
#     if age >= 18:
#         return "SUCCESS"
#     else:
#         return None
#
# result = check_age(19)
# if not result:
#     print("不可进入~")
# else:
#     print(f"输出：{result}")


number = 200

# 修改方法里的变量值无法影响全局变量值
def method1():
    print(f"输出数据number：{number}")


def method2():
    #如果定义了 global 那就将局部变量改为全局变量了
    global number
    number = 500
    print(f"输出数据number：{number}")


method1()
method2()

print(number)
