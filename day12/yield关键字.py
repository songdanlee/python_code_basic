"""
1、g.send(value)
参数到底传递给谁了


2、yield另外的用法(协程)
    可以起到暂停作用

可以实现多任务并发执行

"""

def generator():
    print("a")
    count = yield 1
    print("---->", count)
    print('b')
    yield 2


g = generator()
print(next(g))

res = g.send('123')
print(res)
print("- -" * 10)

import time


def save():
    while True:
        print("保存")
        yield 1


def prin():
    while True:
        print("打印")
        yield 0


g = save()
g1 = prin()
while True:
    g.send(None)
    time.sleep(1)
    g1.send(None)
