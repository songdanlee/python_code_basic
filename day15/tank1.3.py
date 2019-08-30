"""
实现坦克移动边界控制问题

"""

import sys
import pygame
import random
SCRREN_WIDTH = 1000
SCRREN_HEIGHT = 700
clock = pygame.time.Clock()
color = pygame.color.Color("#8B4513")

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
        if self.direction == 'U':
            if self.rect.y > 0:
                self.rect.y -= self.speed
        elif self.direction == 'D':
            if self.rect.y + self.rect.height < SCRREN_HEIGHT:
                self.rect.y += self.speed
        elif self.direction == 'L':
            if self.rect.x > 0:
                self.rect.x -= self.speed
        elif self.direction == 'R':
            if self.rect.x + self.rect.height < SCRREN_WIDTH:
                self.rect.x += self.speed

    def shoot(self):
        pass

    # 将坦克加到窗口
    def display_tank(self):
        self.image = self.images[self.direction]
        MainGame.windows.blit(self.image, self.rect)


class MyTank(Tank):

    def move(self):
        keystatus = pygame.key.get_pressed()

        if keystatus[pygame.K_UP]:
            self.direction = 'U'
            super().move()
        elif keystatus[pygame.K_DOWN]:
            self.direction = 'D'
            super(MyTank, self).move()
        elif keystatus[pygame.K_LEFT]:
            self.direction = 'L'
            super().move()
        elif keystatus[pygame.K_RIGHT]:
            self.direction = 'R'
            super().move()

class MainGame():
    windows = None
    T1 = None

    def create_window(self):
        pygame.display.init()
        # 创建窗口
        MainGame.windows = pygame.display.set_mode((SCRREN_WIDTH, SCRREN_HEIGHT))
        pygame.display.set_caption("坦克大战")
    # 创建我方坦克
    def create_tank(self):
        if not MainGame.T1:
            MainGame.T1 = MyTank(500, 400)
    # 加载我方坦克
    def load_tank(self):
        if MainGame.T1 and MainGame.T1.live:
            MainGame.T1.display_tank()

    def start_game(self):
        # 调用创建窗口的功能
        self.create_window()
        # 调用创建坦克的方法
        self.create_tank()
        while True:
            # 填充颜色
            MainGame.windows.fill(color)
            clock.tick(60)
            # 调用加载坦克的方法
            self.load_tank()
            # v1.0.5调用移动方法
            MainGame.T1.move()
            # 调用事件处理方法
            self.deal_event()
            # 屏幕刷新
            pygame.display.update()
    # 事件处理
    def deal_event(self):
        for event in pygame.event.get():  # 遍历所有事件
            if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
                sys.exit()


MainGame().start_game()
