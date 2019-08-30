'''
变量的作用域
    全局变量:在函数外部定义的变量，任何位置都能访问
    局部变量：在函数内部定义的变量就是局部变量  只能在当前函数内部去使用，函数外部访问不到

'''

#num = 10

# def func():
#     name = 'zhangsan'
#     print(name)
# func()

#在函数内部  如果要修改全局变量的值  需要用global 声明
#告诉函数我们要修改的变量是全局变量

'''
在函数内部使用global声明的变量  其实就是全局变量
但是只能在函数调用之后，才能在全局访问
'''
def func():
    global num1
    num1 = 1
    print(num1)
# print(num1) # 此处报错
func()
print(num1)#调用函数后可以访问

def func2(num1,num2):
    return num1+num2,num1*num2

sum,mul = func2(10,20)

