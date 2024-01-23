"""
replace("代替换数据","要替换数据")
split("")方法，可根据括号内容对字符串进行切分，得到的是切分后的数据组成的list
index()方法，可获取字符串索引值，用法和list.index("xxx")一样
strip()方法，去除字符串前后内容，如果不传参，默认去除字符串前后空格，如果传参，去除字符串两端的参数内容
"""
# 将 he 替换成 ~~
my_str = "hello,test replace"
new_str = my_str.replace("he",'~~')
print(f"new_str:{new_str}")

#以“l”作为分隔条件进行分隔,不会修改原字符串
my_str1 = "hello,test replace"
new_str1 = my_str1.split("l")
print(f"new_str1:{new_str1}")

# 去除空格
my_str2 = "  hello,test replace  "
new_str2 = my_str2.strip()
print(f"new_str2:{new_str2}")

# 去除空格前后的 “1”，“2”
my_str3 = "12hello,test replace2112"
new_str3 = my_str3.strip("12")
print(f"new_str3:{new_str3}")
