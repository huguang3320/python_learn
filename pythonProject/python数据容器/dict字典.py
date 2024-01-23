my_dict = {'a': 1, 'b': 2, 'c': 3}
print(f"字典为：{my_dict}")
print(my_dict.get('a'))
print(my_dict['a'])

# 字典的嵌套

stu_score_dict = {
    "zhangsan": {
        "sx": 10,
        "yw": 20,
        "yy": 30
    },
    "lisi": {
        "sx": 11,
        "yw": 21,
        "yy": 31
    },
    "wangwu": {
        "sx": 12,
        "yw": 22,
        "yy": 32
    }
}
#获取wangwu的yw信息
print(stu_score_dict["wangwu"]["yw"])