"""
what：散列函数，python 中的字典
字典无序，制动扩容，头秃
"""
#book=dict()
book={}
flu={}
flu["a"]=2
flu["b"]=3
book["apple"]=flu
book["rice"]=7
print(book["rice"])
print(book.get("hello"))
 
print(book["apple"]["b"])
"""
---- book
     |
     ---flu
        |
        ---a
        ---b
----rice
"""