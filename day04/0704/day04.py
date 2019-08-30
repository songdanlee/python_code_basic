name_list = ['tom', 'jreey', 'marry']
name_list.append("morty")
print(name_list)

name_list.insert(1, "jenny")
print(name_list)

name_list.extend("rick")
print(name_list)

name_list.extend(['awsl', '摸鱼', '诡术', [1, 2, 3, 4]])
print(name_list)

name_list.pop()
print(name_list)
name_list.pop(5)
print(name_list)
name_list.remove('i')
print(name_list)
del name_list[5]
print(name_list)

name_list[5] = 'IU'
print(name_list)

# name_list.sort(reverse=False,key=lambda x:x.lower())
new_list = sorted(name_list, reverse=False, key=lambda x: x.lower())
print(name_list)
print(new_list)

new_list = []
new_list.append("张三")
new_list.append("李四")
new_list.append("王五")
new_list.append("张三")
new_list.append("张三")
print(new_list)
print(new_list.count("张三"))
print(new_list.index("张三", -2, -1))

# for i,j in enumerate(new_list):
#     print(i,j)

# 浅拷贝
list1 = [1, 2, 3, 4, 5, [7, 8, 9]]
list2 = list1.copy()
list1[0] = 'a'
print(list1)
print(list2)
print("-----------" * 18)
list1[5][0] = 'b'
print(list1)
print(list2)

import copy

# 深复制
print("*" * 20)
list1 = [1, 2, 3, 4, 5, [[2, 3], 8, 9]]
list2 = copy.deepcopy(list1)
list1[5][0][0] = 'b'
print(list1)
print(list2)

# 元组
# 定义一个元素的tu
tu = (1,)
print(type(tu))
tu = (1, 2, 3, 4, 5, 6, 7, 8, 17)
for i in tu:
    print(i)
# 元组求和
from functools import reduce

sumN = reduce(lambda x, y: x + y, tu)
print("sumN", sumN)

# ：输出元组内7的倍数及个位为7的数
res = list(filter(lambda x: x % 7 == 0 or x % 10 == 7, tu))
print(res)


def odd_num(num):
    return num % 2 == 0


# 输出元组内奇偶数的个数
odd_list = list(filter(odd_num, tu))
print(odd_list)
print(len(odd_list))
# 输出元组的最大值最小值
b = (20, 1, 3, 4, 8, 9, 5, 6)
print("max", max(b))
print("min", min(b))
# enumerate 返回索引，和对应的值组成的元组
for i in enumerate(tu):
    print(i)

tu = ('张三', '李四', '王五', '赵柳', '李四', '王五', '赵柳')
print(tu.count('王五'))
print(tu.index("王五", 4, 6))

tu = (1, 2, 3, 4, 5, 6, 7, 8, 17, 14)
# ：输出元组内7的倍数及个位为7的数
res = list(filter(lambda x: x % 7 == 0 or x % 10 == 7, tu))
print(res)
# 判断字符串是否是合法的变量名
# 字母数字下划线组成，数字不能开头
v = '_'
import re
import keyword

resu = re.fullmatch("[a-zA-Z\_][\w]*", v)
if resu is not None and v not in keyword.kwlist:
    print("变量合法")
else:
    print("不合法")

# 3、输出元组内最大值和最小值及其下标
tup = (1, 2, 3, 4, 5, 88, 56, 77)
minnum = tu[0]
maxnum = tu[0]
maxindex = 0
minindex = 0
for index, value in enumerate(tup):
    if value > maxnum:
        maxindex = index
        maxnum = value
    if value < minnum:
        minindex = index
        minindex = value
print("最小值", minindex, minnum)
print("最大值", maxindex, maxnum)
# 4、列表元素求和
from functools import reduce

sumN = reduce(lambda x, y: x + y, tup)
print("sumN", sumN)

s = "_"
if s[0].isdigit():
    print("变量名不合法，以数字开头")
else:
    for i in s:
        if not i.isalnum() and i != '_':
            print("变量名不合法，包含非法字符")
            break
    else:
        print("变量名合法")
dic = {"abc":18,"adc":19,"abe":20}
# 默认对键排序，从小到大，返回排序后键组成的列表
zidian = sorted(dic)#['abc', 'abe', 'adc']
print(zidian)
# 对键进行反向（从大到小）排序
zidian = sorted(dic,reverse=True)#['adc', 'abe', 'abc']
print(zidian)
# 拿到所有的key，然后再对key排序
zidian = sorted(dic.keys(),reverse=True)#['adc', 'abe', 'abc']
print(zidian)
# 对值排序，从小到大
print(dic)
zidian = sorted(dic.values())#[18, 19, 20]
print(zidian)
# 对值排序，从大到小
zidian = sorted(dic.values(),reverse=True)#[20, 19, 18]
print(zidian)
#可以用dict1.items()，得到包含键，值的元组,
# 由于迭代对象是元组，返回值自然是元组组成的列表,x指元组，x[1]是值，x[0]是键

# 键由小到大排序
zidian = sorted(dic.items(),key=lambda x:x[0])
print(zidian)

# 键由大到小排序
zidian = sorted(dic.items(),key=lambda x:x[0],reverse=True)
print(zidian)

# 值由小到大排序
zidian = sorted(dic.items(),key=lambda x:x[1])
print(zidian)
# 值由大到小排序
zidian = sorted(dic.items(),key=lambda x:x[1],reverse=True)
print(zidian)

#itemgetter(0)，获取key
# itemgetter(1)，获取value
from operator import itemgetter
d = {"a":8,"b":4,"c":12,"a":10,"b":1,"e":10}
# 键由大到小
print(sorted(d.items(),key=itemgetter(0),reverse=True))#[('e', 10), ('c', 12), ('b', 1), ('a', 10)]
# 值由大到小
print(sorted(d.items(),key=itemgetter(1),reverse=True))#[('c', 12), ('a', 10), ('e', 10), ('b', 1)]
