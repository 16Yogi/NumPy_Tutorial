import numpy as np  

class higherDie:
    def __init__(self):
        arr = np.array([1,2,3,4],ndmin=5)
        print(arr)
        print(arr.ndim)

obj = higherDie()