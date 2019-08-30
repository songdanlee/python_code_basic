# num = 1
# while num <= 10:
#     j = 1
#     while j <= 10:
#         if num == 1 or num == 10:
#             print(" * ", end="")
#         else:
#             print(" * ", end="")
#             print(" . " * 8, end="")
#             print(" * ", end="")
#             break
#         j += 1
#     print()
#     num += 1
# print("---------------------------------")
# for i in range(1, 11):
#     for j in range(1, 11):
#         if i == 1 or i == 10:
#             print(" *  *  *  *  *  *  *  *  *  * ", end="")
#             break
#         elif i == j or j == 1 or j == 10 or (i + j == 11):
#             print(" * ", end="")
#         elif i <= j and j + i >= 11:
#             print(" $ ", end="")
#         else:
#             print("   ", end="")
#     print()
#
# for i in range(9, 0, -1):
#     for k in range(0, 9 - i):
#         print("    ", end="\t")
#     for j in range(1, i + 1):
#         print("{}*{}={:02d}".format(i, j, i * j), end="\t")
#     print()
#
#
# count = 0
# flag = 0
# password = input("您还有%s次机会，请输入密码:" % (3 - count))
# while count <= 2:
#     if password != "111111":
#         print("密码输入错误")
#         count += 1
#         if 3 > count:
#             password = input("您还有%s次机会，请输入密码:" % (3 - count))
#     if password == '111111':
#         money = int(input("请输入取款金额，100的整数倍1:"))
#         if money % 100 == 0 and money != 0 and money <= 20000:
#             print("取款成功，请取卡，拜了个拜")
#             flag = 1
#             break
#         else:
#             print("金额格式有误，请重新输入金额(100的整数倍,且小于20000)")
#     if flag:
#         break
# else:
#     print("机会用完啦，请想一想正确的密码吧")
# 练习4、编写猜大小游戏
# 要求：
# (1)有三个骰子，每个骰子最大六点，随机生成三个筛子数
# (2)三个骰子数之和大于9为大，否则为小
# (3)用户有100个初始金币
# (4)让用户猜大小，猜中金币数+10，猜错金币数-10 金币为0退出程序

# import random
#
#
# coin = 100
# while coin:
#     randnum = random.randint(1, 18)
#     flag = 0
#     if randnum > 9:
#         flag = 1
#     # print(randnum,flag)
#     num = int(input("请输入猜大猜小，0 小 ，1  大:  2 退出"))
#     if num == 2:
#         break
#     if num == flag:
#         coin += 10
#         print("猜对了，你还有金币%d"%coin)
#     else:
#         coin -=10
#         print("猜错了，你还有金币%d" % coin)

# 练习5、输出100以内所有的质数
import math


def prime(n):
    if n == 1:
        return 0
    for i in range(2, math.ceil(math.sqrt(n + 1))):
        if n % i == 0:
            return 0
    return 1


print(2, end="\t")
for i in range(3, 100, 2):
    if prime(i):
        print(i, end="\t")
