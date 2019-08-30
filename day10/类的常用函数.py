class Foo():
    pass


class Bar(Foo):
    pass


print(issubclass(Bar, Foo))
foo = Foo()
print(isinstance(foo,Foo))


print(hasattr(foo,"name"))

class Teacher():
    dict = {'查看学生的信息':'show_student','查看讲师信息':'show_teacher'}
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @classmethod
    def func(cls):
        print("hahha")

attr = getattr(Teacher,"dict")
print(attr)

func = getattr(Teacher,"func")
setattr(Foo,"name","食物")
print(Foo.name)
