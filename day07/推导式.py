"""
推导式（解析式）：
语法：
变量名=[表达式 for 变量 in 列表]
或者变量名= [表达式 for 变量 in 列表 if 条件]
语义：遍历出列表中的内容给变量，表达式根据变量值进行逻辑运算。或者遍历列表中的内容给变量，然后进行判断，符合的值在给表达式。
好处：
    效率高

练习1：快速创建一个包含元素1-10的列表
练习2：快速创建一个包含1-10之间所有偶数的列表
练习3：现在有一列表 lst = [[1,2,3],[4,5,6],[7,8,9]]要求出 1/4/7 和 1/5/9 元素， 思考如何取出

推导式的分类：
    1.列表推导式
    2.字典推导式
    3.集合推导式
"""
import time

start_time = time.time()  # 获取系统当前时间
# 快速创建包含元素1-10的列表
list1 = [i if i % 2==0 else i+2 for i in range(1, 11)]
print(list1)
end_time = time.time()
print(f"耗时多少秒{end_time - start_time}")
# print(list1)

# 快速创建包含1-10之间所有的偶数列表
list2 = [x for x in range(1, 11) if x % 2 == 0]
print(list2)

# # 练习3：现在有一列表 lst = [[1,2,3],[4,5,6],[7,8,9]]要求出 1/4/7 和 1/5/9 元素， 思考如何取出
list4 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list3 = [x[0] for x in list4]
print(list3)
list3 = [list4[i][0] for i in range(len(list4))]
print(list3)
list3 = [list4[i][i] for i in range(len(list4))]
print(list3)

a = [lambda x: x * i for i in range(3)]
print(a[0](1))
#
# def func():
#     fun_lambda_list = []
#     for i in range(4):
#
#         def lambda_(x):
#             print('Lambda函数中 i {} 命名空间为：{}:'.format(i, locals()))
#             return x*i
#         fun_lambda_list.append(lambda_)
#         print('外层函数 I 为：{} 命名空间为:{}'.format(i, locals()))
#
#     return fun_lambda_list
#
# fl = func()
# fl[0](1)
# fl[1](2)
# fl[2](1)
# fl[3](1)


lis = [x for x in range(1,11) if x % 2==0]
print(lis)

lst = [[1,2,3],[4,5,6],[7,8,9]]

lst1=[lst[i][i] for i in range(len(lst))]
print(lst1)

print("0123a4523".rfind("23",1))

sets = {'a','v','a','a','b','c','d','a','b'}

for i in enumerate(sets):
    print(i)

def fun1(**kwargs):
    print(kwargs)

def fun1(**kwargs):
    print(kwargs)

d = {'a': 1, 'b': 2}
fun1(a=1, b=2)
fun1(**d)