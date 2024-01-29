"""
演示构造方法
"""

class Student:
    name = None
    age = None
    gender = None
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender