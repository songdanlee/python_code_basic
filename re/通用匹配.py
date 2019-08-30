import re
strs = "raoyunjiaoyu"
pat = "yun"
result = re.search(pat,strs)

print(result)

# \n  \t \r
# 通用字符
"""
\w 字母数字下划线
\W 除\w之外的字符
\d 十进制数
\D 除十进制数的数字
\s 空白字符
\S 除空白字符
"""
# []原子表

# 元字符
"""
. 除换行外任意字符
^ 开始位置
$ 结束位置
* 0\1\多次
？0\1
+ 1\多次
{n} 恰好n次
{n,}至少n次
{n,m}至少n，至多m
| 模式选择 或
（）模式单元
"""

"""
模式修正符
I ，忽略大小写
M,多行匹配
L,本地化识别匹配
U，unicode
S，让.匹配包括换行符 
"""
string = "Python"
pat = "pyt"
resu = re.search(pat,string,re.I)

print(resu)

"""
正则表达式函数
match 从头开始匹配
search 只找一个
全局匹配格式re.compile(正则表达式).findall(数据)

"""

# 实例 匹配.com .cn
# <a href = "http://www.baidu.com"></a>
import requests

hre = "https://read.douban.com/provider/all"
content = requests.get(hre).content.decode("utf-8")

pat = '<div class="name">(\w*?)</div>'

resu = re.compile(pat).findall(content)
print(resu)