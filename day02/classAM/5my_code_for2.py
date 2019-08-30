'''
质数：只能被1和被自身整除的数 1不是质数
判断一个数是否是质数
1.判断用户是否输入的是1 如果是1 直接输出1不是质数
2.如果用户输入的不是1 循环 用户输入数之前的数，逐个判断是否能被整除 如果能被整除 调试不是质数 并结束循环
3.如果逐个判断失败 说明当前数为质数 就执行else中的内容
'''

num = int(input("请输入一个数:"))
if num == 1:
    print("1不是质数")
else:
    count = 2
    while count < num:
        if(num % count ==0):
            print(num,"不是质数")
            break
        count += 1
    else:
        print(num,"是质数")