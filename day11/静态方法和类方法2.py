class Goods():
    __diccount = 1

    def __init__(self, name, price):
        self.name = name
        self.__price = price

    @classmethod
    def change_discount(cls, new_discount):
        cls.__discount = new_discount

    @property
    def price(self):
        return self.__price * self.__discount



Goods.change_discount(0.8)
apple = Goods("苹果", 13)
print(apple.price)


banana = Goods("香蕉", 10)
print(banana.price)
