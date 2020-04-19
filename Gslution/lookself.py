
import time
def countdown(i):
    print("have %d" %(i))
    #time.sleep(1)
    if i > 0:
        countdown(i-1)
    else:
        print("over Recursion")
         
countdown(100)
  
 