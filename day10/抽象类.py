"""
抽象类：
抽象类不能创建对象
1.什么抽象类？
    抽象类也是一个类，区别在于包含抽象方法的类，才是抽象类
2.抽象方法
    本质就是一个方法，必须用@abstractmethod装饰
3.如何创建一个抽象类
    1.需要引入 (AbcMeta,abstractmethod)
    2.手动指定元类
    3.创建抽象方法
4.抽象类的作用
    一定以上可以约束子类的行为，要求子类重写父类中抽象方法，如果子类不重写父类中的抽象方法，
    则子类依旧是抽象类
"""
from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):

    def __init__(self, color):
        self.color = color

    @abstractmethod
    def shout(self):
        pass


class Dog(Animal):
    def shout(self):
        print("汪汪汪")


dog = Dog("white")

import abc


class BasePizza(object):
    __metaclass__ = abc.ABCMeta

    ingredient = ['cheese']

    @classmethod
    @abc.abstractmethod
    def get_ingredients(cls):
        """Returns the ingredient list."""
        return cls.ingredients


class Pizza(BasePizza):
    def get_ingredients(cls):
        """Returns the ingredient list."""
        return super(Pizza, cls).get_ingredients()


p = Pizza()
Pizza.get_ingredients()
