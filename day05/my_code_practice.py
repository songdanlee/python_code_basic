class Mynumber:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = Mynumber()
myiter = iter(myclass)

# print(next(myclass))
# print(next(myclass))
# -*- coding: utf-8 -*-
def findMinAndMax(L):
    if len(L) is 0:
        return None,None
    maxnum = -99999
    minnum = 999999
    for i in L:
        if maxnum < i:
            maxnum = i
        if minnum > i:
            minnum = i
    return minnum,maxnum


L1 = ['Hello', 'World', 18, 'Apple', None]

#print([s.lower() for s in L1 if isinstance(s, str)])

a = [1, 2, 3, 4, 5]
b = ["a", "b", "c", "d", "e"]


c = [str(x) + str(y) for x,y in zip(b,a)]
# print(c)


# 例2
# 自定义一个生成器
def genter():
    a = 4
    b = 5
    c = 6
    for i in range(5):
        yield a
        print('hhh'+str(i))
        yield b
        print("aaa" + str(i))
        yield c

# 包含了yield 的 genter() 就是一个生成器
res = genter()
# print(next(res))
# print(next(res))


def story(**kwds):
    return 'Once upon a time, there was a ' \
        '{job} called {name}.'.format_map(kwds)
def power(x, y, *others):
    if others:
        print('Received redundant parameters:', others)
    return pow(x, y)
def interval(start, stop=None, step=1):
    'Imitates range() for step > 0'
    if stop is None: # 如果没有给参数stop指定值，
        start, stop = 0, start  # 就调整参数start和stop的值
    result = []
    i = start # 从start开始往上数
    while i < stop: # 数到stop位置
        result.append(i)  # 将当前数的数附加到result末尾
        i += step # 增加到当前数和step（> 0）之和
    return result
# print(story(job='king', name='Gumby'))
# print(story(name='Sir Robin', job='brave knight'))
params = {'job': 'language', 'name': 'Python'}
# print(story(**params))
# del params['job']
# print(story(job='stroke of genius', **params))
# print(power(2, 3))
# params = (5,) * 2
# print(params)
# print(power(*params))
power(3, 3, 'Hello, world')
print(interval(3, 7))
power(*interval(3, 7))

print("1","2","3",sep="-")


