# 使用import 引入模块，可以使用模块的所有方法
#import time
#print("你好")
#time.sleep(3)
#print("你也好，等了3秒")

# 使用from 导入time 模块的 sleep方法
from time import sleep
print(1)
sleep(3)
print(4)

# 使用from 导入 time 模块的所有方法
from time import *


# 使用 as 给特定模块加上别名
import time as t

