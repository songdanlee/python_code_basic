"""
 1.完善我方坦克类
        属性：
            坐标
            图片集
            方向
            图片
            移动速度
            区域
            是否活着
        行为：
            移动
            设计
            展示（将坦克加到窗口中）

    2.加载我方坦克
        1.封装创建我方坦克的方法
        2.封装加载我方坦克的方法
        3.完成调用
"""

import sys
import pygame

SCRREN_WIDTH = 1000
SCRREN_HEIGHT = 700


class Tank():

    def __init__(self, x, y):
        self.images = {
            'U': pygame.image.load('tank_img/p1tankU.gif'),
            'D': pygame.image.load('tank_img/p1tankD.gif'),
            'L': pygame.image.load('tank_img/p1tankL.gif'),
            'R': pygame.image.load('tank_img/p1tankR.gif'),

        }
        self.direction = 'U'
        self.image = self.images[self.direction]
        # 移动速度
        self.speed = 3
        # 获取图片占据的矩形区域
        self.rect = self.image.get_rect()
        # 根据传入的参数，决定坦克的位置
        self.rect.x = x
        self.rect.y = y
        # 是否存活
        self.live = True

    def move(self):
        pass

    def shoot(self):
        pass

    # 将坦克加到窗口
    def display_tank(self):
        self.image = self.images[self.direction]
        MainGame.windows.blit(self.image, self.rect)


class MyTank(Tank):
    pass


class MainGame():
    windows = None
    T1 = None
    def create_window(self):
        pygame.display.init()
        # 创建窗口
        MainGame.windows = pygame.display.set_mode((SCRREN_WIDTH, SCRREN_HEIGHT))
        pygame.display.set_caption("坦克大战")

    def create_tank(self):
        if not MainGame.T1:
            MainGame.T1 = MyTank(500,400)

    def load_tank(self):
        MainGame.T1.display_tank()

    def start_game(self):

        self.create_window()
        self.create_tank()
        while True:
            # 屏幕刷新
            pygame.display.update()
            self.load_tank()
            self.deal_event()

    def deal_event(self):
        for event in pygame.event.get():  # 遍历所有事件
            if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
                sys.exit()

MainGame().start_game()
