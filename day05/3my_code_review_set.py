'''
集合
    无序，且唯一，
    格式 {val,val,val}

    add()
    update()
    pop()
    del
    remove()

'''

myset = {1,2,3}

myset.add('a')

myset.update({'a','b','c'})
print(myset)
#pop 随机删除  返回值
res = myset.pop()
#remove 删除指定元素，无返回值
myset.remove('a')
print(myset)




'''

pop(), list set dict tuple
del(), list set dict tuple
remove() list set
index(),list,tuple
count(),list,tuple
len() ,list set dict tuple
add() set
update() set,dict
popitem() dict
'''