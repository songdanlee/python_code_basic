import random

guessnum = random.randint(10,30)

"""
count = 1
while count <= 5:
    num = int(input("第"+str(count)+"次,请输入猜的数字\n"))
    if(num > guessnum):
        print("大了")
    elif num < guessnum:
        print("小了")
    else:
        print("猜对了")
        break
    count += 1
else:
    print("机会用完了，下次努力呀")
"""
print("请输入",10,"-","30","之间的数字")
for i in range(1,6):
    num = int(input("第%s次,请输入猜的数字\n"%i))
    if (num > guessnum):
        print("大了")
    elif num < guessnum:
        print("小了")
    else:
        print("猜对了")
        break
else:
    print("机会用完了，下次努力呀")