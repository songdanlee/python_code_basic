"""
敌方坦克射击

"""

import sys
import pygame
import random

SCRREN_WIDTH = 1300
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

    def shoot(self):
       pass


class EnemyTank(Tank):
    def __init__(self, x, y):
        super(EnemyTank, self).__init__(x, y)
        self.images = {
            'U': pygame.image.load('tank_img/enemy1U.gif'),
            'D': pygame.image.load('tank_img/enemy1D.gif'),
            'L': pygame.image.load('tank_img/enemy1L.gif'),
            'R': pygame.image.load('tank_img/enemy1R.gif'),
        }
        # 随机方向
        self.direction = self.rand_direction()
        self.image = self.images[self.direction]
        # 随机速度
        self.speed = random.randint(1, 3)
        # 移动的步数
        self.step = random.randint(1, 10) * self.speed + 40

    # 随机方向
    def rand_direction(self):
        directions = ['U', 'D', 'L', "R"]
        return random.choice(directions)

    def move(self):
        if self.step:
            super().move()
            self.step -= 1
        else:
            self.direction = self.rand_direction()
            self.step = random.randint(40, 60) * (4 - self.speed)


# 子弹类
class Bullet:
    def __init__(self, tank):
        self.images = {
            'm': pygame.image.load("tank_img/tankmissile.gif"),
            'e': pygame.image.load("tank_img/enemymissile.gif")
        }
        self.image = self.images['m']
        # 是否活着
        self.live = True
        # 方向
        self.direction = tank.direction
        self.speed = 5
        # 设置子弹的位置
        self.rect = self.image.get_rect()
        # 子弹初始方向优化
        if self.direction == 'U':
            self.rect.centerx = tank.rect.centerx
            self.rect.centery = tank.rect.centery - tank.rect.height // 2 - self.rect.height // 2
        elif self.direction == 'D':
            self.rect.centerx = tank.rect.centerx
            self.rect.centery = tank.rect.centery + tank.rect.height // 2 + self.rect.height // 2
        elif self.direction == 'L':
            self.rect.centery = tank.rect.centery
            self.rect.centerx = tank.rect.centerx - tank.rect.height // 2 - self.rect.height // 2
        elif self.direction == 'R':
            self.rect.centery = tank.rect.centery
            self.rect.centerx = tank.rect.centerx + tank.rect.height // 2 + self.rect.height // 2
        # 子弹的移动

    def move(self):

        if self.direction == 'U':
            if self.rect.centery > self.rect.height // 2:
                self.rect.centery -= self.speed
            else:
                self.live = False
        elif self.direction == 'D':
            if self.rect.centery + self.rect.height //2 < SCRREN_HEIGHT:
                self.rect.centery += self.speed
            else:
                self.live = False
        elif self.direction == 'L':
            if self.rect.centerx > self.rect.width // 2:
                self.rect.centerx -= self.speed
            else:
                self.live = False
        elif self.direction == 'R':
            if self.rect.centerx + self.rect.width // 2 < SCRREN_WIDTH:
                self.rect.centerx += self.speed
            else:
                self.live = False

    def display_bullet(self):
        MainGame.windows.blit(self.image, self.rect)

    def __str__(self):
        return f"{self.direction},{self.speed},{self.rect.x},{self.rect.y}"


# 爆炸类
class Bomb:
    pass


# 墙壁类
class Wall:
    pass


class MainGame():
    windows = None
    T1 = None
    enemy_list = []
    # 我方子弹列表
    bullet_hero = []
    def create_window(self):
        pygame.display.init()
        # 创建窗口
        MainGame.windows = pygame.display.set_mode((SCRREN_WIDTH, SCRREN_HEIGHT))
        pygame.display.set_caption("坦克大战")

    # 创建我方坦克
    def create_mtank(self):
        if not MainGame.T1:
            MainGame.T1 = MyTank(500, 400)

    # 加载我方坦克
    @classmethod
    def load_mtank(cls):
        if MainGame.T1 and MainGame.T1.live:
            MainGame.T1.display_tank()

    # 加载我方子弹列表
    def load_hero_bullet(self):
        for b in MainGame.bullet_hero:
            if b.live :
                b.display_bullet()
                b.move()
            else:
                MainGame.bullet_hero.remove(b)
    # 创建敌方坦克
    def create_etank(self):
        for i in range(5):
            enemy_tank = EnemyTank(random.randint(1, 10) * 121, random.randint(1, 10) * 33)
            MainGame.enemy_list.append(enemy_tank)

    # 加载敌方坦克
    @classmethod
    def load_etank(cls):
        for enemy_tank in MainGame.enemy_list:
            if enemy_tank.live:
                enemy_tank.display_tank()

    def start_game(self):
        # 调用创建窗口的功能
        self.create_window()
        # 调用创建坦克的方法
        self.create_mtank()
        # 调用创建敌方坦克的方法
        self.create_etank()
        while True:
            # 填充颜色
            MainGame.windows.fill(color)
            clock.tick(60)
            # 调用加载我方坦克的方法
            self.load_mtank()
            # 加载我方坦克子弹
            self.load_hero_bullet()
            # 加载敌方坦克
            self.load_etank()
            # 我方调用移动方法
            MainGame.T1.move()

            # 调用敌方坦克移动
            for e_tank in MainGame.enemy_list:
                e_tank.move()

            self.deal_event()
            # 屏幕刷新
            pygame.display.update()

    # 事件处理
    def deal_event(self):
        for event in pygame.event.get():  # 遍历所有事件
            if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if len(MainGame.bullet_hero) < 3:
                        MainGame.bullet_hero.append(Bullet(MainGame.T1))
                    else:
                        print("子弹最多三发")

MainGame().start_game()
