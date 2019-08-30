"""
装饰器：

日志功能：
    记录：记录访问时间，记录访问了那个功能

开发原则
    1.添加新功能开放
    2.对修改源代码关闭

不修改源代码的前提下，新增新的功能

闭包操作
"""
import time


# 版本1
# def func1():
#     # 增加日志功能
#     f = open('log.txt',mode='a',encoding='utf-8')
#     time_str = time.asctime()
#     func_name = 'func1'
#     f.write(time_str + '\t' + func_name)
#     f.close()
#     print("功能1")
#
# func1()

# 版本2
def log(func):
    # 增加日志功能
    f = open('log.txt', mode='a', encoding='utf-8')
    time_str = time.asctime()
    func_name = func.__name__
    f.write(time_str + '\t' + func_name + "\n")
    f.close()


def funOut(func):
    def funIner():
        log(func)
        func()

    return funIner


@funOut
def func1():
    print('功能1')


# f1 = funOut(func1)
# func1()

def funcOutter(func):
    print("AA")
    def funcInner():
        print("A---start")
        return "《" + func() + "》"
    print("A--end")
    return funcInner

def funcOutter1(func):
    print("BB")
    def funcInner():
        print("B--start")
        return "￥:100 "+func()
    print("B--end")
    return funcInner

@funcOutter1
@funcOutter
def bookName():
    return "从入门到放弃"



# bookName = funcOutter(bookName)
print(bookName())


# bookName = funcOutter1(bookName)
# print(bookName())

