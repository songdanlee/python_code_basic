class Person:

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def greet(self):
        print("Hello ,World,I'am {}".format(self.name)        )
foo = Person()
bar = Person()
bar.set_name('Anakin Skywalker')
foo.set_name('luke skywalker')
foo.greet()
bar.greet()


class Secretive:
    #__ 私有属性或方法，不能从外部访问
    def __inaccessible(self):
        print("But you can't see me ...")

    def accessible(self):
        print("The srcret message is:")
        self.__inaccessible()

s = Secretive()
s.accessible()
# 在类定义中，对所有以两个下划线打头的名称都进行转换，即在开头
# 加上一个下划线和类名
# 访问私有的方法
s._Secretive__inaccessible()



class Calculator:
    def calculate(self,expression):
        self.value = eval(expression)

class Talker:
    def talk(self):
        print("Hi ,my value is,",self.value)
class TalkCalculator(Talker, Calculator):
    pass
tc = TalkCalculator()
tc.calculate("1 + 1 + 2")
tc.talk()
print("="*20)


class BaseClass:
    num_base_calls = 0
    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_calls += 1

class LeftSubclass(BaseClass):
    num_left_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on Lef Subclass")
        self.num_left_calls += 1

class RightSubclass(BaseClass):
    num_right_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on Right Subclass")
        self.num_right_calls += 1

class Subclass(LeftSubclass, RightSubclass):
    num_sub_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on Subcalss")
        self.num_sub_calls += 1
s = Subclass()
s.call_me()

class A(object):
    def f(self):
        print('A')
class B(object):
    def f(self):
        print('B')
class C(A,B):
    pass
class D(A,B):
    def f(self):
        print("D")
class E(C,D):
    pass
s = E()
s.f()
