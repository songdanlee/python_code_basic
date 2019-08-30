"""
1.什么是模块
    .py文件
2.模块分类
    2.1 内键模块(内置模块) builtins.py
    2.2 系统标准模块
    2.3 第三方模块
    2.4 自定义模块
3.模块中可以存在什么东西
    变量，函数，可执行代码......
4.如何使用模块
    4.1 引入模块
        4.1.1 import 模块名
            引入后的用法
            模块名.函数名/变量名
        4.1.2 import 模块名 as 新名字
            新名.函数名/变量名
           import 模块1,模块2，模块3(少用)
        4.1.3  import 模块1 as 新名,模块2 as 新名字
    4.2 引入模块中的功能
       from 模块 import 功能1,
            用法：直接写功能名
       from 模块 import 功能1 as 新功能名
       from 模块 import 功能1,功能2,功能3
    4.3

"""

# import random as rand
#
# num = rand.randint(1,6)
import module1 as mo
from random import randint
from random import choice,random as ran
from sys import *


print(mo.PI)
print(ran())
randint(1,24)



