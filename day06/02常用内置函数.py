"""
什么是内置函数?
    内置模块中的函数，可以直接使用(不要导入任何东西)，就称为内置函数
内键模块(builtins.py),系统默认导入

如何查看模块中包含的东西？
1.官方文档
2.dir(模块)

常见内键函数使用
abs()
max()
min()
map()
filter()
查看文档:
    1.函数大致语义
    2.函数要不要参数
    3.函数返回值


"""
import builtins

v = dir(builtins)
print(type(v))

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]


def get_sum(a, b):
    return a + b


res = map(get_sum, list1, list2)
for i in res:
    print(i)


def func1(x):
    return x ** 2


res = map(func1, list1)
for i in res:
    print(i)


# filter
# 用于过滤序列，过滤掉不符合条件的元素，返回符合条件元素组成新的列表（迭代器）

# s是否是偶数
def func2(x):
    return x % 2 == 0
v = filter(func2,[1,2,3,4,5,6,7,8])
for i in v :
    print(i,end=" ")

# zip() , 传入可迭代序列，返回每个序列，对应索引(以短的为主)组成的元组
# zip("1234","abc") ----> (1,a)  (2,b)   (3,c)
list3 = [3,4,5,6,7,8,9,10]
s3="abcdef"
s1="hij"

for i in zip(list3,s3,s1):
    print(i)

