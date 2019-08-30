"""
列表
 格式
    name =[值1，值2，值3]
 列表可以循环遍历，可以重复，可以+拼接，还可以做索引操作 切片
"""

name1 = ['王宝强','陈羽凡','贾乃亮']
name2 = ['盖伦','嘉文','赵信']
#
res = name1 + name2
print(res)

res = name2 * 3
print(res)

#遍历元素
for i in res:
    print(i)
# 索引获取值，索引从0开始
# 索引为负值，表示取倒数第几个，超出个数会报错

print(res[0])
print(res[-1])

names = ['1','2','3','4','5','6']
#切片
#range(start,end,step)
# 从第一个索引取到6-1 的索引位置，如果超出，取出所有
print(names[0:6])
print(names[0:6:2])
# 默认从第一个取到最后一个，跳步值默认为1，，隔了step-1取
print(names[::2])
# 从头开始取到倒数第几个，返回新列表
print(names[:-2])
print(names[-1:-3:-1])
# 倒序
print(names[::-1])
# 从头取到最后
print(names[:-1])
# 取到倒数第一个
print(names[-1:])
# 取[6,5]
print(names[:-3:-1])

print(names[::])
print(names[::2])
print(names[-1:-3:-1])
print(names[:-3:1])

#列表操作
#添加 append
list1 = ['a','b','c']
list1 .append('d')
print(list1)

# 在指定位置插入一个元素
list1.insert(1,'A')
print(list1)

#删除元素
# pop不传参数时，默认弹出最后一个元素，并返回
# pop(2) 弹出索引值为2的元素，
res = list1.pop()
print(res)
print(list1)
res = list1.pop(1)
print(res)
print(list1)

#修改列表中的元素
list1[0]='A'
print(list1)

#del  python 的方法，python删除数据
del list1[0]
print(list1)

aList = [123, 'xyz', 'zara', 'abc', 123];
bList = [2009, 'manni'];
aList.extend(bList)
print(aList)