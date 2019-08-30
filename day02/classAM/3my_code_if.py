# 单分支
if 1 > 3:
    print("right")
print("代码结束")


# 用户输入年龄，判断用户是否成年，成年可以进入网吧
"""
age = int(input("请输入年龄："))
if age >= 18:
    print("成年，可以上网")
else:
    print("未成年，禁止进入")
"""
# 判断是否是合法年龄，1-120,如果不合法，提示活成妖了
# print("*"*20)
# age = int(input("请输入年龄："))
# if age >= 1 and age <= 120:
#     print("合法年龄")
# else:
#     print("不合法年龄")
#     if age >120:
#         print("活成妖了")

# 两人开房，先检测两个人都有身份证，都有允许入住，一个没有就不允许入住
id_cart1 = 0
id_cart2 = 1
if id_cart1==id_cart2==1:
    print("可以开房")
else:
    print("不可以开房")

"""
一周有七天，根据用户输入的数字，来判断输入的是星期几，
如果超出7天范围，提示一周只有七天
"""

# day = input("请输入星期几:")
#
# if day== '1':
#     print("今天是周一")
# elif day == '2':
#     print("今天是周二")
# elif day == '3':
#     print("今天是周三")
# elif day == '4':
#     print("今天是周四")
# elif day == '5':
#     print("今天是周五")
# elif day == '6':
#     print("今天是周六")
# elif day == '7':
#     print("今天是周日")
# else:
#     print("输入非法")

# 身份证+age>=18 可以上网，否则拒绝
id_card = 1
if id_card:
    age = int(input("请输入年龄："))
    if age >= 18:
        print("可以上网")
    else:
        print("年龄不满18，禁止上网")
else:
    print("没有身份证，不能上网")
# if id_card is 1:
#     print("111")

x = 1
y = 2
z = 3
# 如果x为真返回y，否则返回z
a = y if x else z
