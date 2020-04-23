'''
what: 选择排序
'''

def findsmall(arr):
    last_find_small_date =arr[0]
    last_find_small_index = 0
    for i in range(1,len(arr)):
        if arr[i] < last_find_small_date:
            last_find_small_date=arr[i]
            last_find_small_index = i
    return last_find_small_index,last_find_small_date

def selectionSort(arr):
    newARR=[]
    for i in range(len(arr)):
        index,date=findsmall(arr)
        arr.pop(index)#这个返回值有的别扭
        newARR.append(date)
    return newARR


#print([i for i in range(1,10)]) 
print(selectionSort([3,1,5,4,10]))
#print(findsmall([3,1,5,4,10]))
print(type([3,1,5,4,10]))