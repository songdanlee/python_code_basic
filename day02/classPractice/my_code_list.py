classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(classmates[0])
print(classmates[1])
classmates.append('jerry')
print(classmates[2])
print(classmates[3])

li = [0,1,2]
print(li[2])
# apppend 列表追加元素到尾部
li.append(3)
print(li[3])
# index ，列表元素索引
print(li.index(2))
print("#"*19)
# insert,把元素插入到指定位置，
li.insert(1,'11-22') # 把 '11-22' 插入到索引为1的位置
print(type(li[1]))
# pop ，删除尾部元素,也可以指定删除索引位置，
li.pop(0)
print(li[0])


# sort 排序，默认升序，reverse=True 加上为倒序
# li.sort(reverse=True)
# for l in li:
#     print(l)

