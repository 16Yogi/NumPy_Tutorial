import numpy as np   

class shapeArr:
    def arr1(self):
        arr = np.array([[1,2,3,4,5],[11,22,33,44,55],[111,222,333,444,555]])
        print(arr.shape) 
    
    def arr2(self):
        arr = np.array([1,2,3,4,5], ndmin=5) 
        print(arr)
        print(arr.shape)

obj = shapeArr()
# obj.arr1()
obj.arr2()