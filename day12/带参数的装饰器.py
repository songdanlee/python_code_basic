"""
装饰带参数的函数

"""
# import time
# def func1(a):
#     print(f"a={a}")
#
# def log(func):
#     # 增加日志功能
#     f = open('log.txt', mode='a', encoding='utf-8')
#     time_str = time.asctime()
#     func_name = func.__name__
#     f.write(time_str + '\t' + func_name + "\n")
#     f.close()
#
# def funOut(func):
#     def funIner(a):
#         log(func)
#         func(a)
#     return funIner
# func1 = funOut(func1)
# func1(100)

import time
def func1(a):
    print(f"a={a}")

def log(func):
    # 增加日志功能
    f = open('log.txt', mode='a', encoding='utf-8')
    time_str = time.asctime()
    func_name = func.__name__
    f.write(time_str + '\t' + func_name + "\n")
    f.close()

def funOut(func):
    def funIner(*args,**kwargs):
        log(func)
        func(*args,**kwargs)
    return funIner

@funOut
def fun2(a):
    print(f"a={a}")

fun2(2)

@funOut
def fun3(a,b,c):
    print(f"a={a},b={b},c={c}")
fun3(1,3,5)

@funOut
def fun4(**kwargs):
    print(kwargs)
fun4(b=3,c=5,a=3)

