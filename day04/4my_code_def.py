# 定义一个函数

# 位置传参
def func1(num1,num2): # 形参 用来接收调用时传的参数
    print("参数一",num1)
    print("参数二",num2)

# 调用函数
#func1(10,12) # 实参

#默认值传参

def func2(msg1=1,msg2=2):
    print("第一个参数", msg1)
    print("第二个参数", msg2)
#func2()

#关键字传参
def fun3(msg1,msg2):
    print("这是第一个参数", msg1)
    print("这是第二个参数", msg2)
#fun3(msg2=12, msg1=10)

#非关键字收集参数
def fun4(msg,*args):
    print(msg)
    print(args)
#fun4(1,2,3)

# 关键字参数收集参数
def fun5(msg,**kwargs):
    print(msg)
    print(kwargs)
#fun5(name='a',age=19,msg=10,sex=0)

# 参数的顺序问题
# 先写位置函数  ，非关键字收集参数，关键字参数，关键字收集参数
def func6(msg,age=12,*args,name,**kwargs):
    print(msg)
    print(args)
    print(kwargs)
func6(10,11,1,2,3,4,name='zs',addr='bj',phone='1049')

# 位置参数、默认参数、可变参数、命名关键字参数和关键字参数。
# def function(a, b, c=0, *, d, **kw):



# 函数返回值
def fun7(num1,num2):
    return num1+num2,num1*num2
addresult,multresult = fun7(10,20)
print(addresult,multresult)







