import numpy as np   

class concatcls:

    def arr1(self):
        arr1 = np.array([1,2,3])
        arr2 = np.array([11,22,33])
        arr3 = np.concatenate((arr1,arr2))
        print(arr3)

    def arr2(self):
        arr1 = np.array([1,2,3])
        arr2 = np.array([11,22,33])
        arr3 = arr1 + arr2  
        print(arr3)

    def arr3(self):
        arr1 = np.array([[1,2,3],[11,22,33]])
        arr2 = np.array([[111,222,333],[1111,2222,3333]])
        # arr3 = np.concatenate((arr1,arr2),axis=1)
        arr3 = np.concatenate((arr1, arr2), axis=1)
        print(arr3)

    def arr4(self):
        arr1 = np.array([1,2,3])
        arr2 = np.array([11,22,33])
        arr3 = np.stack((arr1,arr2),axis=1)
        print(arr3)
    
    def arr5(self):
        arr1 = np.array([1,2,3])
        arr2 = np.array([11,22,33])
        arr3 = np.hstack((arr1,arr2))
        print(arr3)
    
    def arr6(self):
        arr1 = np.array([1,2,3])
        arr2 = np.array([11,22,33])
        arr3 = np.vstack((arr1,arr2))
        print(arr3)
    
    def arr7(self):
        arr1 = np.array([1,2,3])
        arr2 = np.array([11,22,33])
        arr3 = np.dstack((arr1,arr2))
        print(arr3)
    
obj = concatcls()
# obj.arr1()
# obj.arr2()
# obj.arr3()
# obj.arr4()
# obj.arr5()
# obj.arr6()
obj.arr7()