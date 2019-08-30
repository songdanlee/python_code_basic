# li = [1, 2, 3, 4, 5]
#
#
# def square(x):
#     return x ** 2
#
#
# print(list(map(square, li)))
# print(list(map(lambda x: x ** 2, li)))

print([x**2 for x in range(1,21)])
print([(lambda x:x**2) (x) for x in range(1,21)])

print(list(map(lambda x:x**2,range(1,21))))

list1 = [3,5,-4,-1,0,-2,-6]
sorted(list1,key=lambda x:abs(x))

from functools import reduce

print(reduce(lambda x, y: x + y, [1,2,3]))