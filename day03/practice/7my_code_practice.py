'''
已知：lst= [1, 2, 3, 4, 5, 6]
题1.请打印输出：
0, 1
1, 2
2, 3
3, 4
4, 5
5, 6
'''
lst= [1, 2, 3, 4, 5, 6]

for i in range(len(lst)):
    print("%d, %d"%(i,lst[i]))
'''
题2.将lst倒序成：[6, 5, 4, 3, 2, 1] 
'''
lst.reverse()
print(lst)
lst= [1, 2, 3, 4, 5, 6]
print(lst[::-1])

'''
将lst中的偶数挑出*2，结果为：[4, 8, 12] 
'''
lst= [1, 2, 3, 4, 5, 6]
ll = [x*2 for x in lst if x % 2 ==0]
print("*"*20)
print(ll)
lst = list(filter(lambda  x: x%2==0,lst))
lst = list(map(lambda x :x*2,lst))
print(lst)
'''
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，
输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

1  2  8  9
2  4  9  12
4  7  10  13
6  8  11  15
'''
numbers = [
[1,2,8,9],
[2,4,9,12],
[4,7,10,13],
[6,8,11,15]
]
findNum = 14
row = 0
col = len(numbers[0])-1
while row <= len(numbers[0])-1 and col >= 0:
    if numbers[row][col] == findNum:
        print("找到了")
        break
    if numbers[row][col] > findNum:
        col -= 1
    if numbers[row][col] < findNum:
        row += 1
else:
    print("找不到啊")
'''
斐波那契数列
写一个函数，输入n，求第n项的值
0,1,1,2,3,5

青蛙跳台阶：
    一只青蛙一次可以跳一级台阶，也可以跳两级。求
    该青蛙上一个n级台阶共多少跳法
    
    思路：一级台阶，有一种跳法，二级台阶有两种跳法，
    分两次跳：每次跳一个  ，一次跳两级
    当n>2时，第一次跳有两种选择，一是第一次直跳一级，此时跳法数目
    等于剩下n-1级台阶的跳法，即f(n-1)
    二是第一次跳两级，此时跳法数目    等于剩下n-2级台阶的跳法，即f(n-2)
    即f(n) = f(n-1) + f(n-2)
'''
fibnaqi = [0,1,1]
n = int(input("请输入n\n"))
for i in range(3,n+1):
    fibnaqi.append(fibnaqi[-1]+fibnaqi[-2])
print(fibnaqi[n])