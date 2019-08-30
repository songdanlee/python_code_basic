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
    def create7Random():  # 随机生成号码序列
        lis = []
        for i in range(0, 6):
            num = random.randint(1, 33)
            while (RandomUtils.checkExist(lis, num)):
                num = random.randint(1, 33)
            lis.append(num)
        lis.sort()
        num = random.randint(1, 16)
        lis.append(num)

        return lis

    @staticmethod
    def createLuckNum():  # 生成中奖序列
        return RandomUtils.create7Random()

    @staticmethod
    def checkExist(lis, num):  # 判断数字在序列里是否存在
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
    #
    # # 判断对象相等，重写这个方法
    # def equal(self, other):


    # 对象输出格式化
    def __repr__(self):
        return "双色球:red=%s blue= %s" % (self.balls[:-1], self.balls[-1])


class BallsMachine:
    guess = []

    def __init__(self):
        self.guess = []

    # 创建一个号码,机器创建
    def createDichroicBall(self):
        m = DichroicBall()
        m.setBalls(RandomUtils.create7Random())
        self.guess.append(m)



    # 创建N个号码，机器创建
    def createDichroicBallN(self, num):
        for i in range(0, num):
            s = self.createDichroicBall()
        print("机器选择如下:")
        for i in self.guess:
            print(i)

    # 生成中奖彩色球
    @staticmethod
    def createLuckBall():
        luckNum = RandomUtils.createLuckNum()
        luck_ball = DichroicBall()
        luck_ball.setBalls(luckNum)
        return luck_ball

    # 判断是否中奖
    def eqalBalls(self, luck_ball):
        for ball in self.guess:
            a = ball.getBalls()
            b =luck_ball.getBalls()
            v = set(a[:-1]) & set(b[:-1])
            b = "中" if a[-1] == b[-1] else "不中"
            print(f"中奖红球号为{v},蓝球{b}")


    # 人工输入彩色球
    def personInput(self):
        lis = list()
        i = 0
        while i < 6:
            num = eval(input("请输入红球的号码"))
            if num in lis:
                print("号码已存在")
            elif not 1 <= num <= 33:
                print("号码输入有误")
            else:
                lis.append(num)
                i += 1
        lis.sort()

        while True:
            num = eval((input("请输入蓝球的号码")))
            if 1 <= num <= 16:
                lis.append(num)
                break
            else:
                print("号码输入有误")

        get_ball = DichroicBall()
        get_ball.setBalls(lis)
        self.guess.append(get_ball)



# 测试人工输入和机器生产中奖号的对比
def human_input():

    pass


# 测试机器生成N个
def machineN(num):
   pass



# 测试机器生成一个
def machine1():
    pass


if __name__ == '__main__':


    while True:
        num = eval(input("请输入选项，1 手工输入号码\t2 机器随机选择号码\t0 退出\t3.查看开奖"))
        if num == 1:
            mc = BallsMachine()
            # 人工输入号码
            mc.personInput()
            print(mc.guess)
        elif num == 2:
            while True:
                choice = eval(input("请输入机器选项，1 随机选择一注\t2 机器随机N注\t"))
                if choice == 1:
                    mc = BallsMachine()
                    mc.createDichroicBall()
                    print("guess", mc.guess)
                    break
                elif choice == 2:
                    n = eval(input("请输入注数"))
                    mc = BallsMachine()
                    mc.createDichroicBallN(n)
                    break
                else:
                    print("输入有误")
        elif num == 3:
            luck_ball = BallsMachine.createLuckBall()
            # 中奖球
            print("中奖号", luck_ball)
            mc.eqalBalls(luck_ball)
        elif num == 0:
            print("下次再来哟")
            break
        else:
            print("输入有误")
