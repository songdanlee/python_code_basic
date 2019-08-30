# int 类型
print(type(10), 10)
#float 类型
print(type(10.0), 10.0)
#bool
print(type(True), True)
print(type(False), False)

# int + True ，自动转型，级别低的向级别高的的类型转换
print(10 + True)
print(10 + False)

print(10.0 + False)

#数值强制转换为bool
print(bool(0))
print(bool(1))

print(bool(0.0))
print(bool(1.1))

# bool转为浮点类型
print(float(True))
print(float(False))
# bool转为整型类型
print(int(True))
print(int(False))

# int + float
print(10+10.0)

# 二进制   八进制  十六进制
print(0B101)  # 二进制
print(0O12)  # 八进制
print(0Xf)  # 十六进制

print(int('f', 16))
