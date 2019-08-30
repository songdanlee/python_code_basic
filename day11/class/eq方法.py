"""
自定义对象的比较问题：
is:
    比较两个对象是否为同一个对象
==: 对于一个对象而言，调用==，本质要到对象所属的类中查找，__eq__()方法
    比较两个对象的值是否相等
    对于自定义类，如果涉及到两个对象是否相等的操作，一般情况下，需要重写__eq__（）方法

"""

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __gt__(self, other):
        return self.age > other.age

stu1 = Student("张三",18)
stu2 = Student("张三",18)

print(stu1 is stu2)

print(stu1 == stu2)