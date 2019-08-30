"""
包：(package)
本质：
    python3
        文件夹
    python2
        必须包含一个__init__.py模块的文件夹才是包
包的作用：
    1.更好的整理多个模块
    2.不同的包中可以存在同名模块

包的使用
    import 包名.模块名
    import 包名.模块名 as 新名
    ---------------------------
    from 包名 import 模块名
    from 包名 import 模块名,模块名 1...
    ---------------------------------
    from 包名.模块名... import 变量名
    from 包名.模块名... import 变量名 1,变量名 2...

    _ _ init _ _ .py的使用
"""
#直接引入包中的模块
# import package1.module1
# # 使用其中变量
# print(package1.module1.number)
# import package1.module1 as pm
# print(pm.number)

# 2 从包中引入模块
from package1 import module1
print(module1.number)

# 3 从包中引入某个模块的功能
from package1.module1 import number
print(number)

#多级包目录引入
from package1.package11.module11 import number
print(number)
