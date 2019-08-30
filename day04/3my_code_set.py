
# 定义集合

myset = {1,2,3,4,1,2,3,4}
print(myset)

#set 函数
# 将字符串转为集合
print(set('蔡徐坤'))
# 将列表转为集合
print(set(['a','b','c','a']))
# 将字典转换成集合
print(set({'name':'caicai','age':20}))

# 向元组添加内容
myset.add(7)
print(myset)
myset.update({7,8,9,0,'a'})
print(myset)

# 删除
print(myset.pop())
print(myset)
#remove  删除指定元素没有返回值
myset.remove('a')
print(myset)
# 清空
# myset.clear()

# 创建一个空集合，
# res = {} 创建空字典
res = set()

print("*"*20)
myset1 = {1,2,3}
myset2 = {3,4,5}
# 交集 & 获取集合共有的元素
print(myset1 & myset2)
# 反交集 ^,去掉两个集合重复的
print(myset1 ^ myset2)
#并集 | 集合除去重复的并在一起
print(myset2 | myset1)
# 差集 以某个集合为参照，去掉相同的，保留自己特有的
print(myset1 - myset2)

print("-"*20)
myset3 = {1,2}
myset4 = {1,2,4,6,2,3}
# 子集 返回bool
print(myset3 < myset4)
# 超集
print(myset3 > myset4)