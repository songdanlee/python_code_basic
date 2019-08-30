"""
生成器:generator
    一边循环一边计算的机制， 称为生成器

    Python2很多列表的地方，在Python3被更新为生成器

    可以基于生成器直接创建列表

    filter
    map

    1、如何创建生成器?
        1.1  g1 = (x for x in range(10) if x % 2 == 0)
        1.2  g2 = func1()
            函数func1中必须包含yield关键字
    2、如何生成数据?（下蛋的鸡）
        特征：
        2.1 必须先生第一个，才能生第二个
        2.2 必须是一个一个来
        生成语法：
        a.next(g)
        b.g.__next__()
        c.g.send(value)
            value 在生成器开始的时候，只能给None
            后续可以给随意参数
    如果超出生成数据范围，会导致异常  StopIteration

    3、生成器的好处?
        3.1 时间开销

        3.2 内存开销

"""


lis = [1,2,3,4,5,6,7]
lis1 = [2,3,4,5,6,7,8]
li = list(map(lambda x,y:x,lis,lis1))
for i in li:
    print(i)


g2 = (x for x in range(10) if x % 2 == 0)
print(type(g2))
# 3种使用方式
v = next(g2)
print(v)
v = g2.__next__()
print(v)
v = g2.send(None)
print(v)



import time
import sys
"""
1M = 1024kb
1kb = 1024byte
1byte = 8bit
"""
start = time.time()
# list1 = [x for x in range(10000000)]
list1 = (x for x in range(10000000))
size = sys.getsizeof(list1)#字节
end = time.time()
print(f'耗时:{end-start}秒')
print(f'list1占用内存{size/1024}kb')
# print(f'list1占用内存{size/1024/1024}M')

