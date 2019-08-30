"""
变量的作用域：
    L:局部
    E:闭包
    G:全局
    B:内建
加载顺序：
    1.内建
    2.全局
    3.闭包
    4.局部
搜索顺序：
L->E->G->B

闭包函数：
    1.定义：
        必要条件：
            1.1 函数嵌套定义
            1.2 外部函数的返回值为内部函数名
            1.3 内部函数使用外部函数得变量
        注意：
            闭包中变量的生命周期得以延长
    2.验证
        print(f.__closure__)
        如果打印的内置为None，则不是闭包函数

"""

# 局部
def funcOut(a):
    def funcIn():
        print("内部函数被调用")
        print(a)
    return funcIn
f = funcOut(10)
f()
# 判断是否是闭包函数，如果打印的是None，则不是
print(f.__closure__)
