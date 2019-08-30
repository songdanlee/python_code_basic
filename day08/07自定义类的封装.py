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

#1.给单个对象添加属性
#2.在模板中直接添加属性
    __init__方法中添加相关属性

    __init__方法触发时机
        在创建一个对象时，系统自动调用


"""
class Hero():
    def __init__(self,name_,damage_,hp_):
        self.name = name_
        self.hp=hp_
        self.damage = damage_
    def move(self):
        print('英雄移动中...')

    def attack(self):
        print('英雄发出攻击')
# 创建一个对象
h1 = Hero("吕布",100,3000)
print(id(h1))
print(h1.__dict__)
print(dir(h1))#对象存属性
print(dir(Hero))#类中不存属性

h2 = Hero('貂蝉',2000,180)
print(id(h2))
print(h2.__dict__)

