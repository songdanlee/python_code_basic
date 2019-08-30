
"""
int()
将bool转换成int
    True --> 1
    False -->0
将float转成int
    只保留整数部分
将str转换成int
    只能转纯数字的整形字符串
    str='123.1'  不能转
    str="123abd"  不能转
"""

str1='123'
print(int(str1))
print(type(int(str1)))

"""
int 转 float 在 后面加.0
str 转 float 
    只能转纯数字组成的字符串，包括纯浮点数组成的字符串
    如果是纯整形的字符串，返回  整形.0
bool 转 float
    True 1.0   False 0.0  
"""
str2=123
print(float(str2))
print(float(123.1))


'''
将int --> bool  0-->False
将float --> bool  0.0 --.False
将str --> bool  ,空字符串为False
'''
print(bool(""))
print(bool("0"))

"""
将float ---> str
将int ----> str
将bool -----> str
"""
print("----------------------")
# f = 1.2
# f = 12
f = True
print(str(f), (str(f)))
