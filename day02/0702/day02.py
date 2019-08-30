# age = int(input("请输入你的年龄:"))
# if age >= 18:
#     print("您可以进入该网吧")
# else:
#     print("未成年，禁止进入")
#
# age = int(input("请输入你的年龄:"))
# if 1 <= age <= 120:
#     print("输入年龄正确")
# else:
#     print("年龄非法")
#
# id_card1 = 0
# id_card0 = 0
# if id_card1 == 1 or id_card0 == 1:
#     print("可以入住")
# else:
#     print("没有身份证，禁止入住")
#
# is_stu = 0
# if is_stu:
#     print("是学生，可以入校")
# else:
#     print("不是学生")
#
# for i in range(1, 10):
#     for k in range(8, i-1, -1):
#         print("        ",end="")
#     for j in range(1, i+1):
#         print("{}*{}={:2d}".format(j, i, i * j),end="\t")
#     print()


# holiday_name = input("请输入节日名称：\n")
# if holiday_name == "情人节":
#     print("看电影，买鲜花")
# elif holiday_name == "平安夜":
#     print("买苹果，吃大餐")
# elif holiday_name == "生日":
#     print("买蛋糕")
# else:
#     print("关心女朋友")
# holiday_name = input("请输入节日名称：\n")
# is_true = True
# if holiday_name == "情人节":
#     if is_true:
#         print("我的钱！！！")
#     else:
#         print("看电影，买鲜花")
# elif holiday_name == "平安夜":
#     if is_true:
#         print("和我有啥子关系")
#     else:
#         print("买苹果，吃大餐")
# elif holiday_name == "生日":
#     if is_true:
#         print("吃点蛋糕就可以了")
#     else:
#         print("买蛋糕")
# else:
#     print("关心女朋友")
#
#
# str1 = "name is {0} ,age is {1} , sex is {2}".format("lalalla", 17, '男')
# print(str1)
# str2 = "name is {name:s}, age is {age:d}, sex is {sex}".format(name="hhaha", age=18, sex='女')
# print(str2)
#
# print("{:*>6}".format(100))
# print("{:6}".format(10))
# print("{:*^6}".format(10))
# print("{:*<6}".format(10))
#
# print("{:b}".format(10))
# print("{:o}".format(10))
# print("{:x}".format(10))
#
# print("{:-^50}".format("AAAA"))
# print("{:50}".format("|"), "{:<50}".format("|"), sep="")
# print("{:50}".format("|"), "{:<50}".format("|"), sep="")
# print("{:50}".format("|"), "{:<50}".format("|"), sep="")
# print("-" * 50)

# 1-100 数字和
# count = 1
# sum = 0
# while count <= 100:
#     sum += count
#     count += 1
# print(sum)

# 1-100 偶数和
# count1 = 0
# sum1 = 0
# while count1 <= 100:
#     sum1 += count1
#     count1 += 2
# print(sum1)

# 1-2+3-4+5-6+......+99-100
# count2 = 1
# sum2 = 0
# while count2 <= 99:
#     if count2 % 2 == 0:
#         sum2 -= count2
#     else:
#         sum2 += count2
#     count2 += 1
# print(sum2)
# #
# print(-1 * 50 + 100)

# count3 = 1
# sum = 0.0
# while count3 <= 5:
#     num = float(input("请输入num%s" % count3))
#     sum += num
#     count3 += 1
# sum /= 5.0
# print(sum)

# count3 = 1
# minnum = 0
# maxnum = 0
# while count3 <= 5:
#     num = float(input("请输入num%s" % count3))
#     if count3 == 1:
#         minnum = maxnum = num
#     if minnum > num:
#         minnum = num
#     if maxnum < num:
#         maxnum = num
#     count3 += 1
# print(minnum,maxnum)


# count4 = 1
# while count4 <= 5:
#     print("*" * count4, end="")
#     print()
#     count4 += 1

# import math
#
# num = int(input("请输入一个数:"))
#
# count = 2
# while count <= math.sqrt(num):
#     if num % count == 0:
#         print(num, "不是质数")
#         break
#     count += 1
# else:
#     if num == 1:
#         print(num,"不是质数")
#     else:
#         print(num, "是质数")

# 猜拳 0剪刀  1石头  2布
# import random
#
# guess_num = random.randint(0, 2)
#
# count = 2
# while count >= 1:
#     num = int(input("请输入你要猜什么？ 0剪刀  1石头  2布:"))
#     if num == guess_num:
#         print("平局")
#     elif num == 0:
#         if guess_num == 1:
#             print("你输了,你还有%d次机会" % (count - 1))
#             print(guess_num, num)
#         else:
#             print("你赢了")
#             break
#     elif num == 1:
#         if guess_num == 2:
#             print("你输了,你还有%d次机会" % (count - 1))
#             print(guess_num, num)
#         else:
#             print("你赢了")
#             break
#     else:
#         if guess_num == 0:
#             print("你输了,你还有%d次机会" % (count - 1))
#             print(guess_num, num)
#         else:
#             print("你赢了")
#             break
#     count -= 1

# “bat”、“bit”、“but”、“hat”、“hit”或者“hut”。

import re

pattern = '[bh][a|i|u]t'
str2 = 'bat,bit,buthathut'

print(re.match(pattern, str2).group())
#
# print(re.findall(pattern, str2))

# 匹配由单个空格分隔的任意单词对，也就是姓和名
pattern2 = r"(.*)\s(.*)"
str3 = "Tom Jerry Hello Bye House Good God"
# print(re.findall(pattern2, str3))
#
# print(re.match(pattern2, str3).group())
# pattern = r'([A-Z]\.)+ ?[A-Z][a-z]+'
# string1 = 'S.N.Owfall'
# string2 = 'S.N. Owfall'
# print(re.match(pattern, string1).group())
# print(re.match(pattern, string2).group())

pattern = r'\d+ [A-Za-z ]+'
string1 = '1180 Bordeaux Drive'
string2 = '3120 De la Cruz Boulevard'

print(re.match(pattern, string1).group())
print(re.match(pattern, string2).group())
# 匹配以“www”起始且以“.com”结尾的简单Web域名；例如，www.://www.yahoo.com/。
# 选做题：你的正则表达式也可以支持其他高级域名，如.edu、.net等
# (例如，http://www.foothilledu)
pattern = r'((http:|https:)//)?[w]{3}\.\w+(.edu|.com|.net)'
string = 'http://www.foothill.edu'
print(re.match(pattern, string).group())

# 为gendata.py更新代码，使数据直接输出到redata.txt而不是屏幕。
# from random import randrange, choice
# from string import ascii_lowercase as lc
# from sys import maxsize
# from time import ctime
#
#
# tlds = ('com', 'edu', 'net', 'org', 'gov')
# f=open('redata.txt','w')
# for i in range(randrange(1, 30)):
#     dtint = randrange(1500000000)
#     dtstr = ctime(dtint)
#     llen = randrange(4, 8)
#     login = ''.join(choice(lc) for j in range(llen))
#     dlen = randrange(llen, 13)
#     dom = ''.join(choice(lc) for j in range(dlen))
#     input = str(dtstr) + '::' + str(login) + '@' + str(dom) + '.' + str(choice(tlds)) + '::' + str(dtint) + '-' + str(llen) + '-' + str(dlen)
#     f.write(input + '\n')

# 判断在redata.tex中一周的每一天出现的次数
# （换句话说，读者也可以计算所选择的年份中每个月中出现的次数）。

week_list = []
month_list = []

with open("redata.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        week_list.append(line.split(" ")[0])
        month_list.append(line.split(" ")[1])
week_list_count = set(week_list)
month_list_count = set(month_list)

for week in week_list_count:
    print("{} appers {} times".format(week, week_list.count(week)))

for month in month_list_count:
    print("{} appers {} times".format(month, month_list.count(month)))




# 将匹配的数字乘以 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?\d+)', "*", s))