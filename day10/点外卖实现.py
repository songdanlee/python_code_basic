import time


# 外卖类
class Food():

    def __init__(self, money, name):
        self.money = money
        self.name = name

    def __str__(self) -> str:
        return f"{self.name}"


class DeliverMan():

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def deliver(self, food, custom):
        print("您的外卖正在飞速赶来，请耐心等待")
        time.sleep(5)
        print(f"{custom.name}，您的{food}已送达")

        self.five_star()

    def five_star(self):
        print("****请给五星好评哟****")


class Merchant():

    def __init__(self, name, food_menu):
        self.food_menu = food_menu
        self.name = name

    # 打印菜单
    def show_food(self):
        for index, i in enumerate(self.food_menu):
            print(index, i)

    def take_order(self, food, customer, delive):
        print(f"{customer}的{food}已下单")
        delive.deliver(food, customer)

    def __str__(self) -> str:
        return f"{self.name}"


class APP():

    def __init__(self, name, mechant_list, deliver_list):
        self.name = name
        self.mechant_list = mechant_list
        self.deliver_list = deliver_list

    def cal_food(self, custom):
        # 显示所有餐馆的菜单
        for index, mechant in enumerate(self.mechant_list):
            print(f"第{index + 1}个餐馆，名字是{mechant},菜单如下")
            mechant.show_food()
        # 用户选择喜欢的菜，下订单
        m_name, f_name = custom.choose_food()
        print(self.mechant_list[m_name - 1].food_menu[f_name])
        self.mechant_list[m_name - 1].take_order(self.mechant_list[m_name - 1].food_menu[f_name], custom, d1)


class Customer():

    def __init__(self, name, money, phone, addr):
        self.name = name
        self.money = money
        self.phone = phone
        self.addr = addr

    def cal_food(self, app):
        app.cal_food(self)

    # 选择一个餐馆，点餐
    def choose_food(self):
        m_name = eval(input("请输入餐馆的编号"))
        f_name = eval(input("请输入想要吃的菜的编号"))
        return m_name, f_name

    def __str__(self) -> str:
        return f"{self.name}"


food1 = Food(20, "宫保鸡丁")
food3 = Food(20, "北京烤鸭")
food2 = Food(10, "煎饼果子")
# print(food)
food_lists1 = []
food_lists2 = []
food_lists1.append(food1)
food_lists1.append(food3)
food_lists2.append(food2)

d1 = DeliverMan("快递员1", "123456")
d2 = DeliverMan("快递员2", "234567")
d_list = [d1, d2]

m1 = Merchant("木子餐馆", food_lists1)
m2 = Merchant("子木餐馆", food_lists2)
m_list = [m1, m2]

app = APP("美团", m_list, d_list)

customer = Customer("张三", 100, "7880269", "中关村")

customer.cal_food(app)
