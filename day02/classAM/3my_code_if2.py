
# if(1 > 2):
#     print("判断成功")
# print("程序结束")

#需求：去网吧
#判断用户年龄是否成年，成年之后允许上网 给出已成年
# age = input("请输入年龄:")
# age = int(age)
# if(age>=18):
#     print("已成年")
# print("结束")
#判断是否是合法年龄 1-120 如果合法提示年龄属于合法范围
#     不在合法范围 提示 活成妖了
age = int(input("请输入年龄"))
if 1<=age <= 120:
    print("合法年龄")
else:
    print("活成妖咯")
'''
需求：两人开房
id_cart1 = 1 有
id_cart2 = 1 
 检测两个人都必须有身份证 都有允许入住 有一个没有就不允许入住
'''
id_cart1 = 1
id_cart2 = 1
if id_cart2 and id_cart1:
    print("可以入住")
else :
    print("没有身份证，禁止入住")
'''
需求：
一周有7天 根据用户输入数字 来判断用户输入的是周几 如果超出7天的范围 提示一周只有七天
'''

day = input("请输入星期几:")

if day== '1':
    print("今天是周一，上班")
elif day == '2':
    print("今天是周二，周二开会")
elif day == '3':
    print("今天是周三，周三过了一半咯")
elif day == '4':
    print("今天是周四，动漫更新日")
elif day == '5':
    print("今天是周五，就要休息啦")
elif day == '6':
    print("今天是周六，睡一觉")
elif day == '7':
    print("今天是周日，明天上班咯")
else:
    print("输入非法")

# 去网吧 升级版
# 1.判断身份证
# 2.判断年龄
id_cart = input("请输入身份证:")
if id_cart:
    age = int(input("请输入年龄:"))
    if age >= 18:
        print("欢迎上网")
    else:
        print("未成年禁止进入网吧")
else:
    print("没有身份证，禁止进入网吧")

x = 1
y = 2
z = 3
a = z if x else y
print(a)