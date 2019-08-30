"""
# 简单工厂
# 简单工厂定义一个Factory类，可以根据参数的不同返回不同类的实例，
# 被创建的实例通常有共同的父类。实质是由一个工厂类根据传入的参数，动态决定应该创建哪一个产品类实例。
class Car(object):
    def run(self):
        print("吧里吧里的跑")
    def stop(self):
        print("蹭蹭的停车")


class BMW(Car):
    def run(self):
        print("宝马--->吧里吧里的跑")
    def stop(self):
        print("宝马--->蹭蹭的停车")


class Benz(Car):
    def run(self):
        print('奔驰-->>>吧里吧里的跑...')

    def stop(self):
        print('奔驰-->>>蹭蹭的停车...')


class Skoda(Car):
    def run(self):
        print('斯柯达-->>>吧里吧里的跑...')

    def stop(self):
        print('斯柯达-->>>蹭蹭的停车...')


class CarFactory():
    def new_cart(self,name):
        if name == "BMW":
            return BMW()
        elif name == "Benz":
            return Benz()
        elif name == "skd":
            return Skoda()


class CarStore():
    def __init__(self,factory):
        self.factory = factory

    def order(self,name):
        return self.factory.new_cart(name)


car_factory = CarFactory()
car_store = CarStore(car_factory)
car = car_store.order('skd')
car.run()
car.stop()
"""
"""
# 工厂方法 把工厂类进行改进，提升为一个抽象类（接口），把对具体产品的实现交给对应的具体的子类去做，解耦多个产品之间的业务逻辑。
from abc import ABCMeta, abstractmethod


class Car(object, metaclass=ABCMeta):
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def stop(self):
        print("蹭蹭的停车")


class BMW(Car):
    def run(self):
        print("宝马--->吧里吧里的跑")

    def stop(self):
        print("宝马--->蹭蹭的停车")


class Benz(Car):
    def run(self):
        print('奔驰-->>>吧里吧里的跑...')

    def stop(self):
        print('奔驰-->>>蹭蹭的停车...')


class Skoda(Car):
    def run(self):
        print('斯柯达-->>>吧里吧里的跑...')

    def stop(self):
        print('斯柯达-->>>蹭蹭的停车...')


class Factory(metaclass=ABCMeta):
    @abstractmethod
    def create_car(self):
        pass


class BMWFactory(Factory):
    def create_car(self):
        return BMW()


class BenzFactory(Factory):
    def create_car(self):
        return Benz()


class SkodaFactory(Factory):
    def create_car(self):
        return Skoda()


def test():
    bmw = BMWFactory().create_car()
    bmw.run()
    bmw.stop()


test()
"""

# 抽象工厂  所谓抽象工厂是指一个工厂等级结构可以创建出分属于不同产品等级结构的一个产品族中的所有对象
'''抽象工厂：
1.抽象工厂主要目的是提供一个接口来创建一系列相关对象，而无需指定具体的类。
2.相比于之前的需要我们去指定创建什么对象，抽象工厂不需要。'''
from abc import ABCMeta, abstractmethod


class PizzaFactory(metaclass=ABCMeta):
    # 有蔬菜的披萨
    @abstractmethod
    def create_veg_pizza(self):
        pass

    # 没蔬菜的披萨
    @abstractmethod
    def create_non_veg_pizza(self):
        pass


class USAPizzaFactory(PizzaFactory):
    # USA披萨店里有蔬菜的披萨是玉米披萨
    def create_veg_pizza(self):
        return CornPizza()

    # USA店里没蔬菜的披萨是牛肉披萨
    def create_non_veg_pizza(self):
        return BeefPizza()


class ChinaPizzaFactory(PizzaFactory):
    # 中国披萨店里有蔬菜的披萨是水果披萨
    def create_veg_pizza(self):
        return FruitsPizza()

    # 中国披萨店里没有蔬菜的披萨是羊肉披萨
    def create_non_veg_pizza(self):
        return MuttonPizza()


# 接下来定义4种披萨和他们的父类（有蔬菜和无蔬菜）
class VegPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self, veg_pizza):
        pass


# 没蔬菜的披萨在有蔬菜的披萨上面加肉就可以
class NonVegPizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self, veg_pizza):
        pass


class CornPizza(VegPizza):
    def prepare(self):
        print(type(self).__name__, '来了')


class BeefPizza(NonVegPizza):
    def serve(self, veg_pizza):
        print(type(self).__name__, '来了，牛肉是加在', type(veg_pizza).__name__, '里面的')


class FruitsPizza(VegPizza):
    def prepare(self):
        print(type(self).__name__, '来了')


class MuttonPizza(NonVegPizza):
    def serve(self, veg_pizza):
        print(type(self).__name__, '来了，羊肉是加在', type(veg_pizza).__name__, '里面的')


class PizzaStore(object):
    def __init__(self):
        pass

    def make_pizzas(self):
        # 创建的是所有对象（所有披萨），而不是单个指定对象
        for factory in [USAPizzaFactory(), ChinaPizzaFactory()]:
            self.factory = factory
            self.non_veg_pizza = self.factory.create_non_veg_pizza()
            self.veg_pizza = self.factory.create_veg_pizza()
            # 调用
            self.veg_pizza.prepare()
            self.non_veg_pizza.serve(self.veg_pizza)


pizza = PizzaStore()
pizza.make_pizzas()
