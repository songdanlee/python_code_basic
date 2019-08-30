# 1.创建函数，可以完成一个视频的复制(注意视频读写使用的mode为rb,wb)，新视频的名字为视频名_副本.后缀，
# 如果被复制的视频文件>10M 则抛出自定义异常(目标文件太大),提示(os.path.getsize(file)可以获取文件大小)
import os


class File2LargeException(Exception):
    def __init__(self):
        self.errMsg = "文件太大"

    def __str__(self):
        return f"{self.__class__},{self.errMsg}"


def copyVideo(videoName):
    try:
        if os.path.getsize(videoName) / 1024 / 1024 > 100:
            raise File2LargeException()
        f1 = open(videoName, "rb")
        tu = videoName.rpartition(".")
        new_file_name = tu[0] + "_副本" + tu[1] + tu[2]
        print(new_file_name)
        f2 = open(new_file_name, "wb")
        content = f1.read(1024 * 1024)
        while content:
            f2.write(content)
            content = f1.read(1024 * 1024)
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        try:
            f2.close()
            f1.close()
        except Exception as e:
            print(e)
        else:
            print("文件关闭")


# copyVideo(f"E:\怪奇物语\回顾.wmv")

# 2.创建学生类，设置私有属性_age, 提供对应的set，get方法，set方法中如果给的数据不合理，抛出
# 自定义异常 AgeError

class AgeError(Exception):
    def __init__(self):
        self.errMsg = "年龄不合法"

    def __str__(self):
        return f"{self.__class__},{self.errMsg}"


class Student:
    def __init__(self, name,age):
        self.name = name
        self.setAge(age)

    def getAge(self):
        return self.__age

    def setAge(self, age):
        if isinstance(age, int) and 1 <= age <= 120:
            self.__age = age
        else:
            raise AgeError

    def __str__(self):
        return self.__age


s = Student("zs",10)
# s.setAge(10)
print(s.getAge())
# s.setAge("ab")

# 3.基于购物车的业务逻辑，实现一个单例模式的购物车类

class Cart():
    __instace = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instace:
            cls.__instace = super(Cart, cls).__new__(cls)
        return cls.__instace

    def __init__(self, cart=[]):
        self.__cart = cart

    def add_elem(self,elem):
        self.__cart.append(elem)

    def rm_elem(self,elem):
        self.__cart.remove(elem)

    def __str__(self):
        return f"{self.__cart}"

#
# c1 = Cart()
# c1.add_elem("123")
# c1.add_elem(123)
# c1.add_elem("abc")
# c1.rm_elem(123)
# c2 = Cart()
# print(c2)
