strs = "this is a line of text for test"

index1 = strs.find("is")
print(index1)
# 指定范围，指定起始结束位置
index2 = strs.find("is", 0, 15)
print(index2)
# find 查找不存在，返回-1，返回第一个字符索引值
print(strs.find("isa"))
# rfind，从右边开始查找
print(strs.rfind("is"))
# index 查找，不存在，会报错
print(strs.index("test"))
# 可以指定起始，结束位置，不包括结束位置
# print(strs.index("test",0,15))
# rindex(),从右边开始查找
print(strs.rindex("is"))
# count(str,start,end)返回str在start，end出现的次数,不包括结束位置
print(strs.count("is", 0, 4))
print(strs.count("is"))


strs = "this is a line of text for test"

# replace(old,new,count)
# 把字符串中的old替换成new，count指定替换的最大次数，替换次数<=count，不指定默认替换所有
# 返回替换后的字符串
print(strs.replace("is", "SS", 4))
print(strs.replace("is", "SS"))
print(strs)
# capitalize()，将字符串第一个字符大写，返回替换后新的字符串
str2 = "this is a test for a line text"
str3 = str2.capitalize()
print(str3)
# title()，将字符串的每个单词首字母大写，返回替换后新的字符串
str4 = str2.title()
print(str4)
# lower()，将字符串的大写字母替换成小写字母，返回
str5 = "THIS IS A TEST TO A LINE OF text"
str6 = str5.lower()
print(str6)
# upper() ,将字符串的小写字母替换成大写字母，返回
print(str6.upper())
# swapcase()    # 大小写互换
str6="This IS A Test"
print("str6",str6.swapcase())

#ljust(width,fillstr),左对齐
#rjust(width,fillstr)，右对齐
#center(width,fillstr)，居中
#默认用空格填充指定宽度，可以指定字符串，返回填充后的字符串
print("this is a title".center(52,"-"))
print("|","|".rjust(51))
print("|","this is text".center(51,"*"),"|",sep="")
print("|".ljust(51," "),"|")
print("-"*53)

# strip(),删除字符串两端的空白字符,可以指定删除的字符
# lstrip(),删除字符串左边的空白字符,可以指定删除的字符
# rstrip()#删除字符串末尾的空白字符,可以指定删除的字符
str7 = " this is a test for blank "
print(str7)
print(str7.strip())
print(str7.lstrip())
print(str7.rstrip())


# split(sp,maxsplit) ,把字符串以sp切割符(默认空格)切割，maxsplit指定切割次数，
# 返回切割后字符串，组成的列表
str1 = "张三|23|180|58"
fields = str1.split("|")
fields = str1.split("|", 2)
print(fields)
str8="""
我是第一个行
我是第二行
我是第三行
我是第四行
我是第五行
"""
# splitlines(keepends) ,按照行分隔，返回一个包含各行作为元素的列表
# keepends,True显示\n,False不显示\n
lines = str8.splitlines(True)
for i in lines:
    print(i)


# startswith(),检查字符串是否是以指定字符串开头，是，返回True，否则，返回False
# 可以加指定起始结束位置，
str2 = "this is a test for a line text"
bo = str2.startswith('th')
print(str2.startswith('this', 0, 3))
print(bo)

# endswith(suffix,start,end),检查字符串是否是以指定字符串开头，是，返回True，否则，返回False
# 可以加指定起始结束位置，
bo1 = str2.endswith("text")
print(bo1)

# isdigit()
# True: Unicode数字，byte数字（单字节），全角数字（双字节），罗马数字
# False: 汉字数字
# Error: 无
#
# isdecimal()
# True: Unicode数字，，全角数字（双字节）
# False: 罗马数字，汉字数字
# Error: byte数字（单字节）
#
# isnumeric()
# True: Unicode数字，全角数字（双字节），罗马数字，汉字数字
# False: 无
# Error: byte数字（单字节）


#isalpha(),如果字符串中所有字符都是字母 则返回 True,否则返回 False
#可以检测中文，编码为unicode编码，当字符串设置为utf-8，返回false
str9 = "ia ma litttl ejoy"
print(str9.isalpha())# False,包含空格
str9 = "hahhayoudontseemewhatimeans"
print(str9.isalpha())#True
# isdigit(),如果字符串中只包含数字则返回 True 否则返回 False.
str10 = "123456789043"
print(str10.isdigit())#True
str10 = "1234567a89043"
print(str10.isdigit())#False
str10 = "1234 56789043 "
print(str10.isdigit())#False
#isalnum(),如果字符串中所有字符都是字母(中文)或数字则返回 True,否则返回 False
print("----"*39)
str11 = "1234567a89043"
str11 = u"1234567a89043咋呼大".encode("utf-8")
# isnumeric() 检测字符串中的数字，纯数字(中文的数字（一,壹,二贰），罗马数字ⅡⅢⅣⅤ)返回True，
# str11 = '12233一二三叁④'
# print(str11.isnumeric())
print(str11.isalnum())
print(str11.isalpha())
print("一壹二贰ⅡⅢⅣⅤ₃⅔❽⒇".isnumeric())
#isspace(), 如果字符串中只包含空格，则返回 True，否则返回 False.
# print("\t\n  ".isspace()) True

print("------"*20)


lis1 = [1,2,4,5]
lis2 = [3,6,7,8]
print(lis1+lis2)

names = ["赵四","刘能","宋小宝","小沈阳"]

name = names[1]#通过索引获取元素

print(name)

for name in names:
    print(name)

print(names[0::2])

name1,name2,name3,name4 = names

print(name1,name2,name3,name4)

*lst2,lst1, = ['a','b','c','d']
print(lst1)
print(lst2)
*s,s1 = "hello worlds"
print(s)
print(s1)

import json

# Python 字典类型转换为 JSON 对象
data1 = {
    "no": 1,
    "name": 'Runoob',
    'url': 'http://www.runoob.com'
}

json_str = json.dumps(data1)
print("Python 原始数据：", repr(data1))
print("JSON 对象：", json_str)

# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print("data2['name']: ", data2['name'])
print("data2['url']: ", data2['url'])

import re
JSONP = 'callbackFunction(["customername1","customername2"])'

result = re.findall(r'^\w+\((.*)\)$',JSONP)
print(result)