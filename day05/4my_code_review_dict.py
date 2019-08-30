'''
字典
    是一个键值对的映射关系数据,字典的键只能使用不可变的数据类型：字符串，元组，数字

    无序
    格式:{key:value,key,value}

        dict()
        get()
        pop()
        popitem()
        clear()
        del
        setdefault() 如果键存在什么都不做，不存在添加
        len()
        keys()
        values()
        items()


        update()
'''

dic = dict(name='lala',age=90,like=['watch movies','chicken'])
{"a":1}

dict()
res = dic['name']
print(res)
dic['name'] = 'lalalala'
print(dic)
dic.update(name='haha')
dic.update(name="ha",age=18,phone='123')
print(dic)
# 返回键，删除键
res = dic.pop('age')
# print(res)
#返回键值对，随机删除一个
# res1 = dic.popitem()
# print(res1)

# keys = dic.keys()
# print(keys)
#
# for k in dic.keys():
#     print(k)
#
# for k,v in dic.items():
#     print(k,v)

# 检测当前键是否属于当前字典
# in
# not in
# result = 'name' in  dic
# print(result)


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([10, 5, 2, 3]))

print(1 or 2 and 3 and 4)

import os
import time
def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()