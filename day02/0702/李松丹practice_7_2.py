# 猜拳 0剪刀  1石头  2布
import random
#
#
# count = 3
# while count >= 1:
#     guess_num = random.randint(0, 2)
#     num = int(input("请输入你要猜什么？ 0剪刀  1石头  2布:"))
#     if num == guess_num:
#         print("平局")
#     elif (num == 0  and guess_num == 1) or (num == 1 and guess_num == 2) or(num == 2 and guess_num == 0):
#         print("你输了,你还有%d次机会" % (count - 1))
#         print(guess_num, num)
#     else:
#         print("你赢了")
#         break
#     count -= 1


level = int(input(("请输入游戏难度：0 入门 1 简单 2 困难 3 末日")))

left = 1
right = 1
if level == 0:
    right = 20
elif level == 1:
    right = 50
elif level == 2:
    right = 100
else:
    right = 10000

guess = random.randint(left, right)
# print(guess)
for i in range(1, 6):
    num = int(input("第{}次输入,请输入要猜的数，范围是{}到{}".format(i,left, right)))
    if guess == num:
        print("猜对了")
        break
    elif num > guess:
        right = num
        print("猜大了")
    else:
        left = num
        print("猜小了")
else:
    print("你输了")
