'''
数据类型
    数值 int:
            字符串转int,只能转纯数字组成的字符串
            小数，去掉小数部分
            bool，true 1 false 0
        float：
            字符串转float，要么是纯数字的字符串，要么是纯小数
            整型,在整数后加.0
            bool, True 1.0 false 0.0
        bool
            字符串，空字符串（"",''）为false，其他为真
            整型，0 为false 其他为true
            float 0.0 为false，其他为true
        二进制 0b
        八进制0o
        十六进制0x
    字符串

    列表:格式 lis = [1,'a',1.0,[1,2,3],{key:value},()]
        列表有序序列 + *
            varlist = [1,2,3]
            varlist1 = ['a','b','c']
            varlist + varlist1
            索引，列表中每一个元素都有一个索引，从0开始
            切片:[开始索引:结束索引:跳步值],跳步值默认为1 ，结束索引不包含
            方法:
                list()
                append()
                insert()
                pop()
                del
                remove()
                index()
                count()

                排序：sort()
                反转：reverse()
                    copy()
                    depcopy()
                    extend()


    元组
    集合
    字典

'''
li = [1,2,3,4,5]
# list() 类型转换
print(list("hello")) # ['h', 'e', 'l', 'l', 'o']
li.insert(1,'a')
li.reverse()
print(li)
# append() 追加
# li.append('a')
# print(li)
# insert(索引位置,插入元素)
# li.insert(0,'A')
# print(li)
# pop([索引值]) 弹出,有返回值，将弹出的元素返回,
# 默认弹出最后一个，也可以指定索引
# res = li.pop()
# print(res)
# print(li)
# remove(元素) 删除指定元素，无返回值
li.remove(1)

'''
del 
'''
# del li[0] # 删除列表中指定位置的元素
# del li # 删除列表

'''
index()  返回指定元素的索引值,从左向右找，找第一个的索引位置
'''
res = li.index(2)

# count() 返回元素出现次数
print(li.count(2))

if not None:
    print("123")
