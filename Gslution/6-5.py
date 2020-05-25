
friend={}
friend["you"]=["alice","bob","claire"]

from collections import deque
search_quene= deque()

search_quene += friend["you"]

print(search_quene)
# dir(deque)打印所有方法

while search_quene :
    get_person=search_quene.popleft()
    if person_is_seller(get_person):
        print("he is seller ")
         
         
    else:
        search_quene += friend[get_person]
         

def person_is_seller(name):

    return name[-1] == 'm' 

'''
参考：

> https://www.cnblogs.com/zhenwei66/p/6598996.html

'''






































