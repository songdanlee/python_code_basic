import time
import sys
import random

# 创建枪对应的类型和弹夹，子弹伤害的关系
DICT_GUN = {
    "AWM": {"clip": 100, "bullet": 10},
    "SRL": {"clip": 150, "bullet": 120},
    "K98": {"clip": 80, "bullet": 200},
    "Win94": {"clip": 30, "bullet": 50},
}


# 封装子弹类 属性：伤害值
class Bullet():
    def __init__(self, damage):
        self.damage = damage

    def move(self,enemy):
        print(f"子弹飞向{enemy.name}")


# 封装弹夹类
# 属性：弹夹容量 存储子弹的列表
class Clip():
    def __init__(self, size, bullets):
        self.size = size
        self.bullets = bullets

    def __str__(self):
        return f"弹夹容量为{self.size},当前有{len(self.bullets)}发子弹"


# 封装枪类
# 属性：型号  弹夹 = None
# 行为：
# 射击(敌人) < 打出一颗子弹 >
class Gun():

    def __init__(self, type, clip):
        self.type = type
        self.clip = clip

    def shoot(self,enemy):
        print("射击，打出一个子弹")
        bullet = self.clip.bullets.pop()
        bullet.move(enemy)
        return bullet

    def __str__(self):
        return f"{self.type}枪，{self.clip}"


# 封装狙击手类
# 属性：名字   枪 = None
# 行为：
# 捡枪(枪)
# 装弹 < 创建弹夹，循环创建子弹，装进弹夹里，然后把弹夹装到墙上 >
# 瞄准(敌人)
# 射击(敌人) < 调用枪的射击方法 >
class Sniper():
    def __init__(self, name):
        self.name = name
        self.gun = None

    def pickGun(self, gun):
        if isinstance(gun, Gun):
            self.gun = gun
            print(f"{self.name}捡到一把{self.gun.type}")
        else:
            print("捡枪失败")

    def reload(self):
        print(self.gun.clip.size)
        if self.__checkGUN():
            if self.gun.clip.size == len(self.gun.clip.bullets):
                print("弹夹已满")
            else:
                # 通过枪的型号获取子弹伤害
                bullet = DICT_GUN.get(self.gun.type).get("bullet")
                # 弹夹容量
                clip = self.gun.clip
                count = 0
                while len(clip.bullets) < clip.size:
                    time.sleep(0.001)
                    clip.bullets.append(Bullet(bullet))
                    count += 1
                    if count % 10 == 0:
                        print("装弹--------ing")
                        count = 0
                print(f"弹夹装填完毕,共有{clip.size}发子弹")

    def aim(self, enemy):
        if self.__checkGUN():
            print("瞄准...........")
            time.sleep(2)

            print(f"瞄准{enemy.name}完毕")

    def shoot(self, enemy):
        if self.__checkBullets() == 0:
            self.reload()
            print("重新瞄准")
            self.aim(enemy)
        if self.__checkGUN():
            bullet = self.gun.shoot(enemy)
            enemy.getShot(bullet)

            if enemy.isAlive():
                print(f"{enemy.name}中弹,还有{enemy.hp}血")
            else:
                print(f"{self.name}用{self.gun.type}枪,击败了{enemy.name}")
                sys.exit(0)
            print(f"弹夹还有{len(self.gun.clip.bullets)}发子弹")

    def __checkGUN(self):
        if self.gun == None:
            print("当前没有可以操作的枪，请先捡枪")
            return 0
        return 1

    def __checkBullets(self):
        if len(self.gun.clip.bullets) > 0:
            return 1
        else:
            print("已经没有子弹，正在准备装弹")
            return 0


# 5.封装敌人类
# 属性：名称   生命值
# 行为：是否死亡<根据生命值进行判断，如果<=0，应声倒下>
class Enemy():
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def isAlive(self):
        if self.hp > 0:
            return 1
        else:
            return 0
    def getShot(self,bullet):
        self.hp -= bullet.damage

# 利用字典创建枪
# 随机向弹夹添加子弹
def GUNFactory(k):
    lis = []
    #
    for i in range(random.randint(1, 20)):
        lis.append(Bullet(DICT_GUN.get(k).get("bullet")))
    clp = Clip(DICT_GUN.get(k).get("clip"), lis)
    return Gun(k, clp)


# 狙击手xxx捡起一把xx枪，装弹，瞄准敌人xxx，射击,敌人生命值归0，应声倒下
if __name__ == '__main__':
    enermy = Enemy("play01", 1000)
    # enermy.isAlive()

    gunlist = ["AWM", "SRL", "98K", "Win94"]
    #  创建四把枪
    AWM = GUNFactory("AWM")
    SRL = GUNFactory("SRL")
    K98 = GUNFactory("K98")
    Win94 = GUNFactory("Win94")
    # print(AWM.clip.size)
    # print(SRL)
    # print(K98)
    # print(Win94)

    player = Sniper("sniper")

    player.pickGun(AWM)
    # player.reload()
    while enermy.hp > 0:
        player.aim(enermy)
        player.shoot(enermy)
