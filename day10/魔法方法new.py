"""
TypeError: 'Student' object is not callable
__call__:
    触发场景：
        如果一个对象，被当成函数/方法来调用，__call__方法默认会执行

__new__:
    触发场景:
        创建对象时，自动触发，先与__init__
        new方法中的返回值，固定的
        作用：负责开辟内存

运算符重载：
    对于自定义对象的运算，本质会调用魔法方法：
    比如：__add__
    两个对象求和时，会触发
    __add__(self,rhs)        self + rhs        加法
    __sub__(self,rhs)        self - rhs         减法
    __mul__(self,rhs)        self * rhs         乘法
    __truediv__(self,rhs)   self / rhs          除法
    __floordiv__(self,rhs)  self //rhs          地板除
    __mod__(self,rhs)       self % rhs       取模(求余)
    __pow__(self,rhs)       self **rhs         幂运算

    对象的比较，默认会调用当前类中的比较方法
    >：__gt__()
    >=：__ge__()
    <：__lt__()
    <=：__le__()
"""


class Student():

    def __new__(cls, *args, **kwargs):
        print("__new__")
        return super().__new__(cls)

    def __init__(self, name, age):
        print("__init__")
        self.name = name
        self.age = age

    def __call__(self, *args, **kwargs):
        print("__call__被调用")

    # + 执行时，调用
    def __add__(self, other):
        print("--add--被触发")
        return self.age + other.age

    def __sub__(self, other):
        print("--sub调用--")
        return self.age - other.age

    def __str__(self):
        return f"名字是{self.name},年龄是{self.age}"

    def __gt__(self, other):
        return self.age > other.age


stu1 = Student("张三", 21)
stu2 = Student("张三", 20)
print(stu1 + stu2)
print(stu1 - stu2)
print(stu1 > stu2)

