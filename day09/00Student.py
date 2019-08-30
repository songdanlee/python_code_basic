class Student():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def paly_game(self, game):
        print(f"{self.name}爱玩游戏--{game}")

    def sleep(self):
        self.paly_game("守卫萝卜")
        print("太黑了，睡觉了")


s = Student("如花似玉", 18, '女')

