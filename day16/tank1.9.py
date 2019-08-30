"""
坦克与墙的碰撞

"""

import sys
import pygame
import random

SCRREN_WIDTH = 1300
SCRREN_HEIGHT = 700
clock = pygame.time.Clock()
color = pygame.color.Color("#8B4513")


class Tank:

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
        # 记录旧坐标
        self.oldx = self.rect.x
        self.oldy = self.rect.y
        # 是否存活
        self.live = True

    def back(self):
        self.rect.x = self.oldx
        self.rect.y = self.oldy

    def hit_wall(self):
        for wall in MainGame.wall_list:
            if pygame.sprite.collide_rect(self,wall):
                self.back()

    def move(self):
        # 每次移动前先记录旧坐标
        self.oldx = self.rect.x
        self.oldy = self.rect.y
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

    # 实现射击方法
    def shoot(self):
        return Bullet(self)

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
        # 子弹计数
        self.count = 0

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

    def shoot(self):
        self.count += 1
        if self.count > 50:
            b = super().shoot()
            MainGame.bullet_enemy.append(b)
            self.count = 1


# 子弹类
class Bullet:
    def __init__(self, tank):
        self.images = {
            'e': pygame.image.load("tank_img/tankmissile.gif"),
            'm': pygame.image.load("tank_img/enemymissile.gif")
        }
        if isinstance(tank, MyTank):
            self.image = self.images['m']
        else:
            self.image = self.images['e']
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
            if self.rect.centery + self.rect.height // 2 < SCRREN_HEIGHT:
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

    def hit_enemy_tank(self):
        for e_tank in MainGame.enemy_list:
            if pygame.sprite.collide_rect(self, e_tank):
                self.live = False
                e_tank.live = False
                MainGame.bomb_list.append(Bomb(e_tank))

    def hit_mytank(self):
        if pygame.sprite.collide_rect(self, MainGame.T1):
            self.live = False
            MainGame.bomb_list.append(Bomb(MainGame.T1))
            MainGame.T1.live = False
    # 子弹撞墙方法
    def hit_wall(self):
        for wall in MainGame.wall_list:
            if pygame.sprite.collide_rect(self,wall):
                self.live = False
                # 墙的生命值减少
                wall.hp -= 1


# 爆炸类
class Bomb:
    def __init__(self, tank):
        self.images = [
            pygame.image.load('tank_img/blast0.gif'),
            pygame.image.load('tank_img/blast1.gif'),
            pygame.image.load('tank_img/blast2.gif'),
            pygame.image.load('tank_img/blast3.gif'),
            pygame.image.load('tank_img/blast4.gif'),
            pygame.image.load('tank_img/blast5.gif')
        ]
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = tank.rect
        self.live = True

    def display_bomb(self):
        if self.image_index < len(self.images):
            self.image = self.images[self.image_index]
            MainGame.windows.blit(self.image, self.rect)
            self.image_index += 1
        else:
            self.image_index = 0
            self.live = False


# 墙壁类
class Wall:
    def __init__(self, x, y):
        self.image = pygame.image.load("tank_img/walls.gif")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hp = 3

    def display_wall(self):
        MainGame.windows.blit(self.image, self.rect)


class MainGame(object):
    windows = None
    T1 = None
    enemy_list = []
    # 我方子弹列表
    bullet_hero = []
    # 敌方子弹列表
    bullet_enemy = []
    # 存储所有爆炸效果类
    bomb_list = []
    # 存储所有墙壁
    wall_list = []

    def create_window(self):
        pygame.display.init()
        # 创建窗口
        MainGame.windows = pygame.display.set_mode((SCRREN_WIDTH, SCRREN_HEIGHT))
        pygame.display.set_caption("坦克大战")

    # 创建墙壁类
    def create_wall(self):
        wall = Wall(SCRREN_WIDTH // 2, SCRREN_HEIGHT - 60)
        MainGame.wall_list.append(wall)
        wall = Wall(SCRREN_WIDTH // 2, SCRREN_HEIGHT - 120)
        MainGame.wall_list.append(wall)
        wall = Wall(SCRREN_WIDTH // 2 + 60, SCRREN_HEIGHT - 120)
        MainGame.wall_list.append(wall)
        wall = Wall(SCRREN_WIDTH // 2 + 120, SCRREN_HEIGHT - 120)
        MainGame.wall_list.append(wall)
        wall = Wall(SCRREN_WIDTH // 2 + 120, SCRREN_HEIGHT - 60)
        MainGame.wall_list.append(wall)


    # 加载墙壁类
    def load_wall(self):
        for wall in MainGame.wall_list:
            if wall.hp > 0:
                wall.display_wall()
            else:
                MainGame.wall_list.remove(wall)

    # 创建我方坦克
    def create_mtank(self):
        if not MainGame.T1:
            MainGame.T1 = MyTank(500, 400)

    # 加载我方坦克
    def load_mtank(cls):
        if MainGame.T1 and MainGame.T1.live:
            MainGame.T1.display_tank()
            # 我方调用移动方法
            MainGame.T1.move()
            MainGame.T1.hit_wall()
        else:
            # 从内存删除我方坦克
            del MainGame.T1
            MainGame.T1 = None
    # 创建敌方坦克
    def create_etank(self):
        for i in range(10):
            enemy_tank = EnemyTank(random.randint(1, 10) * 121, random.randint(1, 10) * 33)
            MainGame.enemy_list.append(enemy_tank)

    # 加载敌方坦克
    def load_etank(cls):
        for enemy_tank in MainGame.enemy_list:
            if enemy_tank.live:
                enemy_tank.display_tank()
                # 敌方坦克移动
                enemy_tank.move()
                # 是否撞墙
                enemy_tank.hit_wall()
                # 调用优化后的射击方法
                enemy_tank.shoot()
            else:
                # 移除已经死亡的坦克
                MainGame.enemy_list.remove(enemy_tank)

    # 加载我方子弹列表
    def load_hero_bullet(self):
        for b in MainGame.bullet_hero:
            if b.live:
                b.display_bullet()
                b.move()
                # 检测打中敌方坦克
                b.hit_enemy_tank()
                # 检测是否打中墙
                b.hit_wall()
            else:
                # 从子弹列表移除子弹
                MainGame.bullet_hero.remove(b)

    # 加载敌方子弹列表
    def load_enemy_bullet(self):
        for b in MainGame.bullet_enemy:
            if b.live:
                # 展示子弹
                b.display_bullet()
                # 移动子弹
                b.move()
                # 我方坦克存在才会进行碰撞检测
                if MainGame.T1 and MainGame.T1.live:
                    b.hit_mytank()
                # 检测敌方子弹是否打中墙
                b.hit_wall()
            else:
                MainGame.bullet_enemy.remove(b)

    # 加载所有爆炸效果
    def load_bomb(self):
        for bomb in MainGame.bomb_list:
            if bomb.live:
                bomb.display_bomb()
            else:
                MainGame.bomb_list.remove(bomb)

    def start_game(self):
        # 调用创建窗口的功能
        self.create_window()
        # 创建墙壁
        self.create_wall()
        # 调用创建坦克的方法
        self.create_mtank()
        # 调用创建敌方坦克的方法
        self.create_etank()
        while True:
            # 填充颜色
            MainGame.windows.fill(color)
            # 加载墙壁
            self.load_wall()
            clock.tick(60)
            # 调用加载我方坦克的方法
            self.load_mtank()
            # 加载我方坦克子弹
            self.load_hero_bullet()
            # 加载敌方坦克
            self.load_etank()
            # 加载敌方子弹
            self.load_enemy_bullet()
            # 加载爆炸效果
            self.load_bomb()
            # 处理事情
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
                    if len(MainGame.bullet_hero) < 5:
                        # 我方坦克存在才可以发射子弹
                        if MainGame.T1 and MainGame.T1.live:
                            MainGame.bullet_hero.append(Bullet(MainGame.T1))
                    else:
                        print("子弹最多五发")


MainGame().start_game()
