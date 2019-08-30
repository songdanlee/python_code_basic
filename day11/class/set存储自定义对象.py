"""
set存储自定义对象的问题：
set：
    特性：
        无序，唯一,只能存储
    hash(obj) 哈希函数,求某个对象的hash值(只有不可变类型，才可以得到对应的hash值)

    hash函数的本质，会调用该对象所属类中__hash__()方法

set底层数据结构是哈希表：
    如果set存储自定义对象，
    需要重写两个方法：1.__hash__()
                        用来决定对象的hash值，由哪个属性来决定

                      2.__eq__()
                        用来决定自定义对象的比较算法
                        用来指定不同的对象之间用什么来进行比较

"""


class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __hash__(self):
        return hash(self.name) + hash(self.age)

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __str__(self):
        return f"姓名：{self.name},年龄：{self.age}"


stu1 = Student("张三",15)
stu2 = Student("张三",15)
stu3 = Student("张三",15)
stu4 = Student("张三",15)

sets = {stu1,stu2,stu3,stu4}
print(sets)


