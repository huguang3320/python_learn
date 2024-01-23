# 使用 all 变量，可以限定调用者允许调用的方法，方括号里是允许调用的方法
# all变量是作用在 import * 上，如果手动导my_testA方法，则依然可以被调用
__all__ = ['my_testB']
def my_testA(x, y):
    print(x + y)

def my_testB(x, y):
    print(x - y)

