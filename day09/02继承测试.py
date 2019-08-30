"""
面向对象：
    1.封装
    2.继承
        类与类之间建立关系的一种方式   （课下查资料，类与类之间的关系）
        父类(基类，根类，超类)
        子类(孩子类，派生类)
    语法：
        旧式类(经典类)
        class 类名:
            pass
        新式类：
        class 类名(父类):
            pass

        1.如果一个类，没有明确指明父类是谁，那么默认父类是object，
        2.object是所有类的父类

    特性：
        子类可以继承父类中所有非私有的属性跟方法

    使用继承的必要性：
        1.优化代码结构
        2.易拓展，易维护

"""


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print("睡觉")

    def eat(self):
        print("吃东东")


class Dog(Animal):
    def lookAfterHome(self):
        print("看家护院")


class Cat(Animal):
    def climbTree(self):
        print("上树")


dog = Dog("哈士奇", 2)
dog.eat()
dog.sleep()
dog.lookAfterHome()
dog.name
dog.age

cat = Cat("波斯猫", 2)
cat.sleep()
cat.eat()
cat.climbTree()
