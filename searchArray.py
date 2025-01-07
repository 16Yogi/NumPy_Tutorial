import numpy as np   

class searcharr:
    def arr1(self):
        arr1 = np.array([1,2,3,4,5,6])
        cparr = np.where(arr1==10)
        print(cparr)
    
    def arr2(self):
        arr1 = np.array([1,2,3,4,5,6])
        cparr = np.where(arr1==2)
        print(cparr)

    def arr3(self):
        arr1 = np.array([11,22,33,44,55,66,77,88])
        cparr = np.where(arr1%2==0)
        print(cparr)
        for i in cparr:
            print(arr1[i])

    def arr4(self):
        arr1 = np.array([11,22,33,44,55,66,77,88])
        cparr = np.where(arr1%2==1)
        print(cparr)
        for i in cparr:
            print(arr1[i])

            

obj = searcharr()
# obj.arr1()
# obj.arr2()
# obj.arr3()
obj.arr4()