"""
what: quick sort
"""
def quicksort(arr):
    if len(arr)<2:
        return arr
    else:
        base_arr=arr[0]
        smaller =[i for i in arr[1:] if i<base_arr]
        biger = [i for i in arr[1:] if i>base_arr]
        return quicksort(smaller) +[base_arr]+quicksort(biger)

print(quicksort([10,1,4,5,7,2]))


