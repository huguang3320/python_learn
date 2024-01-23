"""
元组的概念和list差不多，但是元组数据不可修改，只用index、count、len方法
元组中的数据类型也可以是多种
元组内如果包含list，则可以修改list内的数据
元组中如果只有一个数据，那么需要在数据后写一个逗号
元组的关键字是turple
元组也支持for、while循环，使用方式和list相同
"""

yuanzu1 = (1,2,3)
print(f"yuanzu2数据:{yuanzu1},数据类型:{type(yuanzu1)}")

yuanzu2 = tuple()
print(f"yuanzu2数据:{yuanzu2},数据类型:{type(yuanzu2)}")

yuanzu3 = ("aaa",111,True)
print(f"yuanzu3数据:{yuanzu3},数据类型:{type(yuanzu3)}")

yuanzu4 = ('a','b','c','b','a')
print(f"元素a的位置是：{yuanzu4.index('a')},元组长度为：{len(yuanzu4)},yuanzu4的a元素个数为：{yuanzu4.count('a')}")

yuanzu5 = ('a','b','c',['d','e','f'])
yuanzu5[3][0] = 'a'
print(f"元组5：{yuanzu5}")

yuanzu6 = ('a','b','c')
index = 0
while index < len(yuanzu6):
    print(yuanzu6[index])
    index += 1

yuanzu7 = ('a','b','c','d')
for ele in yuanzu7:
    print(ele)
