res = 1 + 3
print(res)

# 如果+两边都是字符串，就叫做字符串的拼接
res1 = '1' + '12'
print(res1)
print(type(res1),res1)

# 字符串+数字 ，表示把字符串复制的次数
str1 = "**"*10
print(str1)

# / ,除 有小数,返回浮点型
print(10/3)
print(10/2)
# // ,整除 ，返回整数部分，舍去小数部分
print(10//3)
print(10//2)

# % ,取余，
print(10 % 2)
print(10 % 3)

# 比较运算,返回bool类型
# > >= < <= == !=
print(1 > 2)
print(2 >= 2)
print(10 != 10)
print(1 == 0)

# and 与 ，两边都为真，才为真，第一个为False ,则后面不会判断
print(1 > 2 and 1 == 1)
print(4 >=2 and 1 < 2)
print(10> 2 and 10 < 40)
print(1 ==2 and 3 ==3)

# or 或，只要有一个为真就为True，第一个为真，后面不会判断
print(2>1 or 3 > 2)
print(2 < 1 or 4 > 3)
# not 取反
print(not (1 > 2))
print(not (1==3))

# 123 ---> 321
num=123
a=num%10
b=num//10%10
c=num//100
print(a*100+b*10+c)