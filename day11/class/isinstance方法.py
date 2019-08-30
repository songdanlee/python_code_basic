"""
isinstance(obj,cls):
判断对象obj是否为cls的实例，或者是cls的子类的实例

需求：
    判断一个变量是否为int类型

issubclass(cls1,cls2):
判断cls1是否为cls2的子类

"""

class A:
    def testA(self):
        print("testA")

class B(A):
    def testB(self):
        print("testB")

class C(B):
    pass
a = A()
print(isinstance(a,A))
print(isinstance(a,B))
b = B()
print(isinstance(b,A))
print(isinstance(b,B))

print(issubclass(C,A))
print(issubclass(C,B))
print(issubclass(C,C))


a = eval(input("请输入数值"))
if isinstance(a,int):
    print("int")
elif isinstance(b,float):
    print("float")
else:
    print("其他")