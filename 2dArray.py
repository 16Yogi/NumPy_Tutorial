import numpy as np  

class arr2D:
    def __init__(self):
        arr = np.array([[1,2,3,4],[11,22,33,44]]) 
        print(arr) 
        print(arr[1][0])
        print(arr[0][1])
        for i in arr:
            print(i) 
obj = arr2D()