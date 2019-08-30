"""
冒泡排序：让子序列中的最大元素不断沉底，达到排序的目的。
冒泡排序一共经过N-1次遍历，其中第i次遍历前N-i个元素（第i+1到N个元素已经排序完毕），将第i大的元素移动到N-i的位置
"""
# lists = [2, 4, 1, 3, 0, 100, 23, 60]
#
# for i in range(len(lists) - 1):
#     for j in range(0, len(lists) - i - 1):
#         lists[j], lists[j + 1] = min(lists[j], lists[j + 1]), max(lists[j], lists[j + 1])
#
# # 优化
# # 如果进行某一趟排序时并没有进行数据交换，则说明所有数据已经有序，可立即结束排序，避免不必要的比较过程
#
# for i in range(len(lists) - 1):
#     flag = False
#     for j in range(len(lists) - 1 ,i,-1):
#         if lists[j] < lists[j - 1]:
#             flag = True
#             lists[j],lists[j-1] = lists[j-1],lists[j]
#     if not flag:
#         break
#
# print(lists)

# 选择排序，每次选择一个最小的放在当前未排序序列的首位
lists = [2, 4, 1, 3, 0, 100, 23, 60]


def selection_sort(li):
    for i in range(len(li)):
        index = li.index(min(li[i:]))
        li[i], li[index] = li[index], li[i]
    print(li)


# selection_sort(lists)

# arr = [1, 12, 2, 11, 13, 5, 6, 18, 4, 9, -5, 3, 11]


# def insertionSort(arr):
#     # 从要排序的列表第二个元素开始比较
#     for i in range(1,len(arr)):
#         j = i
#         # 从大到小比较，直到比较到第一个元素
#         while j > 0:
#             if arr[j] < arr[j-1]:
#                 arr[j-1],arr[j] = arr[j],arr[j-1]
#             j -= 1
#     return arr
# print(insertionSort(arr))


# 通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

# arr = [1, 12, 2, 11, 13, 5, 6, 18, 4, 9, -5, 3, 11]
#
# def insertsort(arr):
#     for i in range(1, len(arr)):
#         j = i
#         while j > 0:
#             if arr[j] < arr[j - 1]:
#                 arr[j], arr[j - 1] = arr[j - 1], arr[j]
#             j -= 1
#     return arr
#
#
# print(insertsort(arr))



arrx = [1, 12, 2, 11, 13, 5, 6, 18, 4, 2,9, -5, 3, 11]

def quick_sort(arr):
    if len(arr) < 0:
        return arr
    else:
        pivot = arr[0]
        small_arr = [i for i in arr[1:] if i < pivot]
        big_arr = [i for i in arr[1:] if i >= pivot]
        return quick_sort(small_arr) + [pivot] + quick_sort(big_arr)


print(quick_sort(arrx))
