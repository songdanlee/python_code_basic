"""
迭代：
迭代是访问集合元素的一种方式，可以将某个数据集内的数据“一个挨着一个的取出来”，就叫做迭代
可迭代协议

1.可迭代性(Iterable)
    具备可迭代性的元素，才可以使用for循环进行遍历
    只要一个类实现了可迭代性协议(实现了__iter__这个方法)，那么这个对象就具备可迭代性
    for 临时变量 in Iterable:

    str,tuple,list,dict,set

    如果判断某个对象是否具备可迭代性
    1.判断是否包含__iter__方法
    2.isinstance,Iterable

2.迭代器 Iterator
    迭代器协议
    拥有__iter__方法和__next__方法的对象就是迭代器

    思考？
        具备可迭代性的元素，是否一定是迭代器对象？
        不一定
        生成器对象是否是迭代器对象？
        一定是

    如何一个对象是否为迭代器对象？
        1.判断是否包含__iter__,__next__
        2.isinstance Iterator
"""

from collections.abc import Iterable
from collections.abc import Iterator

a = 123
b = '123'
d = dict(a=1,b=2)
print('__iter__' in dir(a))
print('__iter__' in dir(b))

print(isinstance(a,Iterable))
print(isinstance(b,Iterable))
print(isinstance(d,Iterable))

list1 = [1,2,3]
d = {'a':1,'c':2}

print("__iter__" in dir(list) and "__next__"in dir(list))
print(isinstance(list1,Iterator))
print(isinstance(d,Iterator))

v = d.keys()
print(isinstance(v,Iterable))
print(isinstance(v,Iterator))