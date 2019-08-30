def binary_search(item, list1):
    st = 0
    ed = len(list1) - 1
    mid = (st + ed) // 2

    while st <= ed:
        if list1[mid] == item:
            return mid
        elif list1[mid] < item:
            st = mid + 1
        elif list1[mid] > item:
            ed = mid - 1

    return -1

def binary_search_digui(st,ed,item, list1):
    mid = (st + ed) // 2
    if st > ed:
        return -1
    if item == list1[mid]:
        return mid
    elif item > list1[mid]:
        binary_search_digui(mid+1,ed,item,list1)
    else:
        binary_search_digui(st,mid-1,item,list1)

index = binary_search(5, [1, 2, 3, 4, 5, 9, 13, 14, 15])
print(index)

