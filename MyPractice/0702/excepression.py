import re

"""
re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
re.match(pattern, string, flags=0) pattern 匹配的正则表达式 string 要匹配的字符串 flag标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等
re.search 扫描整个字符串并返回第一个成功的匹配。

re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。

import re
 
line = "Cats are smarter than dogs";
 
matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print("match --> matchObj.group() : ", matchObj.group())
else:
   print("No match!!")
 
matchObj = re.search( r'dogs', line, re.M|re.I)
if matchObj:
   print("search --> matchObj.group() : ", matchObj.group())
else:
   print("No match!!")
   
   
输出
No match!!
search --> matchObj.group() :  dogs
"""


reGroupTestStr = '<h1 class="h1user">crifan</h1>'
# 1 Match Objects
# 如果查找到了，则对应返回的值是一个 match对象，打印出来都是 re.Match object之类的
# +?最小匹配
foundH1user = re.search('<h1 class="h1user">(.+?)</h1>', reGroupTestStr)
print(foundH1user)
if foundH1user:
    # 2 matched.group(0)
    # 如果有匹配的字符串，则之前通过括号所括起来的就是group，
    # group(0)代表整个字符串
    matchString = foundH1user.group(0)
    print(matchString)
    # 3 matched.group(N)
    # 如果之前有多个括号，即多个group，那么分别对应着group(1),group(2)....group(N)
    h1User = foundH1user.group(1)
    print("Group(1)", h1User)

    # 4 matched.groups()
    # MAtch对象的groups,表示从group(1)开始往后所有的值，组成一个Tuple类型的值
    allMatchedGroups = foundH1user.groups()
    print("allMatchedGroup", allMatchedGroups)  # allMatchedGroup ('crifan',)

    # 5 matched.start(N) and matched.end(N)
    # 也可以获得所匹配的group的起始位置和结束位置
    start1 = foundH1user.start(1)
    end1 = foundH1user.end(1)
    print("Group(1) start postion=%d,end position=%d" % (start1, end1))
    # 6 matched.string
    # 通过MatchObject.string的方式，获取值，和之前MatchObject.group(0)，是一样的
    foundString = foundH1user.string
    print("foundString",foundString)
    #7 get string by [startN:endN]
    # 对应的，还可以通过start和end之间，获得所匹配的字符串
    #和之前通过MatchObject.group(1)获得的值，也是一样的
    strByStartEnd = foundString[start1:end1]
    print(strByStartEnd)
# 8. 演示如何 前向引用，即匹配前面已经出现的某个group的值
# ！！！注意：下面这个写法，是无法工作的，因为\1只是代表了特殊的单个字符'\1'而不是去匹配编号为1的group
# foundPrevMatch = re.search('<(\S+) class="h1user">.+?</\1>', reGroupTestStr);
# 下面两种写法才是正确的：
# foundPrevMatch = re.search('<(\S+) class="h1user">.+?</\\1>', reGroupTestStr);
# \S 匹配任意非空格字符，与\s相反（匹配任何空格字符），
foundPrevMatch = re.search(r'<(\S+) class="h1user">(.+?)</\1>', reGroupTestStr)
if foundPrevMatch:
    #9 编号为1，2的group，分别就是上面的
    #(\S+)和(.+?),所以分别是标签h1和h1user的值
    #10，对应的\1就是匹配最前面的，第一个group，即(\S+)
    h1 = foundPrevMatch.group(1)
    print("h1=",h1)

    h1User = foundPrevMatch.group(2)
    print("h1User=",h1User)
