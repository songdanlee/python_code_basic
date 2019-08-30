"""

封装
    球矩形的周长，矩形的面积
    求圆的周长，面积
"""
PI = 3.14


# 求矩形周长
def func1(length, width):
    return 2 * (length + width)


# 求矩形的面积
def func2(length, width):
    return length * width


# 求圆形周长
def func3(r):
    return 2 * r * PI

# 求圆形面积
def func4(r):
    return PI * r * r
#如果直接运行当前模块执行

if __name__ == '__main__':
    print("圆周率为%s"%PI)
