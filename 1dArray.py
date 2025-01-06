import numpy as np   

class arr1d:
    def __init__(self):
        arr = np.array([12,321,23,431,233]) 
        print(arr)
        print(type(arr))
        for i in arr:
            print(i,end=" ")
obj = arr1d()