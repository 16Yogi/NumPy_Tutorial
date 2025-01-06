import numpy as np 

class creatArr1:
    def __init__(self):
        arr = np.array([12,321,132,13,31,'wq'])
        print(arr)
        print(type(arr))
        for i in arr:
            print(i,end=" ")
        
# obj = creatArr1()


class arr2: 
    def __init__(self): 
        arr = np.array((12,32,32,213,543,31,"hrew"))
        print(arr,end=" ")
        print(type(arr))
        for i in arr:
            print(i,end=" ")  
obj = arr2()