"""
super的用法：
    可以调用父类中的方法

# super(B, self).__init__(a)可以在类外使用

"""

class A:
    def test1(self):
        print("A.test")


class B(A):
    def test1(self):
        print("B.tets")

        super().test1()

class C(A):
    def test1(self):
        print("C.test")

        super(C, self).test1()

class D(B, C):
    def test1(self):
        print("D.test")
        super(D, self).test1()


d = D()
d.test1()
print(D.mro())
super(D,d).test1()


# mro  D  B  C  A顺序
# super(D,d).test1() 根据mro顺序调用D的后面的类的test1 即B
# super(B, d).test1()根据mro顺序调用B的后面的类的test1 即C
# super(C, d).test1()根据mro顺序调用C的后面的类的test1 即A