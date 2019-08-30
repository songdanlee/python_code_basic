# “双色球”每注投注号码由6个红色球号码和1个蓝色球号码组成。
# 红色球号码从1--33中选择；蓝色球号码从1--16中选择
# 一等奖：7个号码相符（6个红色球号码和1个蓝色球号码）（红色球号码顺序不限，下同）
# 二等奖：6个红色球号码相符；
# 三等奖：5个红色球号码和1个蓝色球号码相符；
# 四等奖：5个红色球号码，或4个红色球号码和1个蓝色球号码相符；
# 五等奖：4个红色球号码，或3个红色球号码和1个蓝色球号码相符；
# 六等奖：1个蓝色球号码相符（有无红色球号码相符均可）。

import random
import sys


class RandomUtils:
    # 红色球不可以重复，蓝色球可以与红色球重复
    @staticmethod
    def create7Random():# 随机生成号码序列
        lis = []
        for i in range(0, 6):
            num = random.randint(1, 33)
            while (RandomUtils.checkExist(lis, num)):
                num = random.randint(1, 33)

            lis.append(num)

        num = random.randint(1, 16)
        lis.append(num)

        return lis

    @staticmethod
    def createLuckNum():# 生成中奖序列
        return RandomUtils.create7Random()

    @staticmethod
    def checkExist(lis, num):#判断数字在序列里是否存在
        if lis.count(num) == 0:
            return False
        return True


class DichroicBall:
    __balls = []

    def __init__(self):
        self.balls = None

    def getBalls(self):
        return self.balls

    def setBalls(self, balls):
        self.balls = balls

    # 判断对象相等，重写这个方法
    def __eq__(self, other):
        for i, j in zip(self.balls, other.getBalls()):
            if i != j:
                return False
        return True

    # 对象输出格式化
    def __repr__(self):
        return "双色球:red=%s blue= %s" % (self.balls[:-1], self.balls[-1])


class BallsMachine:
    guess = []

    # 创建一个号码,不传参数是机器创建，否则是人工传入
    def createDichroicBall(self, *args):
        if len(args) == 0:
            m = DichroicBall()
            m.setBalls(RandomUtils.create7Random())
            self.guess.append(m)
        else:
            for i in args:
                self.guess.append(i)

    # 创建N个号码，机器创建
    def createDichroicBallN(self, num):
        for i in range(0, num):
            s = self.createDichroicBall()
        print(self.guess)

    # 生成中奖号码
    @staticmethod
    def createLuckNum():
        luckNum = RandomUtils.createLuckNum()
        return luckNum
    # 判断是否中奖
    def eqalBalls(self, luck_ball):
        for ball in self.guess:
            if ball == luck_ball:
                print("中奖了")
                sys.exit(0)
        print("很遗憾，未中奖")
    #人工输入彩色球
    def personInput(self):
        lis = list()
        num = input("请输入球的号码")
        while True:
            if lis.count(int(num)) == 0:
                if 1<=int(num)<=33 or (1<=int(num)<=16 and len(lis)==6):
                    lis.append(int(num))
                else :
                    print("号码错误")
            else:
                print("号码存在")
            if len(lis) == 7:
                break
            num = input("请输入球的号码")

        get_ball = DichroicBall()
        get_ball.setBalls(lis)
        return get_ball

mc = BallsMachine()
luckNum = BallsMachine.createLuckNum()
# 中奖球
luck_ball = DichroicBall()
luck_ball.setBalls(luckNum)
print("中奖号", luck_ball)
# 人工输入号码
print(mc.personInput())
#机器创建一个
mc.createDichroicBall()
# print(mc.guess)
#判断是否相等
mc.eqalBalls(luck_ball)
# mc.guess.append(luck_ball)





