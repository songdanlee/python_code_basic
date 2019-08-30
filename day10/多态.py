"""
多态：方法的多态
方法的多态
调用的同样的名字的方法，但是实现的形式可能是多样的

多态的条件
    1.继承
    2.方法重写
python的多态不同于java多态，不能再一个类里面定义同名方法(不同参数，返回值)
"""


class Person:
    def eat(self):
        print("人都要吃饭")


class Chinese(Person):
    def eat(self):
        print("中国人用筷子吃饭")


class English(Person):
    def eat(self):
        print("英国人用刀叉吃饭")


class Indian(Person):
    def eat(self):
        print("印度人用手吃饭")


person = Chinese()

person.eat()

person = English()
person.eat()
