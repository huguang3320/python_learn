# 追加list
my_list = [21,25,21,23,22,20]
my_list.append(31)
print(my_list)

#追加新list
add_list = [29,33,30]
my_list.extend(add_list)
print(my_list)
# 取出第一个元素
num = my_list[0]
print(num)

# 取出最后一个元素
last_num = my_list[-1]
print(last_num)

# 找出元素31
index = my_list.index(31)
print(index)