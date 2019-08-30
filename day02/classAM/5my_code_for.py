#range(start,end,step) 左闭右开，不包括结束位置，step步长

# for i in range(1,10):
#     print(i)
# lists = ["张三","李四","王五"]
# for i in lists :
#     print(i)

# 判断一个数是否是质数
# 1 不是质数

num = int(input("请输入数值:"))

# if(num == 1):
#     print(num,"不是质数")
# else:
#     flag = 1
#     for i in range(2, num):
#         if num % i == 0:
#             flag = 0
#             break
#     print(num, "是质数") if flag else print(num,"不是质数")

if(num == 1):
    print(num,"不是质数")
else:
    i = 2
    while i < num:
        if num % i == 0:
            print(num, "不是质数")
            break # break 后 ，不会执行else 的内容
        i += 1
    else:
        print("是质数")
