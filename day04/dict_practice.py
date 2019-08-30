dic = {'name':'张三','age':18,'sex':1,'phone':'13090807060'}

# 索引值
print(dic['name'])
print(dic.get('sex',0))

# 添加/修改
dic['name'] = '李四'
print(dic)
dic.setdefault('addr','beijing')
dic.setdefault('addr','shanghai')
#删除
dic.pop('sex')
print(dic)
dic['acd']='123'
dic.popitem()
print(dic)

# 遍历
for i in dic.keys():
    print(i,dic.get(i))
for v in dic.values():
    print(v)

for k,v in dic.items():
    print(k,v)

# 清空
dic.clear()
print(dic)
# del dic