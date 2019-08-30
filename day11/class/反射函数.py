"""
反射函数：

    1.hasattr()
    判断是否包含某个属性
    2.getattr()
    获取某个属性
    3.setattr()
    修改属性值
    4.delattr()
    删除属性

    a = A()
    a.value = 10

反射系统模块中的方法：

方法/类/函数 =  getattr(模块名,'方法名/类名/函数名')
方法()
类()
函数()

"""


class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showInfo(self):
        print(self.name, self.age)


s = Student("张三", 18)
s.name = "学生"
print(s.name)

# 通过反射函数，删除s对象的age属性
# delattr(s,"age")
# print(s.age)

print(s.name, s.age)

# 判断某个对象是否包含某个属性
if hasattr(s, "name"):
    setattr(s, "name", "学生2")
    # 获取对象中的属性
    val = getattr(s, "name")
    print(val)

import time

print(time.time())

# 使用反射调用系统模块中的方法

t = getattr(time, "time")
print(t())

import random

# 通过反射拿到系统模块random中的randint方法
r = getattr(random, "randint")
print(r(1, 9))

import sys

# sys.modules 系统加载到内存中的模块(其中有一个特殊的就是"__main__",表示当前模块),是一个字典
print(list(sys.modules.keys()))
# 使用反射函数拿到当前模块中，Student类
S = getattr(sys.modules['__main__'], "Student")
S2 = getattr(sys.modules[__name__], "Student")
print(S2)
print(S)
stu2 = S("李四", 19)
print(stu2.name, stu2.age)
