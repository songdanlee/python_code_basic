lis = ["a",'b','c','d','z']
lis1 = ['e','f','g']

lis.extend(('e','f','g'))
print(lis.index('e',1,6))
print(lis.count('a'))

str1 = "hello world"
print(str1.find('o',5,8))
for i in str1.split('o'):
    print(i)

s = " ".join(lis)
print(s,"1243",sep='--')

dic = dict(name='lala',age=90,like=['watch movies','chicken'])

dic.update(name='hha',sex='0')
print(dic)
a = "{name:s}-----{age:d} ".format(name='tom',age=12)
print(a)