# width = int(input('Please enter width: '))
# price_width = 10
# item_width = width - price_width
# header_fmt = '{{:{}}}{{:>{}}}'.format(item_width, price_width)#{:25}{:>10}
# fmt  = '{{:{}}}{{:>{}.2f}}'.format(item_width, price_width)#{:25}{:>10.2f}
# print(header_fmt)
# print(fmt.format('Apples',0.4))


# 浅拷贝 cpoy
#方法 copy 返回一个新字典，其包含的键值对与原来的字典相同
# （这个方法执行的是浅复制, 只拷贝父对象，不会拷贝对象的内部的子对象。
print("="*20)
print("浅拷贝")
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()
y['username'] = 'mlh'
y['machines'].remove('bar')
print(y)
print(x)
from copy import deepcopy
# 深复制
# copy.deepcopy 深拷贝 拷贝对象及其子对象
print("-"*20)
print("深复制")
d = {}
d['name'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['name'].append('Clive')
print("浅拷贝",c)
print("深复制",dc)
# dict.fromkeys(['name', 'age'])
# fromkeys 创建一个新字典，其中包含指定的键，且每个键对应的值都是 None
# 如果你不想使用默认值 None ，可提供特定的值。
print(dict.fromkeys(('name', 'age'),'NULL'))
print(d)
d.update(name="hha",age = 19)
print(d)

age = 10
assert 0 < age < 100, 'The age must be realistic'
age = -1

names = ['anne', 'beth', 'george', 'damon','lili']
ages = [12, 45, 32, 102]
for name, age in zip(names, ages):
    print(name, 'is', age, 'years old')

