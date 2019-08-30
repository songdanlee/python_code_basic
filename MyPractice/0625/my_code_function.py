def my_abs(x):
	if x > 0:
		return x
	else :
		return -x
print(my_abs(10))
print(my_abs(-10))

def nop():
	pass #pass 什么都不做，占位符

import math

def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx,ny
x,y = move(100,100,60,math.pi/6)
print(x,y)


# ^ 异或
def change(x,y):
	x = x ^ y
	y = x ^ y
	x = x ^ y
	return x,y
x,y = change(1,7)
print(x,y)


def quadratic(a, b, c):
	return (-b + math.sqrt(b*b - 4 * a *c)) / (2 * a),(-b - math.sqrt(b*b - 4 * a *c)) / (2 * a)


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

def pown(x,n):
	num = 1
	while n > 0:
		num *= x
		n -= 1	 
	return num
print(pown(10,3))
"""
python的默认参数比c++的更灵活： 
１、默认参数都需要放在最后边(必选参数必须在前,默认在后) 
２、可以仅修改需要的默认参数，而不必把该参数之前的默认参数都填上
"""
def enroll(name,gender,age=16,num = 8,city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('num:', num)
    print('city:', city)
enroll("Michale","F")
enroll("Michale","F",18)
enroll("Michale","F",city = '上海',num = 9)


def add_end(L = None):
	if L is None:
		L = []
	L.append('END')
	return L

print(add_end())
print(add_end())

def calc(*number):
	sum = 0
	for n in number: 
		sum += n * n
	return sum
print(calc(1,2,3,4))


lis = [1,2,3,4,5,6]
def sqare(x):
	return x**2
print(list(map(sqare,lis)))
print(list((lambda x:x**2) (x*2) for x in lis))


 list(map(lambda x:x**2,range(1,21)))
list(map(lambda x:x**2,range(1,21)))