# import time
# from functools import wraps
#
#
# def timer(func):
#     @wraps(func)
#     def innner(*args, **kwargs):
#         start_time = time.time()
#         time.sleep(0.01)
#         func(*args, **kwargs)
#         end_time = time.time()
#         print(end_time - start_time)
#
#     return innner
#
#
# # fun = timer(func)
# # fun()
#
# @timer
# def func1(*args, **kwargs):
#     print("我爱。。。。你好世界，hello world")
#
#
# func1('aa', 'bb')
# print(func1.__dict__)
# print(func1.__name__)
#
#
# # 装饰器1
# def wrapper1(func):
#     def inner1():
#         print("wrapper1,before func")
#         func()
#         print("wrapper1,after func")
#
#     return inner1
#
#
# def wrapper2(func):
#     def inner2():
#         print("wrapper2,before func")
#         func()
#         print("wrapper2,after func")
#
#     return inner2
#
#
# @wrapper1
# @wrapper2
# def f():
#     print("in f")
#
#
# f()

# property 修饰私有方法的getter setter方法，
class Person():

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    # 控制属性的访问属性，没有设置@name.setter装饰器
    # 因此无法设置name属性的值
    @property
    def name(self):
        return self.__name

    # @name.setter
    # def name(self, name):
    #     self.__name = name

    @property
    def age(self):
        return self.__age
    # age.setter 是property装饰后的副产品，用来修饰setter方法
    @age.setter
    def age(self, age):
        if 1 <= age <= 120:
            self.__age = age
        else:
            print("从火星来的吧")
            return


person = Person("zs", 13)
print(person.name)
person.age = 14
print(person.age)

from math import pi

class Circle():
    def __init__(self,r):
        self.r = r

    @property
    def zhouchang(self):
        return 2*pi*self.r
    @property
    def area(self):
        return pi*self.r**2

c = Circle(2)
print(c.zhouchang)
print(c.area)