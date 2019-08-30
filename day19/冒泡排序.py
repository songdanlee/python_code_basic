
# 冒泡排序，两两比较，大的放后面，比较n-1次（n元素个数）
#
def bull_sort(list1):
    for i in range(len(list1) - 1):
        flag = False
        for j in range(len(list1) - 1 - i):
            if list1[j] > list1[j + 1]:
                list1[j],list1[j + 1] = list1[j + 1],list1[j]
                flag = True
        if not flag:
            break

list1 = [0,1,-4,23,1002,33,4]
bull_sort(list1)
print(list1)