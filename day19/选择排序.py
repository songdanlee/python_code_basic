
def select_sort(list1):
    for i in range(len(list1)):
        min = i
        for j in range(i+1,len(list1)):
            if list1[min] > list1[j]:
                min = j
        list1[i],list1[min] = list1[min],list1[i]
        print(list1)

select_sort([10,9,8,7,6,5,4,3,2,1,0])