# 字典 无序
dic = {"name": "张三", 'age':18, 'hobby':['sing', 'rap']}

# 获取字典的值
print(dic['name'])

# 遍历字典
for i in dic: # i 的值是键
    print(i, dic[i])
# 添加一个新的数据 , 如果指定的键已经存在做修改操作，如果不存在添加
dic['sex']= 'F'
print(dic)
dic.setdefault('phone', '15057890987')
print(dic)

dic['email']= '23@q97.com'
# 删除一个键 pop 弹出指定的键并返回弹出键对应的值
res = dic.pop('phone')
res = dic.pop('email', None)
print(res, dic)
# popitem 随机弹出一个键，返回一个有弹出键和值组成的元组
item = dic.popitem()
print(item)

# 清空字典 clear ,del 删除字典
# dic.clear()
print(dic)

# 查找  根据键去查找  注意：键不存在会报错
# print(dic['ss'])
# get 如果键不存在不会报错，返回None
#     同时可以指定一个默认值，如果没有指定的键就返回默认值
print(dic.get('name', 'zs'))
# keys() 返回字典所有键
keys = dic.keys()
print(type(keys))
# values() 返回所有的值
values = dic.values()
#返回所有的键和值
item = dic.items()
print(item)

print("---"*10)

for i in dic.keys():
    print(i)

for i in dic.values():
    print(i)

for i in dic.items():
    print(i)

for key,value in dic.items():
    print(key,value)

# 创建空字典
dic2 = dict()


dic3 = dict(name="zs",age=18,sex=0)
lis = [('name','zs'),('phone',17)]
dict4 = dict(lis)
print(dict4)
dic3.update(dict4)
print("-*"*20)
print(dic3)
print("-*"*20)

#解包
#a,b = [1,2]
a,b = ('a','b')
print(a,b)

# *item2 回收集剩下的所有元素，并组成列表进行返回
item1,*item2 = (1,2,3,4)
print(item1)
print(item2)

dict()
{'name':1,'age':19}
dict([('name','lisi'),('age',17)])
{x:x*2 for x in range(5)}
dict.fromkeys(range(5),'a')