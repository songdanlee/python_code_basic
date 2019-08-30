# 1.基于闭包的创建原则，创建一个闭包

def funOut(func):
    print("start")

    def funInner():
        print("我执行了")
        func()

    return funInner


@funOut
def func():
    print("hello")


# func()
# 2.使用两种方式，创建生成器，可以生产10以内所有的偶数
g1 = (x for x in range(0, 11) if x % 2 == 0)


# for i in g1:
# #     print(i)
def odd():
    for i in range(11):
        if i % 2 == 0:
            yield i


# g = odd()
# for i in g:
#     print(i)

# 3.有两个任务，任务1,无限生产，任务2，无限消费，要求两个任务无限交替执行(使用yield实现)
import time


def consume():
    while True:
        print("生产")
        yield 1


def produce():
    while True:
        print("消费")
        yield 2


def test():
    c = consume()
    p = produce()
    while True:
        next(c)
        time.sleep(0.5)
        next(p)


# 4.封装一个函数，可以求斐波那契数列的第n个数(查资料了解斐波那契数列,可以用循环或者递归的方式实现)
# 例如：print(fibo(6))  可以打印出斐波那契数列中的第6个数字 '8'
def fibo(num):
    if num <= 2 or num == 1:
        return 1
    else:
        return fibo(num - 1) + fibo(num - 2)


def fibo2(num):
    a = b = 1
    if num <= 2 or num == 1:
        return 1
    else:
        while num > 2:
            a, b = b, a + b
            num -= 1
    return b


# print(fibo2(6))

# 5.有一个模拟下载任务的功能，要求实现在不修改该功能源码的前提下，
# 新增日志功能(要求日志功能中，记录访问时间，以及访问的方法名,使用通用装饰器实现)


def log(func):
    def inner():
        with open("log.properties", mode="a", encoding="utf-8") as f:
            t = time.strftime("%Y-%M-%d %H-%m-%S")

            f.write(f"访问时间:{t},\t 访问方法：{func.__name__} \n")
        func()

    return inner


@log
def download():
    print("下载中请等待")

print(time.strftime("%Y-%M-%d %H-%m-%S"))
# download()


# 6.基于模拟Range实现的IntegRange，封装一个类，可以通过for循环直接打印指定范围的质数
# 例如:
# for i in IntegerRange(2,20,1):
# 	print(i)
# 可以依次打印出2,3,5,7,11...等全为质数的数字，
import math


class IntegerRange:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step
    #
    def __iter__(self):
        while self.start < self.end:
            if self.prime(self.start):
                yield self.start
            self.start += self.step

    def prime(self, n):
        if n <= 1:
            return 0
        for i in range(2, math.ceil(math.sqrt(n + 1))):
            if n % i == 0:
                return 0
        return 1


g = IntegerRange(1, 30, 3)

for i in g:
    print(i)


