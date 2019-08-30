# 迭代⼀个序列时，跟踪当前项的序号
# enumerate(可迭代序列),返回(索引值,对应值)的元组
some_list = ['foo', 'bar', 'baz']
mapping = {}
for i, v in enumerate(some_list):
    mapping[v] = i
print(mapping)  # {'foo': 0, 'bar': 1, 'baz': 2}

# sorted 函数排序
print(sorted([7, 1, 2, 6, 0, 3, 2]))  # [0, 1, 2, 2, 3, 6, 7]
print(sorted('horse race'))  # [' ', 'a', 'c', 'e', 'e', 'h', 'o', 'r', 'r', 's']

# zip可以将多个列表、元组或其它序列成对组合成⼀个元组列表
seq1 = ['foo', 'bar', 'baz']
seq2 = ['one', 'two', 'three']
zipped = zip(seq1, seq2)
print(list(zipped))  # [('foo', 'one'), ('bar', 'two'), ('baz', 'three')]
# zip 可以处理任意多的序列，元素的个数取决于最短的序列：
seq3 = [False, True]
print(list(zip(seq1, seq2, seq3)))  # [('foo', 'one', False), ('bar', 'two', True)]

# zip也可以用来解压序列，可以把行的列表转为列的列表。
pitchers = [('Nolan', 'Ryan'), ('Roger', 'Clemens'), ('Schilling', 'Curt')]
first_names, last_names = zip(*pitchers)
print(first_names)  # ('Nolan', 'Roger', 'Schilling')
print(last_names)  # ('Ryan', 'Clemens', 'Curt')

# reversed 可以从后向前迭代一个序列
#  reversed 是⼀个⽣成器，只有实体化（即列表或for循环）之后才能创建翻转的序列
print(list(reversed(range(10))))

di = {'foo': 0, 'bar': 1, 'baz': 2}
# di.pop("d")#键不存在，报错
di.get("id")#键不存在默认返回None，否则报错

# 你可以通过⾸字⺟，将⼀个列表中的单词分类
words = ['apple', 'bat', 'bar', 'atom']
by_letter = {}
# by_letter.setdefault("h", {}).update(hello="world")
# by_letter.setdefault("h", {}).update({"name":"zhsngsna"})
for word in words:
    letter = word[0]
    #apple的a不在字典中，向字典中插入{'a':[]}，并返回[]，然后更改字典的值，得到{'a': ['apple']}
    by_letter.setdefault(letter,[]).append(word)
print(by_letter)
# 利用defaultdict，简化上面程序
from collections import defaultdict
by_letter = defaultdict(list)
for word in words:
    by_letter[word[0]].append(word)
print(by_letter)

# 列表、集合和字典推导式
# # 列表推导式是Python最受喜爱的特性之⼀。它允许⽤户⽅便的从
# # ⼀个集合过滤元素，形成列表，在传递参数的过程中还可以修改
# # 元素。形式如下：
# # [expr for val in collection if condition]
# # 它等同于下⾯的for循环;
# result = []
# for val in collection:
#   if condition:
#       result.append(expr)

# filter条件可以被忽略，只留下表达式就⾏。例如，给定⼀个字符
# 串列表，我们可以过滤出长度在2及以上的字符串，并将其转换成⼤写：

strings = ['a', 'as', 'bat', 'car', 'dove']
print([s.upper() for s in strings if len(s) >= 2])
# 字典推导式 尖括号
# dict_comp = {key-expr : value-expr for value in collection if condition]
# 字典键为strings中元素，值为对应索引
loc_mapping = {val : index for index, val in enumerate(strings)}
print(loc_mapping) #{'a': 0, 'as': 1, 'bat': 2, 'car': 3, 'dove': 4}

# 集合的推导式 尖括号  set_comp = {expr for value in collection if condition]

# 嵌套列表推导式
all_data = [['John', 'Emily', 'Michael', 'Mary', 'Steven'],['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]
newlist=[name for names in all_data for name in names if len(name)>=6] #或者过滤名字中a出现多次的，name.count('a')>2
print(newlist)#['Michael', 'Steven', 'Javier', 'Natalia']

import re
def remove_punctuation(value):
    return re.sub("[!#?]","",value)

clean_ops = [str.strip,remove_punctuation,str.title]

def clean_strings(strings,ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result
states = [' Alabama ', '###Georgia!', 'Georg###ia',' Geor###gia ',' Flor????ida ','S outh!!!!! Carolina ','We###st Virginia ']
res = clean_strings(states,clean_ops)
# ['Alabama', 'Georgia', 'Georgia', 'Georgia', 'Florida', 'S Outh Carolina', 'West Virginia']
print(res)


# ⽣成器表达式
# 这是⼀种类似于列表、字典、集合
# 推导式的⽣成器。其创建⽅式为，把列表推导式两端的⽅括号改成圆括号

# gen = (x**2 for x in range(100))
# print(gen)
# for u in gen:
#     print(u)

import numpy as np
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
print(arr1)
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
print(arr2)

# 但 sorted()也是一个高阶函数，它可以接收一个比较函数来实现自定义排序，
# 比较函数的定义是，传入两个待比较的元素 x, y，
# 如果 x 应该排在 y 的前面，返回 -1，
# 如果 x 应该排在 y 的后面，返回 1。
# 如果 x 和 y 相等，返回 0

# def cmp_ignore_case(s1, s2):
#
#     if s1.lower()>s2.lower():
#         return 1
#     else :return -1
# print(sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case))

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1())

