# i = 1
# while i<= 5:
#     print("我是第%s次外循环****"%i)
#     j = 1
#     while j <= 5:
#         print("内循环,第%s次循环"%j)
#         j += 1
#     i += 1


for i in range(1,6):
    print("*"*i)


for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()


print("-"*20)
# 九九乘法表 下三角
for i in range(1,10):
    for j in range(1,i+1):
        print("%s*%s =%2d" %(j,i,i*j),end="\t")
    print()

print("----"*15)
# 九九乘法表 上三角
for i in range(9,0,-1):
    for k in range(0,9-i):
        print("        ",end="")
    for j in range(1,i+1):
        print("%s*%s =%2d"%(j,i,i*j),end="\t")
    print()
