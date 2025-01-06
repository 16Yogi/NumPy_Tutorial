import numpy as np

class cpArray:
    def arr1(self):
        arr = np.array([1,2,3,4,5])
        cparr = arr.copy()
        arr[0] = 100 
        print(arr)
        print(cparr)
    
    def arr2(self):
        arr = np.array([1,2,3,4,5])
        cparr = arr.view()
        arr[1] = 45
        print(arr)
        print(cparr)

    def arr3(self):
        arr = np.array([1,2,3,4,5])
        cparr = arr.copy()
        arr[0] = 20
        cp2arr = arr.view()
        arr[0] = 100 #overlap
        print(arr)
        print(cparr)
        print(cp2arr)
        print(cparr.base) 
        print(cp2arr.base)

obj = cpArray()
# obj.arr1()
# obj.arr2()
obj.arr3()