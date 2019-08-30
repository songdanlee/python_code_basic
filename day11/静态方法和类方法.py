class Goods():
    def __init__(self,name,price):
        self.name = name
        self.__price = price
        self.__discount = 1

    def change_discount(self,new_discount):
        self.__discount = new_discount
    @property
    def price(self):
        return self.__price*self.__discount
#创建苹果  打八折
apple = Goods("苹果",13)
print(apple.price)
apple.change_discount(0.8)
print(apple.price)


banana = Goods("香蕉",10)
print(banana.price)

