import re


def test1():
    phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
    # print(type(phoneNumRegex))
    mp = phoneNumRegex.search("My number is 145-345-2333. 145-345-2335")
    print(mp.group())


def test2():
    # 添加括号将在正则表达式中创建“分组”,第一对括号是第 1 组。第二对括号是第 2 组
    # 向 group()方法传入 0 或不传入参数，将返回整个匹配的文本
    phoneNumRegex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
    mp = phoneNumRegex.search("My number is 145-345-2333. 145-345-2335")
    print(mp.group())
    print(mp.group(1))
    print(mp.group(2))
    # 如果想要一次就获取所有的分组，使用groups()方法返回多个值的元组
    areacode, mainNumber = mp.groups()
    print(areacode)
    print(mainNumber)


def test3():
    # 转义\
    phoneNumRegex = re.compile(r"(\(\d\d\d\))-(\d\d\d-\d\d\d\d)")
    mp = phoneNumRegex.search("My number is (145)-345-2333. 145-345-2335")
    print(mp.groups())

# 管道匹配多个分组
def test4():
    heroRegex = re.compile(r"Batman|Tina Fey")
    mo1 = heroRegex.match("Batman and Tina Fey.")
    print(mo1.group())
    mo2 = heroRegex.match("Tina Fey and Batman")
    print(mo2.group())

#  问号实现可选匹配
def test5():
    batRegex = re.compile(r"Bat(wo)?man")
    mo1 = batRegex.search("the adventures of Batman")
    print(mo1.group())
    mo2 = batRegex.search("the adventures of Batwoman")
    print(mo2.group())


# 用星号匹配零次或多次
def test6():
    batRegex = re.compile(r'Bat(wo)*man')
    mo1 = batRegex.search('The Adventures of Batman')
    print(mo1.group())
    mo2 = batRegex.search('The Adventures of Batwoman')
    print(mo2.group())
    mo3 = batRegex.search('The Adventures of Batwowowowoman')
    print(mo3.group())


def test7():
    """
如果调用在一个没有分组的正则表达式上，例如\d\d\d-\d\d\d-\d\d\d\d，方法
findall()将返回一个匹配字符串的列表，例如['415-555-9999', '212-555-0000']。
2．如果调用在一个有分组的正则表达式上，例如(\d\d\d)-(\d\d\d)-(\d\d\d\d)，方
法 findall()将返回一个字符串的元组的列表（每个分组对应一个字符串），例如[('415',
'555', '1122'), ('212', '555', '0000')]
"""
    phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
    lis = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
    print(lis)


def test8():
    # Regex对象的 sub()方法需要传入两个参数。第一个参数是一个字符串，用于取代发现的匹
    # 配。第二个参数是一个字符串，即要被替换的字符串。sub()方法返回替换完成后的字符串。
    namesRegex = re.compile(r'Agent \w+')
    print(type(namesRegex))
    s = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.Agent')
    print(s)


test8()

