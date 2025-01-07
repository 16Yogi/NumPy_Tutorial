import numpy as np

class sortCls:
    def arr1(self):
        arr1 = np.array([231,32,54,1,43,4,12])
        cparr = np.sort(arr1)
        print(cparr)
    
    def arr2(self):
        arr1 = np.array(['hello','chalo','oyo','ayehaye'])
        cparr = np.sort(arr1)
        print(cparr)
        print(np.sort(arr1))
    
    def arr3(self):
        arr3 = np.array([True,False,True,False])
        print(np.sort(arr3))
    
    def arr4(self):
        arr4 = np.array([1,'Helo',2.4,True])
        print(np.sort(arr4))

    def arr5(self):
        arr5 = np.array([[4,3,2,1],[33,44,11,22]])
        print(np.sort(arr5))

obj = sortCls()
# obj.arr1()
# obj.arr2()
# obj.arr3()
# obj.arr4()
obj.arr5()