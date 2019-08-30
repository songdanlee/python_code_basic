"""
类方法与成员方法：
    1.默认参数不同
        cls
    2.所有者不同
        类
    3.调用方式不同
        类名.类方法名()
        对象名.类方法名()

静态方法：
 必须使用@staticmethod装饰
    定义在类内的一个函数
    调用方式：与类方法的调用方式一致
"""

class A:
    def testa(self):
        print("成员方法")
    @classmethod
    def test2(cls):
        print("类方法")
    @staticmethod
    def test3():
        print("静态方法")

a = A()
a.testa()
a.test2()
a.test3()

A.test2()
A.test3()
