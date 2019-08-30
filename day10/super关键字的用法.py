"""
super的用法：
    可以调用父类中的方法

# super(B, self).__init__(a)可以在类外使用

"""
class A:
    def __init__(self,a):
        self.a = a
    def test1(self):
        print("A.test")
class B(A):
    def __init__(self,a,b):
        super(B, self).__init__(a)
        self.b = b
    def test1(self):
        print("B.tets")

b = B(1,2)
print(b.__dict__)
#可以在类外直接调用父类的方法
super(B,b).test1()
# 这种写法只能在类内使用
# super().test1()



