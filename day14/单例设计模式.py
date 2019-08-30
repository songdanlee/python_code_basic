"""
__new__ 保证内存唯一
__init__ 保证初始化唯一
函数的默认值传参，只会在内存中创建一份
"""


class Sington:
    __has = None
    __firstInit = True

    def __new__(cls, *args, **kwargs):
        if cls.__has is None:
            cls.__has = super(Sington, cls).__new__(cls, *args, **kwargs)
        return cls.__has

    def __init__(self, cart=[]):
        self.cart = cart

    # def __init__(self):
    #     #     if self.__firstInit:
    #     #         Sington.cart = []
    #     #         Sington.__firstInit = False


c1 = Sington()
c2 = Sington()
c1.cart.append("acb")
c1.cart.append("efg")
c2.cart.append("efg")

print(hex(id(c1)))
print(hex(id(c2)))
print(c1.cart)
print(c2.cart)

# class Singleton:
#     __instance = None
#
#     def __init__(self):
#         pass
#
#     @classmethod
#     def getInstance(cls):
#         if cls.__instance is None:
#             cls.__instance = Singleton()
#         return cls.__instance
