"""

方法重写:
    子类重写父类的方法
什么时候重写？
    父类中方法无法满足子类需求的时候，需要进行方法重写


其中一个子类想增加新的属性：
    子类中实现__init__()方法
    在方法添加新属性
    可以super().__init__()调用父类中的init方法

"""


class Animal:
    def __init__(self, name, age):
        super(Animal,self).__init__()
        self.name = name
        self.age = age

    def sleep(self):
        print("睡觉")

    def eat(self):
        print("吃东东")


class Dog(Animal):

    def __init__(self, name, age, breed):
        super(Dog, self).__init__(name, age)
        self.breed = breed

    def lookAfterHome(self):
        print("看家护院")


class Cat(Animal):
    def climbTree(self):
        print("上树")


dog = Dog("秋田", 2, "田园犬")
dog.eat()
dog.sleep()
dog.lookAfterHome()


print(Dog.mro())
# cat = Cat("波斯猫", 2)
# cat.sleep()
# cat.eat()
# cat.climbTree()
