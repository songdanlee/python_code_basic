"""

列表推导式[]
字典推导式
    需求：{'A':65,'B':66.....}
集合推导式
{}
"""
s = {chr(i) for i in range(97, 97 + 26)}
print(s)

d = {chr(i): i for i in range(65, 65 + 26)}
print(d)

d = {v: k for k, v in d.items()}
print(d)

list1 = [(i, j) for i in range(5) for j in range(3)]

# 练习
a = [lambda x: x * i for i in range(3)]
print(a[0](2))  # 4

a = []
for i in range(3):
    def func(x, i=i):
        return x * i
    a.append(func)
print(a[1](2))
