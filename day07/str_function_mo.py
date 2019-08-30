"""
封装字符串相关函数

基础练习题
在自定义模块中封装如下功能：并完成验证
1.封装自定义函数，功能类似lower(src)
2.封装自定义函数，功能类似upper(src)
3.封装函数，功能类似find(src,sub)
4.封装函数，功能类似rfind(src,sub)
5.封装函数，功能类似isdigit(src)
6.封装函数，功能类似partition(src,sub)
"""


# 1.封装自定义函数，功能类似lower(src)
def str_lower(src):
    str_new = ""
    for i in src:
        if 'A' <= i <= 'Z':
            str_new += chr(ord(i) + 32)
        else:
            str_new += i
    return str_new


# 2.封装自定义函数，功能类似upper(src)
def str_upper(src):
    str_new = ""
    for i in src:
        if 'a' <= i <= 'z':
            str_new += chr(ord(i) - 32)
        else:
            str_new += i
    return str_new


# 3.封装函数，功能类似find(src,sub)
def str_find(src, sub):
    for i in range(len(src) - len(sub) + 1):
        # print(src[i:i+len(sub)])
        if src[i:i + len(sub)] == sub:
            return i
    return -1


# 4.封装函数，功能类似rfind(src,sub)
def str_rfind(src, sub):
    for i in range(len(src) - len(sub), -1, -1):
        # print(src[i:i + len(sub)])
        if src[i:i + len(sub)] == sub:
            return i
    return -1


# 5.封装函数，功能类似isdigit(src)
def str_isdigit(src):
    for i in src:
        if not '0' <= i <= '9':
            return False
    return True


# 6.封装函数，功能类似partition(src,sub)
# 原字符串以sub切分为三部分，构成元组。(sub之前,sub,sub之后)

# "1236789abcada"   "abcada"   ("1236789", "abcada","")
# "12234" "a"    ("12234","","")
# "1234" "2"    ("1","2","34")

def str_partition(src, sub):
    index = str_find(src, sub)
    if index!=-1:
        tu = (src[:index], sub, src[index + len(sub):])
    else:
        tu = (src[::], "", "")
    return tu


print(str_partition("abcdefg", "fg"))
# 功能类似startswith(src,sub)判断字符串src是否以字符串sub的内容开头
def str_startswith(src, sub):
    return src[:len(sub)] == sub


# 功能类似endswith(src,sub)判断字符串src是否以字符串sub的内容结尾
def str_endswith(src, sub):
    return sub == src[len(src)-len(sub):]

if __name__ == '__main__':

    ss="12345"
    print(ss[:])
    # print(str_lower("ABCDEFcedff&&*1223"))
    # print(str_upper("ABCDEFcedff&&*1223"))

    # print("12CD3456ABCDCD".find("CD"))
    # print(str_find("12CD345CD6ABCDCD", "CD"))

    # print(str_rfind("123456ACabcd","bc"))
    # print("123456ACabcd".rfind("bc"))

    # print("1234123131".isdigit())
    # print(str_isdigit("1234111211112313213"))

    # tu = "1236789abcada".partition("2")
    # print(tu)
    print(str_partition("1236789abcada","2"))

    # print("acd123456".startswith("acda"))
    # print(str_startswith("acd123456", "acda"))


    # print("acd1234567 ".endswith("567 "))
    # print(str_endswith("acd1234567 ","567 "))