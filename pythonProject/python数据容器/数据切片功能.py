# 对 list 进行切片，从1开始，4结束，步长为1
my_list = [0,1,2,3,4,5]
result1 = my_list[1:4]
print(f"结果1：{result1}")

# 对tuple进行切片，从头开始，到最后结束，步长为1
my_tuple = (1,2,3,4,5,6,7)
result2 = my_tuple[:]
print(f"结果2：{result2}")
# 对str进行切片，从头开始，到最后结束，步长2
my_str = "01234567"
result3 = my_str[::2]
print(f"结果3：{result3}")
#对str进行切片，从头开始，到最后结束，步长为-1
my_str2 = "01234567"
result4 = my_str2[::-1]
print(f"结果4：{result4}")
#对列表进行切片，从3开始，到1结束，步长 -1
my_list2 = [0,1,2,3,4,5]
result5 = my_list2[3:1:-1]
print(f"结果5：{result5}")
# 对元组进行切片，从头开始，到尾结束，步长-2
my_tuple2 = (1,2,3,4,5,6,7)
result6 = my_tuple2[::-2]
print(f"结果6：{result6}")

# 练习题，从一段倒叙的话中取出关键字，并给正序   -- 从这段话中取出关键字三个字
test_str = "序正给并，字键关出取中话的叙倒段一从"
result7 = test_str[::-1][10:13]
print(f"练习题结果为：{result7}")
result8 = test_str[::-1]