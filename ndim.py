import numpy as np  

class ndimArr:
    def __init__(self):
        arr1 = np.array(12)
        arr2 = np.array([12,321,31])
        arr3 = np.array([[123,321,3,13],[231,31,342,23]])
        arr4 = np.array([[12, 31, 321, 42], [314, 32, 32, 23]])
        arr5 = np.array([
            [[12, 32, 123, 432], [123, 422, 3, 0]],
            [[12, 123, 34, 12], [13, 54, 12, 523]]
        ])

        print(arr1.ndim)
        print(arr2.ndim) 
        print(arr3.ndim)
        print(arr4.ndim)
        print(arr5.ndim)
obj = ndimArr()