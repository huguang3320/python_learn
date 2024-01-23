#  list.index -- 获取元素索引值
list_a = ['zhangsan',666,'aaa']
print(list_a.index(666))

# 修改指定索引位置的值
list_a[1] = 'lisi'
print(list_a)

#插入
list_a.insert(1,'wangwu')
print(list_a)

#追加，将元素添加到列表的尾部
list_a.append(888)
print(list_a)

#删除方式一 根据索引删除
del list_a[2]
print(list_a)

#删除方式二，删除后还能获取到删除的元素
test_list = ['a','b']
str = test_list.pop(1)  # 根据索引删除
print(f"集合元素{test_list},删除的元素是{str}")

#根据内容进行删除，从前到后搜索，找到的第一个进行删除
my_list = ['a','b','c','b','a']
my_list.remove('b')
print(my_list)

#清空列表
my_list.clear()

#统计某元素在列表中的数量
my_list_b = ['a','b','c','b','e']
count = my_list_b.count('b')
print(f"元素个数为{count}")

# 统计列表元素个数
my_list_b = ['a','b','c','b','e']
len = len(my_list_b)
print(f"列表元素个数为{len}")



