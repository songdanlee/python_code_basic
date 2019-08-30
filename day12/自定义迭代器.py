from collections.abc import Iterator, Iterable


class func(object):
    def __init__(self):
        self.name = []
        self.position = 0  # 这个是记录迭代的位置，默认从第一个开始，初始值为0

    # 取得迭代器
    def __iter__(self):
        """返回一个迭代器"""
        return self

    def __next__(self):
        """返回迭代器下一个指向的值"""
        if self.position < len(self.name):  # 判断当前的位置是否跟总的长度相等，

            item = self.name[self.position]
            self.position += 1
            return item
        else:
            raise StopIteration

    def add(self, name):
        self.name.append(name)


# 创建对象
s1 = func()
s1.add("aaaa")
s1.add("dddd")
s1.add("vvvv")
s1.add("aaaas")

# 是否为可迭代对象：True
print("是否为可迭代对象：%s" % isinstance(s1, Iterable))
# 这时候遍历对象发现报错，原因是在这个类中没有写__next__方法，这个类只是有了迭代器，
# 但并不是很完善
for item in s1:
    print(item)

import math


class IntegerRange:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        while self.start < self.end:
            self.start += self.step
            if self.prime(self.start):
                return self.start
        else:
            raise StopIteration("跑完了")

    def prime(self, n):
        if n <= 1:
            return 0
        for i in range(2, math.ceil(math.sqrt(n + 1))):
            if n % i == 0:
                return 0
        return 1
g = IntegerRange(2,20,1)
print(g.__next__())
print(next(g))
# for i in g:
#     print(i)
#
# def prime(n):
#     if n <= 1:
#         return 0
#     for i in range(2, math.ceil(math.sqrt(n + 1))):
#         if n % i == 0:
#             return 0
#     return 1
#
#
# def Prime(n):
#     st = 2
#     while n:
#         if prime(st):
#             yield st
#             n -= 1
#         st += 1
#
# for i in Prime(10):
#     print(i)
