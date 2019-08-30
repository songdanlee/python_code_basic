# 123 ---> 321

res = 123
a = res % 10
res //= 10
b = res % 10
c = res // 10

print(a, b, c)
print(a * 100 + b * 10 + c)
