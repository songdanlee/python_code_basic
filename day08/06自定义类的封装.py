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

"""


class Hero:
    def move(self):
        print('英雄移动中...')

    def attack(self):
        print('英雄发出攻击')


# 创建一个对象
h1 = Hero()
# 打印h1的地址
print(id(h1))
# 给对象h1添加属性
h1.name = "吕布"
# 首次操作，添加属性
h1.hp = 5000
# 非首次操作执行修改值
h1.hp = 10000
h1.damage = 100
#打印h1的所有属性
print(h1.__dict__)

h2 = Hero()
h2.name = '干将莫邪'
h2.hp = 3000
h2.damage = 150
h2.move()
h2.attack()
print(h2.__dict__)