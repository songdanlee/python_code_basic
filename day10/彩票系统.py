import random


# 彩票类：
# 	属性：彩票号码   彩票价格
# 	行为：展示彩票信息

class Lottery():
    def __init__(self, price, num):
        self.price = price
        self.num = num

    def show_information(self):
        print(f"价格是{self.price},号码是{self.num}")

    def __str__(self):
        return f"彩票号码:{self.num}"

    # 重写equal方法
    def __eq__(self, other):
        self.num.sort()
        other.num.sort()

        return self.num == other.num


# lo = Lottery(11, [3, 6, 7])
# lo1 = Lottery(10, [6, 3, 7])
# print(lo == lo1)
#
# print([6,3,7] == [6,3,7])
# print((6,3,7) == (6,3,7))


# lo.show_information()


# 系统类：
# 行为：生成彩票  彩票开奖
class System():
    def __init__(self):
        self.luck_ball = None

    # 生成彩票
    def create_lottery(self, price, num):
        lo = Lottery(price, num)
        return lo

    # 创建中奖号码
    def create_luck(self):
        if self.luck_ball is None:
            lo = []
            for i in range(3):
                lo.append(random.randint(0, 9))
            self.luck_ball = Lottery(None, lo)
            return self.luck_ball
        else:
            print("已生成中奖号码")

    # 销毁号码
    def destroy_luck(self):
        if self.luck_ball is not None:
            self.luck_ball = None
            print("销毁中奖号码成功")

    # 彩票开奖
    def lottery_draw(self):
        return self.create_luck()

    def inpput_list(self):
        lo_lii = []
        print("请输入购买彩票的号码，0-9（共3个）")
        for i in range(3):
            num = eval(input(f"请输入第{i + 1}个数"))
            lo_lii.append(num)
        return lo_lii


# 人类：
# 	属性：名字  金钱	已购彩票
# 	行为：购买彩票 兑奖 剩余金钱展示
class Human():
    def __init__(self, name, money, buy_list):
        self.name = name
        self.money = money
        self.buy_list = buy_list

    # 购买彩票
    def buy_lottery(self, price, num, mc):
        if self.money >= price:
            lottery = mc.create_lottery(price, num)

            self.money -= price
            self.buy_list.append(lottery)
            # print(f"{self.name}购买{lottery}成功")
        else:
            print("钱不够了，请先充值")

    # 兑奖
    def expiry(self, lottery):
        if len(self.buy_list) == 0:
            print("未购买彩票")
            return -1
        for index, lo in enumerate(self.buy_list):
            print(f"购买的第{index + 1}个号码为{lo}")
            if lo == lottery:
                self.money += 200
                print("恭喜你中了200现金")
                self.show_money()
                return 1
        self.buy_list = []
        print("很遗憾，未中奖")
        self.show_money()
        return 0

    # 显示还有多少钱
    def show_money(self):
        print(f"{self.name}还有{self.money}钱")

    def show_buys(self):
        if self.buy_list == []:
            print("未购买彩票")
            return 0
        for lot in self.buy_list:
            print(lot)


lo_li = []
h1 = Human("张三", 100, lo_li)
mc = System()

# h1.buy_lottery(10, [1, 2, 3], mc)
# h1.buy_lottery(10, [3, 2, 3], mc)
# h1.buy_lottery(10, [2, 2, 3], mc)


# 实现张三花xx钱买了1注彩票，去兑奖，展示中奖结果，以及张三的剩余钱数
while True:
    choice = eval(input("请输入要进行的操作，1 购买彩票，2 兑奖，3剩余多少钱，4 展示购买列表 0退出"))
    if choice == 1:
        lo = mc.inpput_list()
        h1.buy_lottery(10, lo, mc)
    elif choice == 2:
        luck_ball = mc.create_luck()

        result = h1.expiry(luck_ball)
        if result in [1, 0]:
            print(f"中奖{luck_ball}")
            mc.destroy_luck()
    elif choice == 3:
        h1.show_money()
    elif choice == 4:
        h1.show_buys()
    elif choice == 0:
        break
