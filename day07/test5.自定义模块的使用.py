"""

from 模块 import *
默认引入所有

如果模块中有__all__ = []，这时候import * 不再
引入所有，而是引入__all__变量中包含的
"""
# 一
# import module1 as mo
# print(mo.PI)
# print(mo.func1(10, 20))
# 二
# import module1
# # print(PI)#NameError: name 'PI' is not defined
# print((module1.PI))
#三
# from module1 import *
# print(PI)
