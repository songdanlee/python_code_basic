def war1(func):
    print("war 1")

    def inner(*args, **kwargs):
        print("======war1 start=====")
        func(*args, **kwargs)  # inner
        print("======war1 end=====")
    return inner

def war2(func):
    print("war2")

    def inner(*args, **kwargs):
        print("======war2 start=====")
        func(*args, **kwargs)
        print("======war2 end=====")
    return inner

@war1
@war2
def f():
    print("****self****")
f()
# 等价于
# f1 = war2(f)
# f2 = war1(f1)
# f2()