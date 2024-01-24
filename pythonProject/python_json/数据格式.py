"""
json格式的转换

"""
import json
# 将列表数据转化成json格式
list_A = [{"name":"zhangsan","age":18},{"name":"lisi","age":22},{"name":"王五","age":23}]
json_str = json.dumps(list_A,ensure_ascii=False)    # ,如果列表数据中包含中文，则 需要添加ensure_ascii=False参数
print(json_str)

# 将字典数据转化成json
dict_A = {"name":"周杰伦","add":"台北"}
json_dict = json.dumps(dict_A,ensure_ascii=False)
print(dict_A)

# 将json转化成列表格式
json_list = '[{"name":"zhangsan","age":18},{"name":"lisi","age":22},{"name":"王五","age":23}]'
list_C = json.loads(json_list)
print(f"lisc_C的数据类型为：{type(list_C)}")
print(list_C)

# 将json转化成字典格式
json_str_dict = '{"name":"周杰伦","add":"台北"}'
list_D = json.loads(json_str_dict)
print(f"lisc_d的数据类型为：{type(list_D)}")
print(list_D)