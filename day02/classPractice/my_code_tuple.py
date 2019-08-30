# 元组元素不可变，没有append，insert 方法，可以正常索引获取
# 定义一个空的tuple，t=()
classmates=("Michael","BOb","Tracy","Bob","Bob")

for name in classmates:
    print(name)

print(classmates.count("Bob"))


