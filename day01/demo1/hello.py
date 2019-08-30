# num = int(input("请输入数字:"))


#输入三角形的三个边长，计算三角形的周长，
# 先要判断三个数是否满足三角形的三边
# a = float(input("请输入边长a\n"))
# b = float(input("请输入边长b\n"))
# c = float(input("请输入边长c\n"))
#
# if (a + b) > c and (b + a) > c and (a + c) > b:
#     print(a+b+c)
# else:
#     print("不符合三角形")
#打印2-100的所有质数

def prime(num):
    if num == 1:
        return 0
    for i in range(2,num):
        if num % i == 0:
            return 0
    else:
	    return 1
count = 0
for i in range(2,101):
    if(prime(i)):
        count += 1
        print(i,end='\t')
    if(count % 10 == 0):
        count = 0
        print()
'''
一次输入一些数字，判断这些数字的最大值和最小值
'''
def findnum(*args):
    maxnum = 0
    minnum = 99999
    for i  in args:
        if i > maxnum:
            maxnum = i
        if minnum > i:
            minnum = i

    return maxnum,minnum


#print(findnum(10, 202, 40, 60, 1, -1, 999))

"""
'''
打印如下图所示的图形
   *
  ***
 *****
*******
 *****
  ***
   *
   1,3,5,7
   3 2 1 0
   5,3,1
   1,2,3
'''
"""
print()
for i in range(1,8,2):
    print(" "*((7-i)//2),end="")
    print("*"*i)
for i in  range(1,4):
    print(" "*i,end="")
    print("*"*(7-i-i))
## 输入一些数字，求出这些数字的平均数
def avg(*numbers):
    sum = 0.0
    for i in numbers:
        sum+=i
    sum /= len(numbers)
    return sum
print(avg(1,2,3,4,5,6,7,8,9))

'''
猜拳游戏
'''
import random

while True:
    num = int(input("请输入石头剪刀布，石头1，剪刀2，布3,退出0\n"))
    if num == 0:
        break
    guessnum = random.randint(1,3)
    if num == guessnum:
        print("平手")
    elif num == 1:
        if guessnum==3:
            print("你输了")
        else:
            print("你赢了")
    elif num == 2:
        if guessnum==1:
            print("你输了")
        else:
            print("你赢了")
    elif num == 3:
        if guessnum == 2:
            print("你输了")
        else:
            print("你赢了")
    print("机器",guessnum,"你",num)
