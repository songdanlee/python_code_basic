print(dir([]))
print(dir([].__iter__()))

print(set(dir([].__iter__())) - set(dir([])))

print(['A', 'B', 'C'].__iter__().__length_hint__())

li = ['A', 'B', 'C', 'D']
iterator = li.__iter__()  # 获取迭代器
print(iterator.__next__())  # 获取A
print(iterator.__next__())
print(iterator.__next__())


class Fibonacci(object):

    def __init__(self, all_num):
        self.all_num = all_num
        self.a = 1
        self.b = 1
        self.current_num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.all_num <= 2:
            self.current_num += 1
            if self.current_num == 3:
                raise StopIteration
            return self.a
        else:
            if self.current_num < self.all_num:
                ret = self.a
                self.a,self.b = self.b,self.a+self.b
                self.current_num +=1
                return ret
            else:
                raise StopIteration

# for i in Fibonacci(10):
#     print(i)

def generator():
    print("zzz")
    yield 1
    print("xxxxx")
    yield 2

res = generator()
print(res.__next__())
print(res.__next__())


def gen1():
    for c in "AB":
        yield c
    for i in range(3):
        yield i
g = gen1()
for i in g:
    print(i)

def gen2():
    yield from 'AB'
    yield from range(3)

g = gen2()
for i in g:
    print(i)

print(list(gen2()))

laomuji = ('鸡蛋%s' % i for i in range(10))
print(laomuji)
print(next(laomuji))
print(laomuji.__next__())
print(next(laomuji))
print(laomuji)
print(list(laomuji))




def func():
    name = 'eva'
    def innner():
        print(name)
    print(innner.__closure__)
    return innner
f = func()
f()