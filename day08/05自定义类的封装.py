"""
封装一个英雄类
类名的定义：使用大驼峰
创建类的语法：
语法：
创建方式1
class 类名:
    pass
创建方式2
class 类名():
    pass

在Python3中两种方式没有区别

对象的创建：
    变量名 = 类名()

方法的调用：
    对象名.方法名()

"""
class Hero:
    hp = 300
    def move(self):
        print("对象移动..........")
    def attack(self):
        print("对象攻击")
h1 = Hero()
h1.attack()
h1.move()
print(h1.hp)

print(h1.__getattribute__("hp"))


class Human():

    def __init__(self,name,age):
        self.name  = name
        self.age = age
    def __str__(self):
        return f"名字是{self.name},年龄是{self.age}"
    def talk(self):
        print("你好呀")

hu = Human("张三",13)
print(hu)
hu.talk()

# d = {'a': 1, 'b': 2}
# def func(**kwargs):
#     print(kwargs)
#
# func(**d)
