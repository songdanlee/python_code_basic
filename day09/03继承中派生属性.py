"""
继承：
    子类可以继承父类非私有的属性，方法(无法访问属性以及私有方法)

派生属性(属性重写)
    子类中如果存在与父类中的同名属性，以子类为准

"""
class A:
    def __init__(self):
        self.__a = 10

    def __test(self):
        print("test测试")


class B(A):
    def test(self):
        super().___test()#错误



b = B()
b.test()
# print(b.__a)
# b.__test()
print(b.__dict__)
print(b._A__a)