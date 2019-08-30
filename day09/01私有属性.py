"""
面向对象本质只做两件事:
1.设计好对应的类（封装）
2.处理类与类之间的相互关系（业务，需求）



面向对象：
1.封装
    类的封装：
        属性：
            __init__(self)
        方法：

        私有属性：
            什么是私有属性？
                双下划开头的属性，被称为私有属性
            有哪些特性？
                只能在类的内部访问，不对外开放(无法在类外访问)
            为什么要用私有属性？
                控制属性的访问权限
            如果使用私有属性需要注意的事项？
                应该对外提供私有属性的访问方式：
                    1.提供获取私有属性值的方法(读)
                    2.提供设置私有属性值的方法(写)
            私有化的本质？
                python不是真正意义上的私有化，本质是进行名字重整(被改名)
                改名的规则：
                    _类名__属性名

        私有方法：


2.继承
    类与类之间关系的一种
3.多态
    方法的多态
"""


class Student():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        # 私有属性
        self.__gender = gender

    # 提供私有属性的访问接口
    def getGender(self):
        return self.__gender
    # 提供私有属性的修改接口
    def setGender(self,gender):
        if gender in ['男','女']:
            self.__gender = gender
        else:
            print("性别有误")
    def introduce(self):
        print(f"我叫{self.name},{self.age}岁,性别{self.__gender}")
        self.__test()
    def __test(self):
        print("测试方法")


stu = Student("张三",13,"男")
stu.introduce()

print(stu.name)
print(stu.age)

stu.setGender("女")
print(stu.getGender())
print(dir(stu))
print(stu.__dict__)
#可以通过访问重整后的属性/方法名，进行修改和访问，不推荐

stu._Student__gender = "半男不男"
print(stu._Student__gender)
stu._Student__test()