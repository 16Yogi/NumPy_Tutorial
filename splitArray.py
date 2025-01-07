import numpy as np  

class splitArr:

    def arr1(self):
        arr1 = np.array([1,2,3,4,5,6,7,8])
        cparr = np.array_split(arr1,2)
        print(cparr) 

    def arr2(self):
        arr1 = np.array([1,2,3,4,5,6,7,8,9])
        cparr = np.array_split(arr1,2)
        print(cparr)
    
    def arr3(self):
        arr1 = np.array([1,2,3,4,5,6])
        cparr = np.split(arr1,2)  #it is not able to spilit when have extra value
        print(cparr)
    
    def arr4(self):
        arr1 = np.array([[1,2],[11,22],[111,222],[1111,2222],[11111,22222],[111111,222222]])
        cparr = np.array_split(arr1,2)
        print(cparr)
    
    def arr5(self):
        arr1 = np.array([[1,2],[11,22],[111,222],[1111,2222],[11111,22222],[111111,222222]])
        cparr = np.array_split(arr1,3,axis=1)
        print(cparr)
    
    def arr6(self):
        arr1 = np.array([[1,2],[11,22],[111,222],[1111,2222],[11111,22222],[111111,222222]])
        cparr = np.hsplit(arr1,2)
        print(arr1)


obj = splitArr()
# obj.arr1()
# obj.arr2()
# obj.arr3()
# obj.arr4()
# obj.arr5()
obj.arr6()