# 编程求解1-4这4个数字可以组成多少个无重复的三位数，按从小到大的顺序输出这些数字
# li = [1,2,3,4]
#
# for i in li:
#     for j in li:
#         for k in li:
#             if i != j and j != k and k!=i:
#                 print(100*i+10*j+k)

#  验证命题：如果一个三位整数是37的倍数，则这个整数循环左移后得到的另两个3位数也是37的倍数。
# （注意验证命题的结果输出方式，只要输出命题为真还是假即可，而非每一个三位数都有一个真假的输出）

# 370 703 037
def check(num):
    ge = num % 10
    shi = num // 10 %10
    bai = num // 100
    print(num,ge,shi,bai)
    if (bai + ge*10 + shi *100)%37 == 0 and(ge*100+bai*10 + shi)%37==0:
        return 1
    return 0


for i in range(100,1000):
    if i%37==0 and check(i) == 0:
        print("假")
        break
else:
    print("真")

# 7. 一个数如果等于它的因子之和则称这个数为完数，
# 例如6，6=1+2+3，编程计算1000之内的所有完数并输出。
def iswanshu(num):
    s=0
    for i in range(1,num):
        if num % i == 0:
            s +=i
    if s==num:
        print(num,"是完数","组成是",end=" ")
        for i in range(1, num):
            if num % i == 0:
                print(i," ",end="")
        print()

for i in range(1,1001):
    iswanshu(i)

# 寻找第6个默尼森数
# 经典程序设计问题：找第n个默尼森数。P是素数且M也是素数，
# 并且满足等式M=2**P-1，则称M为默尼森数。
# 例如，P=5，M=2**P-1=31，5和31都是素数，因此31是默尼森数。
# 提交方式直接将答案（M的值）写在txt文件中通过网络提交。
import math as m
def prime(num):
    if num == 1:
        return 0
    for i in range(2,m.ceil(m.sqrt(num+1))):
        if num % i==0:
            return 0
    return 1
count = 0
for i in range(2,100):
    if prime(i) and prime(2**i-1):
        print(i,2**i-1)
        count+=1
        if count == 6:
            print(2**i-1)
            break

s = 0
for i in range(1, 11):
     if i % 2 == 0:
        continue
     if i % 10 == 5:
        break
     s = s + i
print(s)

