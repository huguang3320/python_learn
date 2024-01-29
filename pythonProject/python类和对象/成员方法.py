# 定义一个带有成员方法的类
class Student:
    name = None
    # self是默认的属性，访问成员内部变量时需要用self.xxx，但是在调用成员方法时，不需要给这个参数传值
    def say_hello(self,msg):
        print(f"大家好，我是{self.name},{msg}")


# 生成对象，并调用方法
stu = Student()
stu.name = "张三"
stu.say_hello("我给大家表演个唱跳rap")