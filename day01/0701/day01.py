
# 注释
'''
多行注释
多行注释
'''
"""
多行注释
多行注释
"""
# 自动类型转换
print(10 + 11.2)
print(True + 10)# True 转为1
print(False + 10.1) #False 转为0.0
# 强制转换

# bool 强转
print(bool(10))
print(bool("10.20"))
print(bool(0))
print(bool(""))

# int 强转

print(int(True))
print(int(False))
print(int(10.02))
print(int(10.2))
print(int("100"))
# print(int("10.0")) 不能转

# float 强转
print(float("10.9"))
print(float(10))
print(float(True))
print(float(False))
print(float("10"))

# 变量
x = 10
y = 20
z = x * y
print(z)

# wname = input("请输入名称：")
# wpass = input("请输入密码：")
#
# print(wname, wpass)

name = "尼古拉斯赵四"
age = 38
sex = False
height = 1.78
weight = 60.3

dic = dict(name="尼古拉斯赵四", age=38, sex=False, height=1.78, weight=60.3)
print(True and False or not False and False)
print(False >= 0)

# height = float(input("请输入高度:"))
# weight = float(input("请输入宽度"))
# print(height * weight)

# name = input("请输入用户名")
# password = input("请输入密码")
#
# print(name, password)

# price = float(input("请输入香蕉的单价:"))
# num = int(input("请输入购买数量："))
# print(price * num)

