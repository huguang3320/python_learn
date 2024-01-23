# 使用print直接输出
print(type("你好你好"))
print(type(666))
print(type(13.14))

# 使用变量存储type返回得结果
string_type = type("你好你好~")
int_type = type(666)
float_type = type(11.123)
print(string_type)
print(int_type)
print(float_type)

# 使用type语句，查看变量中存储得数据类型信息
name = "你好你好你好"
name_type = type(name)
print(name_type)