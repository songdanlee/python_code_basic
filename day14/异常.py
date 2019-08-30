
try:
    a = input("请输入被除数")
    a = int(a)
    b = input("请输入除数")
    b = int(b)
    c = a / b
    print(c)
except ValueError as e:
    print("输入数据有误")
    print(e)
except ZeroDivisionError as e:
    print("0不能做除数")
    print(e)
except Exception as e:
    print(e)
