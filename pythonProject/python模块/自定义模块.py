# 引入自定义模块，如果两个自定义模块定义了相同方法，并同时被引用，则后面引入的方法会覆盖前面引入的方法
# from my_module import my_testA
# my_testA(1,1)


# 验证__all__变量
from my_module2 import *
my_testB(2,1)

