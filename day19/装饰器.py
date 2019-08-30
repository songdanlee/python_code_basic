def wrapper(f):
    def inner(*args,**kwargs):
        ret = f(*args,**kwargs)
        return ret
    return inner

@wrapper
def func(*args,**kwargs):
    print("zzz")
    return 1

print(func())