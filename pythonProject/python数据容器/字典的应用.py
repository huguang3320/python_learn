my_dict = {'a': 1, 'b': 2, 'c': 3}
# 在字典中添加、修改元素
my_dict['d'] = 5

# 在字典中删除元素
my_dict.pop('c')
# print(my_dict)

# 清空字典
#my_dict.clear()

# 获取字典全部的key值
keys = my_dict.keys()
print(f"字典中全部的key：{keys}")
for key in keys:
    print(my_dict[key])