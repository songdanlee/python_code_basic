'''
字符串
    使用引号引起来的数据
    字符串是一个不可变的数据类型，字符串也有索引
'''

str1 = '我是字符串'
str2 = "我也是 字符串"
str3 = """我是第一行
  我是第二行
  我是第三行      
"""
print(str3, type(str3))
#通过索引获取字符串的某一个元素
print(str3[0])
# 切片
print(str2[2:5])

# 函数
# index()第一个参数  指定的字符  返回当前字符在字符串中的索引位置  如果字符不存在就报错
# 第二个参数 查找起始位置
# 第三个参数  查找结束位置（不包含结束位置）
print(str2.index('是', 1, 3))
# find() 查找指定字符串索引位置，如果没有找到返回-1
print(str2.find("我a", 1, 3))

# split()切分， 如果不传参数 以空格切分
# 如果传了参数 就以指定的字符切分  返回列表
print(str2.split())
# join 将列表按照指定的字符返回字符串
list1 = ['我', '是', '啦', '啦', '啦']
res = "".join(list1)
print(res)

tup = ("h", 'e', 'l', 'l', 'o')
str4 = "".join(tup)
print(str4)

# 替换 replace(字符,字符)用后面的字符替换前面的字符
#[]指定最多替换多少个
str4 = str4.replace('l', 'o', 1)
print(str4)

#strip() 默认去除字符串两边的空格
# 如果传参数，就是指定删除字符串开头和结尾的指定字符，字符串中间的内容不会被删除

str3 = "**I LOVE YOU**"
print(str3)
print(str3.strip())

print(str3.strip('*'))
print(str3.lstrip("*"))
print(str3.rstrip("*"))

str4 = '欢迎光临%s' % '北京'

str5 = '欢迎{}来到{}参加开班'.format('小灰灰', '青青草原')
print(str5)

str5 = '欢迎{name}来到{addr}参加开班'.format(name='小灰灰', addr='青青草原')
print(str5)

str6 = '我是我也是我'
print(str6.split("我"))