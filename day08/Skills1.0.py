# 1、封装技能类
# 	属性：
# 		技能名
# 		技能伤害值
# class Skill():
#     def __init__(self,skill_name_, skill_damage_):
#         self.skill_name = skill_name_
#         self.skill_damage = skill_damage_
# skill1 = Skill('回旋之刃', 1300)
# print(skill1.__dict__)
# skill2 = Skill('不灭魔躯', 2800)
# print(skill2.__dict__)

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
# class Hero():
#     def __init__(self, hp_, attack_, skill_list):
#         self.hp = hp_
#         self.attack = attack_
#         self.skill_list = skill_list
#
# hero_kai = Hero(8000, 950, ['修罗之魂', '回旋之刃', '极刃风暴', '魔神降临'])
# print(hero_kai.__dict__)
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

import random


class Skill():
    def __init__(self, name_, damage_):
        self.name = name_
        self.damage = damage_


class Hero():

    def __init__(self, name_, hp_, atk_, skills_):
        self.name = name_
        self.hp = hp_
        self.atk = atk_
        self.skills = skills_

    # 普通攻击
    def normalAtk(self, others):
        others.hp -= self.atk
        if others.hp < 0:
            others.hp = 0
        print(f"{self.name}使用普通攻击对{others.name}造成{self.atk}点伤害，{others.name}还有{others.hp}血")
        if self.name == "嘉文四世":
            self.criticalStrike(others)

    # 技能伤害
    def skillAtk(self, others, skil):
        others.hp -= skil.damage
        if others.hp < 0:
            others.hp = 0
        print(f"{self.name}使用{skil.name}对{others.name}造成{skil.damage}点伤害，{others.name}还有{others.hp}血")

    # 暴击随机产生
    def criticalStrike(self, others):
        if random.random() >= 0.95:
            others.hp -= 2
            print(f"你的攻击出现暴击，敌方血量-2,{others.name}还有{others.hp}血")
        if others.hp < 0:
            others.hp = 0


s1 = [Skill("巨龙撞击", 10), Skill("黄金圣盾", 15), Skill("天崩地裂", 40)]
s2 = [Skill("暴雨梨花", 15), Skill("风卷残云", 20), Skill("末日风暴", 45)]
h1 = Hero("嘉文四世", 100, 10, s1)
h2 = Hero("时光守护者", 90, 5, s2)
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
        print("你赢了")
        break

    # 随机攻击：
    if random.random() > 0.3 and len(h2.skills) != 0:
        h2_skil = random.choice(h2.skills)
        h2.skills.remove(h2_skil)
        h2.skillAtk(h1, h2_skil)
    else:
        h2.normalAtk(h1)

    if h1.hp <= 0:
        print("你输了")
        break
