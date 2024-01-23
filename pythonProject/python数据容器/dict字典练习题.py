my_dict = {
    "zhangsan": {
        "part": "科技部",
        "salary": 3000,
        "level": 1
    },
    "lisi": {
        "part": "市场部",
        "salary": 5000,
        "level": 2
    },
    "wangwu": {
        "part": "市场部",
        "salary": 7000,
        "level": 3
    },
    "zhaoliu": {
        "part": "科技部",
        "salary": 4000,
        "level": 1
    },
    "sunqi": {
        "part": "市场部",
        "salary": 6000,
        "level": 2
    },
}
print(f"原来的薪水：{my_dict}")
for key in my_dict:
    my_level = my_dict[key]["level"]
    if my_level == 1:
        my_dict[key]["salary"] += 1000

print(f"现在的薪水：{my_dict}")



