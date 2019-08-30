# 1.封装函数，可以判断一个数字是否为偶数
def isEven(num):
    return num % 2 == 0


# 2.封装函数，可以实现1-n之间所有偶数的打印，每a个一行
def printEven(n, count):
    res = list(filter(isEven, range(1, n + 1)))
    cc = 0
    for i in res:
        print("%3d" % i, end=" ")
        cc += 1
        if cc == count:
            cc = 0
            print()


# 3.封装函数，可以找出整型列表中的最大值
def findMax(lis):
    max_num = lis[0]
    for value in lis:
        if value > max_num:
            max_num = value
    return max_num


# 4.封装函数，可以找出整型列表中的最大值的索引
def findMaxIndex(lis):
    max_num = lis[0]
    max_index = 0
    for index, value in enumerate(lis):
        if value > max_num:
            max_num, max_index = value, index
    return max_index


# 5.封装函数，可以找出整型列表中的最小值
def findMin(lis):
    return min(lis)


# 6.封装函数，可以找出整型列表中的最小值的索引
def findMinIndex(lis):
    min_index = 0
    for i in range(1,len(lis)):
        if lis[i] < lis[min_index]:
            min_index = i
    return min_index
print(findMinIndex([1,2,3,4,10,0,-1]))

# 7.封装函数，可以求任意多个数字的和,并返回这个和(参数可以使用*args)

def sumN(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


# 8.封装函数，判断一个数字是否为水仙花数
def check_Narcissus(num):
    tol = 0
    num1 = num
    length = len(str(num))
    if length < 3:
        return 0
    while (num1):
        tol += (num1 % 10) ** length
        num1 = num1 // 10
    if num == tol:
        return 1
    else:
        return 0


# if check_Narcissus(24678050):
#     print("是水仙花数")

# 9.封装函数，打印所有的水仙花数
def printNarcissus(num):
    for i in range(100, num + 1):
        if check_Narcissus(i):
            print(i, end=" ")
    print()

printNarcissus(10000)
# 10.封装函数，可以打印指定范围内所有的质数

import math

def checkPrime(num):
    if num == 1:
        return 0
    for i in range(2, math.ceil(math.sqrt(num + 1))):
        if num % i == 0:
            return 0
    return 1


def printPrimeN(num):
    if num >= 2:
        print(2, end=" ")
    for i in range(3, num + 1, 2):
        if checkPrime(i):
            print(i, end=" ")

# 字符串.isalnum()  所有字符都是数字或者字母，为真返回 Ture，否则返回 False。
# 字符串.isalpha()   所有字符都是字母，为真返回 Ture，否则返回 False。
# 字符串.isdigit()     所有字符都是数字，为真返回 Ture，否则返回 False。
# 字符串.islower()    所有字符都是小写，为真返回 Ture，否则返回 False。
# 字符串.isupper()   所有字符都是大写，为真返回 Ture，否则返回 False。
# 字符串.istitle()      所有单词都是首字母大写，为真返回 Ture，否则返回 False。
# 字符串.isspace()   所有字符都是空白字符，为真返回 Ture，否则返回 False。
# 11.封装函数，可以实现某个字符串的大小写转换，比如：输入'Abc' - > 'aBC'
def changeStr(orign_str):
    res_str = ""
    for  v in orign_str:
        if v.isupper():
            res_str += v.lower()
        elif v.lower():
            res_str += v.upper()
        else:
            res_str += v
    return res_str

print(changeStr("Abc"))


