# 使用add添加元素
set1 = {"zhangsan", "lisi", "wangwu"}
set1.add("zhaoliu")
print(f"set1的结果是：{set1}")

# 使用remove移除元素
set2 = {"zhangsan", "lisi", "wangwu"}
set2.remove("lisi")
print(f"set2的结果是：{set2}")

# 使用pop 从集合中随机取出一个元素
set3 = {"zhangsan", "lisi", "wangwu", "zhaoliu"}
result = set3.pop()
print(f"set3的结果是：{result}")

# 使用clear 清空集合元素
set4 = {"zhangsan", "lisi", "wangwu", "zhaoliu"}
set4.clear()
print(f"set4的结果是：{set4}")

# 使用difference方法，A集合和B集合，如果A.difference（B）,则可获取到A中没有，B中有的集合，获得的结果不会影响原集合数据
setA = {1, 2, 3}
setB = {1, 5, 6}
set5 = setA.difference(setB)
print(f"set5的结果是：{set5},原集合A是{setA},原集合B是{setB}")

# 使用difference_update方法，A集合和B集合，如果A.difference_update(B)，则去掉A中和B相同的元素
# A集合中有1，B集合中有1，则A会把1去掉
setA = {1, 2, 3}
setB = {1, 5, 6}
setA.difference_update(setB)
print(f"集合A是{setA},集合B是{setB}")

# 使用union方法，A集合和B集合做union，得到一个新的集合，原来的两个集合数据不变
setA = {1, 2, 3}
setB = {1, 5, 6}
set6 = setA.union(setB)
print(f"set6集合为：{set6}，集合A是{setA},集合B是{setB}")

# 使用len方法获取集合长度
setC = {1, 2, 3, 4, 5, 6, 7}
lengths = len(setC)
print(lengths)

# set集合的for循环遍历
setC = {1, 2, 3, 4, 5, 6, 7}
for ele in setC:
    print(f"循环结果{ele}")

