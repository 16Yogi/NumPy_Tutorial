import numpy as np   

class arrSlicing: 
    def __init__(self):
        arr = np.array([12,23,12,3,23])
        arr1 = np.array([[1,2,3,4],[11,22,33,44]])
        print(arr[0:2])
        print(arr[1:4])
        print(arr[-1:0])
        print(arr[::1])
        print(arr1[0:1,2])
obj = arrSlicing()