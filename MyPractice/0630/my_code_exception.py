# try:
#     x = int(input("enter the first number"))
#     y = int(input("enter the second number"))
#     print(x / y)
# except ZeroDivisionError:
#     print("The second number can't be zero!")


# while True:
#     try:
#         x = int(input('enter the first number:'))
#         y = int(input("enter the second number"))
#         value = x / y
#         print('{0} / {1} is {2}'.format(x,y,value))
#     except Exception as e:
#         print("Invalid input: {}".format(e))
#         print("please try again")
#     else:
#         break

# try:
#     x = 1 / 0
# except Exception:
#     print("Unknown variable")
# else:
#     print("That went well")
# finally:
#     print("cleaning up...")
#


# class Rectangle:
#     def __init__(self):
#         self.width = 0
#         self.height = 0
#     def set_size(self, size):
#         self.width, self.height = size
#     def get_size(self):
#         print("get size")
#         return self.width, self.height
#     # 在获取size时
#     size = property(get_size, set_size,"i am size")
#
#
# r = Rectangle()
# r.width = 10
# r.height = 5
# # 在获取size时，或调用get_size()方法
# print(r.size)
# # 在设置size时，或调用set_size()方法
# r.size = 150,100
# print(r.width)

class MyClass:

    @staticmethod
    def smeth():
        print("我是静态方法")

    @classmethod
    def cmeth(cls):
        print("我是类方法")

# MyClass.smeth()
# MyClass.cmeth()
nested = 123
try:
    nested + ''
except TypeError:
    print("sssss")



