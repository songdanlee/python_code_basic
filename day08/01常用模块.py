"""
1.常见的系统标准模块
    dir(模块)
        查看模块所包含的东西
    help(函数名)
        提示该函数的帮助文档

    random
        random()
            产生大于 0 且小于 1 之间的小数
        uniform(a,b)
            产生指定范围[a,b)内的随机小数
        randint(a,b)
            产生 a,b 范围内的整数，包含开头和结尾
        random.choice(lst)
            随机返回序列中的一个数据
        random.shuffle()#打乱源数据
            随机打乱列表顺序

    time  #calender
        表示时间的三种方式：

        1.时间戳（给计算机看的）
        time.time()
        2.字符串时间(给人看的)
        time.asctime()
        ret = time.strftime('%Y-%m-%d %H:%M:%S')
        3.元组时间(用来操作时间的)
        time.localtime()

        三种不同时间格式之间可以相互转换（课下查资料）

    sys

"""
import random

# print('randfloat' in dir(random))
# help(random.randint)
#
# def get_sum(a,b):
#     """
#     get sum with a and b;
#     :param a: 参数1
#     :param b: 参数2
#     :return: ->int   a 与 b的和
#     """
#     return a + b
#
# help(get_sum)
# list1 = [x for x in range(10)]#【0,1,2,3,4,5,6,7,8,9】
# # for i in range(5):
# #     print(random.random())
# #     print(random.uniform(1,10))
# #     print(random.choice(list1))
# random.shuffle(list1)
# print(list1)
import time
print(dir(time))
# print(60*60*24*365*100)
t = time.time()
print(t)
print(time.time()-60*60*24)
print(time.asctime())
t1 = time.localtime()
print(t1)
print(t1.tm_year,t1.tm_mon,t1.tm_mday,t1.tm_hour,t1.tm_min,t1.tm_sec)

time_now = time.strftime('%Y-%m-%d %H:%M:%S')
print(time_now)
