names = {"Michael":95,"BOb":67,"Tracy":85}

print(names['Michael'])

names['Michael'] = 100
print(names['Michael'])


print("Michael" in names)
# get 查询指定的key，是否存在，不存在返回None,也可以指定返回的value
print(names.get("Michae",-1))
# pop 删除一个key ，对应的value也会删除
names.pop("Michael")
print("Michael" in names)
"""
和list比较，dict有以下几个特点：
查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。
"""
# set 没有重复的元素
print("*"*20)
s = set([1,2,3])
print(s)
# add，可以把元素添加到set
s.add(3)
print(s)
# remove ，删除元素
s.remove(2)
print(s)