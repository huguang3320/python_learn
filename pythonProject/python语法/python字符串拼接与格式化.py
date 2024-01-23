name = "张三"
message = "嘿嘿嘿，我是%s" % name
print(message)

# 多个占位符  数字如果使用%s占位符，会自动转化为字符串
student_name = "张三"
class_num = 51
avg_salary = 12405.123
message = "字符串占位符:%s,数字占位符:%d,浮点型占位符:%f" % (student_name,class_num, avg_salary)
print(message)

#精度控制
num1 = 11
num2 = 11.345
print("数字11宽度限制5，结果是:%5d" % num1)
# 整数部分设定的宽度如果比实际数字的位数要小，则限制不了 如下：
print("数字11宽度限制1，结果是：%1d" % num1)
print("数字11.345，宽度限制7，小数精度2，结果是：%7.2f" % num2)
print("数字11.345，宽度无限制，小数精度2，结果是：%.2f" % num2)

# 快速模式
name = "李四"
age = 14
weight = 18.88
print(f"我的名字是{name},年龄是{age},体重是{weight}")

# 表达式的格式化
print(f"计算 {6*2}")