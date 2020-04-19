
'''
add date with loop

'''
"""
def sum(arr):
    tatal = 0
    for x in arr:
        #tatal +=x
        tatal=tatal +x
    return tatal

print(sum([1,2,3,4]))
"""
def sum(arr):
    if arr ==[]:
        return 0
    return arr[0] + sum(arr[1:])
    

print(sum([1,2,3,4]))
