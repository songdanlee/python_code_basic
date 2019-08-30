"""

匿名函数
    传统函数定义方式:
        def 函数名(形参列表):
            pass
    匿名函数
        lambda 参数列表....:实现函数的代码
        实现函数的有限制
        1.表达式中不能包含 循环，return
        2.可以包含 if...else...语句（三元条件表达式）.
        3.表达式计算的结果直接返回

    使用场合
        列表中元素排序
        第一种
        sort(key=lambda x:x[index])
        sort(key=lambda x:x[key])
        max(key=lambda x:x[index])
        max(key=lambda x:x[key])

        第二种
        filter(lambda x:x%2==0,[1,2,3,4,5])

        第三种
        func1 = lambda a,b:a+b
        print(func1(10,20))
"""

list1 = [1, 2, 10, -2, 23]
list1.sort()  # 默认从小到大
print(list1)
student_list = [
    [1002, 'Jack', 18],
    [1000, 'Rose', 90],
    [1001, 'James', 35]
]

print("排序前：", student_list)
student_list.sort(key=lambda x: x[2])
print("排序后", student_list)

student_list = [
    {'id': 1001, 'name': 'Jack', 'age': 18},
    {'id': 1002, 'name': 'Rose', 'age': 90},
    {'id': 1003, 'name': 'James', 'age': 35}
]
print("排序前：", student_list)
student_list.sort(key=lambda x: x["name"])
print("排序后", student_list)

v = max(student_list, key=lambda x: x["age"])
v = max(student_list, key=lambda x: x["id"])
print(v)
# 需求，找出列表中的所有偶数 [1,20,3,4,90,23]
list2 = [1, 20, 3, 4, 90, 23]
v = filter(lambda x: x % 2 == 0, list2)
print(list(v))
for i in v:
    print(i)

func1 = lambda x, y: x + y
print(type(func1))
print(func1(10, 22))


def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j * j
            return g
        r = f(i)
        fs.append(r)
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())
print(type(f1))