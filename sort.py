import pysnooper


@pysnooper.snoop()
def sm(list):
    if len(list) == 0 :
        return  0
    elif len(list) == 1:
        return list[0]
    else:
        return  sum(list[:])


print(sm([]))

# 快速排序一
@pysnooper.snoop()
def quicksort(list):
    if len(list ) < 2:
        return list
    else:
        arr = list[0]
        less = []
        more = []
        # 所有元素小于arr组成得基准值
        for i in list[1:]:
            if i < arr:
                less.append(i)
            else:
                more.append(i)
        return quicksort(less) + [arr] + quicksort(more)

a= [8,1,6,2,4,9]
print(quicksort(a))

# 快速排序二
def quicksort(list):
    if len(list)< 2:
        return list
    else:
        arr = list[0]
        less = [i for i in list[1:] if i < arr]
        more = [i  for i in list[1:] if i> arr]
        return quicksort(less) + [arr] + quicksort(more)

b= [9,1,5,2,8,3,6]
print(quicksort(b))


# 选择排序
def findSmallest(list):
    smallest = list[0]
    smallest_index = 0
    for i in range(1,len(list)):
        if list[i] < smallest:
            smallest = list[i]
            smallest_index = i
    return smallest_index


def selectSort(list):
    newList = []
    for i in range(len(list)):
        smallest = findSmallest(list)
        newList.append(list.pop(smallest))
    return newList

b= [9,5,2,8,3,6]
print(selectSort(b))


# 冒泡排序
def maopao(list):
    for j in range(len(list)-1 , 0 ,-1):
        for i in range(j):
            if list[i]> list[i +1]:
                list[i], list[i+1] = list[i +1], list[i]

b= [5,1,4,2,8,6]
maopao(b)
print(b)


# 插入排序
def insertSort(list):
    for j in range(1, len(list)):
        for i in range(j, 0 ,-1):
            if list[i] < list[i-1]:
                list[i], list[i-1] = list[i-1], list[i]


b = [5,1,4,2,8,6,45,20]
insertSort(b)
print(b)






























