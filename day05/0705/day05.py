user_info = {

    "name": "张三",
    True: "这可以",
    1.43: "浮点型",
    2: "整形",
    (1, 2, 3): (3, 4, 5, 6, 7)

}
print(user_info)

# user = dict(name="张三",age=18)
user = dict()
user['name'] = '张三'
user['age'] = 13
user.setdefault("weight", 120)
user.update(name="装神弄鬼")
user.update({'name': "李四", "height": 14})
print(user)

print("name" in user)
print("李四" in user.values())

pop_val = user.pop("name")
print(pop_val)
print(user.get("name"))
print(user.get("name1", "zhngsan"))

for key in user.keys():
    print(key)
for value in user.values():
    print(value)
for key, value in user.items():
    print(key, value)
print(len(user))

di = dict.fromkeys(('name', 'age', 'weight'), 1)
print(di)

sets = {'a'}
sets.add("a")
print(sets)
sets.update({"张安", "李思", "王武"})
print(sets)
# 随机删
# print(sets.pop())
sets.remove("王武")
print(sets)
sets.discard("账上")
print(sets)

set1 = {1, 2, 3, 4, 5, 6}
set2 = {2, 3, 7, 8, 9}
# 交集
print(set1 & set2)
print(set1.intersection(set2))
# 并集
print(set1 | set2)
print(set1.union(set2))
# 差集
print(set1.difference(set2))
print(set1 - set2)
# 反交集
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

set3 = {1, 2, 3, 900}
set4 = {1, 2, 3, 4, 5, 6, 7, 8}

print(set3.issubset(set4))
print(set4.issuperset(set3))
print(set4 ^ set3)

# set4中去除和set3重复的
set4.difference_update(set3)
print(set4)


def func(num):
    return num % 2 == 0


# 编写函数 实现 根据输入的数值 打印 几乘几的正方体
def print_func(num):
    for i in range(num):
        print(" * " * num)


# print_func(10)


# 编写函数 实现 根据输入年份判断该年份是否是闰年
def isLeapYear(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


# year = input("请输入年份")
# if year.isdigit():
#     print(isLeapYear(int(year)))
# else:
#     print("格式非法")

def fun_shunxu(a, b, c, d=10):
    print("a:%s,b:%s,c:%s,d:%s" % (a, b, c, d))


# fun_shunxu(10, 2, 3)
# fun_shunxu(10, 2, 3, 15)


def func_keyword(name, age, weight):
    print("name{},age{},weight{}".format(name, age, weight))


# func_keyword(age=19, name="詹少干", weight="128")


def func_args(*args, name="zhangsan1", **kwargs):
    print(args)
    print(name)
    print("kwargs", kwargs)


# func_args(1, 2, 3, 4, 5, 6, 7, 9, name="李思", age=19, sof=120)
#

# 1.定义一个函数，传入两个参数，计算两个参数的和并返回，调用函数并输出函数返回值
def sum2Num(num1, num2):
    return num1 + num2


sum2Num(10, 20)


# 2.定义函数compare(arg1,arg2) 比较两个参数大小，如果arg1>arg2返回True 否则返回False
# 调用函数compare，返回True输出‘大于’，返回False输出‘小于’
def compare(num1, num2):
    return num1 > num2


print("大于") if compare(10, 20) else print("小于")


# 3.定义一个函数，该函数接收两个参数num和num1
# 如果num1==0返回False否者计算num*num1 和 num/num1的结果并返回
def jisuan(num, num1):
    if num1 == 0:
        return False
    return num * num1, num / num1


res = jisuan(10, 2)
print(res)

# 4.定义函数，实现根据传入参数的判断是否是质数
import math


def isprime(num):
    if num == 1:
        return False
    for i in range(2,math.ceil(math.sqrt(num+1))):
        if num % i == 0:
            return False
    return True


for j in range(1, 102):
    if isprime(j):
        print(j, end=" ")

print()
def primeN(num):
    li = []
    if num>=2:
        li.append(2)
    for j in range(3,num+1,2):
        if isprime(j):

            li.append(j)
    return li
print(primeN(101))


def jiecheng(num):
    if num == 1:
        return 1
    return num*jiecheng(num-1)
print(jiecheng(5))


aa = 1
def ss():
    global aa
    aa=2
ss()
print(aa)


dic = {'id': '1002', 'name': '张三', 'age': 12, 'height': 189, 'sex': '男'}
dic1 = {'id': '1002', 'name': '张三', 'age': 12, 'height': 189, 'sex': '男'}
print(dic==dic1)