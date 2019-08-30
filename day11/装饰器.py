import time
from functools import wraps

def func():
    print("感谢大家，感谢人民。。。。。。。。。。。")


def timer(func):
    def innner():
        start_time = time.time()
        time.sleep(0.01)
        func()
        end_time = time.time()
        print(end_time - start_time)
    return innner

fun = timer(func)
fun()

@timer
def func1():
    print("我爱。。。。你好世界，hello world")

func1()

