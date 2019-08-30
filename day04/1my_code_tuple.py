# 元组内元素不可变，也是有序序列
# 格式 t = ()
# 如果元组中只有一个元素,后面要加','


# 元组操作 可以连接，重复，索引，切片，遍历
t = (1, 2, 3, 4)
# print(t * 2)
# print(t, type(t))
#
# t2 = ('a','b','c','d')
# res = t + t2
# print(res)
#
# print(res[0])
# print(res[-1])
#
# print(res[::-1])

# 遍历元组
# for i in t:
#     print(i)
# 求元组数字和
sum1 = 0
for i in t:
    sum1 += i
print(sum1)

# tuple() 函数,
#re = tuple("你还好吗") #将字符串转成元组
re = tuple([1,2,3,4,5,6,7,2,2,2,2,2])#将列表转为元组
print(re)
# count(元素) 统计元素的个数
print(re.count(2))

# 获取指定元素的下标(就近原则，从左往右，找到第一个就结束)
# 　　index(self, value, start=None, stop=None)
# 参数:value:待查询下标的元素   start:查询起始下标  stop：查询终止下标(查询到stop前一个下标)
print(re.index(2,3))
# tuple 转字符串，元素必须都是字符串
tup = ("abc","efg","hij","klm")
print(" ".join(tup))

tup1 = (1, 2, ['a', 'b', 'c'])
tup1[2].append(1)
print(tup1[2])


# len 获取元组 列表  字符串的长度
print(len(tup1))
print(len("abcdref"))

# 如果元组中只有一个元素
tup2 = (1,)
print(type(tup2))
