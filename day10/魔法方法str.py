"""

魔法方法：
    1.系统定义的__方法__()
    2.特点是，在一定场景下系统自动触发
__init__()
    创建对象时，系统自动调用
__str__
__repr__
两个方法都会在打印对象时，默认调用，优先调用__str__,如果没有，则执行__repr__,如果都没有，找父类

__del__
    删除方法，
    在一个对象，被系统回收时，会触发


"""
import copy


class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"名字是{self.name},年龄是{self.age}"

    def __repr__(self):
        return f"我叫{self.name},我{self.age}岁了"

    def __del__(self):
        print(f"{self.name}被删除了")


s = Student("张三", 13)
print(s)
s2 = copy.deepcopy(s)
print(id(s2))
print(id(s))
del s
