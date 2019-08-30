# 1、封装技能类
# 	属性：
# 		技能名
# 		技能伤害值
# 2、封装我方英雄类
# 	属性：
# 		生命值
# 		攻击力
# 		技能列表
# 	行为：
# 		普通攻击(hero2)
# 		暴击(hero2)
# 		技能攻击(hero2)
# 		思路：对方损失生命值，损失多少取决于自身的攻击力，如果是技能攻击，则取决于
# 			技能伤害值
# 3、封装敌方英雄类
# 	属性：
# 		生命值
# 		攻击力
# 		技能列表
# 	行为：
# 		普通攻击(hero1)
# 		技能攻击(hero1)
# 		思路：对方损失生命值，损失多少取决于自身的攻击力，如果是技能攻击，则取决于
# 			技能伤害值
# 4、完成回合制的游戏设计
# 	while True:
# 		A->B
# 		if b 凉了：
# 			游戏结束，A赢了
#
# 		B->A
# 		if a 凉了：
# 			游戏结束，B赢了


"""
优化了暴击的伤害

"""
import random


class Skill():
    def __init__(self, name_, damage_):
        self.name = name_
        self.damage = damage_


class Hero():
    #   crt 暴击率，伤害值= atck*(1+crt)
    def __init__(self, name_, hp_, atk_, skills_, crt=0):
        self.name = name_
        self.hp = hp_
        self.atk = atk_
        self.skills = skills_
        self.crt = crt

    # 普通攻击
    def normalAtk(self, others):
        others.hp -= self.atk
        if others.hp < 0:
            others.hp = 0
        print(f"\033[0;33m{self.name}\033[0m使用\033[1;36m普通攻击\033[0m 对\033[1;34m {others.name}\033[0m造成{self.atk}点伤害,\033[1;34m {others.name}\033[0m还有{others.hp}血")

        self.criticalStrike(others)

    # 技能伤害
    def skillAtk(self, others, skil):
        others.hp -= skil.damage
        if others.hp < 0:
            others.hp = 0
        print(f"\033[0;33m{self.name}\033[0m使用\033[5;31m{skil.name}\033[0m对\033[1;32;34m {others.name}\033[0m造成{skil.damage}点伤害,\033[1;34m {others.name}\033[0m还有{others.hp}血")

    # 暴击随机产生
    def criticalStrike(self, others):
        # 暴击产生条件：随机数小于等于暴击率不为
        if random.random() < self.crt / 100:
            # 暴击伤害 = ( (1+暴击率)*基础伤害 + (1-攻击力)的随机值)
            damage = int(self.atk * (1 + self.crt / 100) + random.randint(1,self.atk))
            others.hp -= damage
            if others.hp < 0:
                others.hp = 0
            print(f"\033[0;33m{self.name}\033[0m的攻击出现\033[1;41m暴击\033[0m\033[1;32;34m {others.name}\033[0m血量-{damage},\033[1;32;34m{others.name}\033[0m还有{others.hp}血")


s1 = [Skill("巨龙撞击", 10), Skill("黄金圣盾", 15), Skill("天崩地裂", 40)]
s2 = [Skill("暴雨梨花", 15), Skill("风卷残云", 20), Skill("末日风暴", 45)]
h1 = Hero("嘉文四世", 100, 10, s1,20)
h2 = Hero("时光守护者", 90, 8, s2,40)
# print(random.choice(s1).name)
while True:

    choice = eval(input("请输入你的攻击方式：1 普通攻击  2 技能攻击"))
    if choice == 1:
        h1.normalAtk(h2)

    elif choice == 2:

        for i, v in enumerate(h1.skills):
            print(f"技能号:{i} 技能名:{v.name} 伤害值:{v.damage}")
        ch = eval(input("请输入释放的技能号:"))
        h1.skillAtk(h2, h1.skills.pop(i))
    if h2.hp <= 0:
        print(f"\033[4;31;45m{h1.name}\033[0m战胜了{h2.name}")
        break

    # 随机攻击：
    if random.random() > 0.3 and len(h2.skills) != 0:
        h2_skil = random.choice(h2.skills)
        h2.skills.remove(h2_skil)
        h2.skillAtk(h1, h2_skil)
    else:
        h2.normalAtk(h1)

    if h1.hp <= 0:
        print(f"\033[4;31;45m{h2.name}\033[0m战胜了{h1.name}")
        break
