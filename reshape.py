import numpy as np  

class resharearr:
    def arr1(self):
        arr = np.array([1,2,3,4,5,6,7,8,9,10])
        cparr = arr.reshape(5,2)
        print(arr)
        print(cparr)
        cparr = arr.reshape(2,5)
        print(arr)
        print(cparr)
    
    def arr2(self):
        arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
        cparr = arr.reshape(2,3,2)
        print(arr)
        print(cparr)
        print("-------------------")
        cparr = arr.reshape(3,2,2)
        print(cparr)
    
    def arr3(self):
        arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
        # cparr = arr.reshape(2,6).base 
        print(arr)
        # print(cparr)
        print(arr.reshape(3,2).base)

    def arr4(self):
        arr = np.array([1,2,3,4,5,6,7,8])
        print(arr) 
        cparr = arr.reshape(4,2,-1)
        print(cparr)

    def arr5(self):
        arr = np.array([[1,2,3,4],[5,6,7,8]])
        print(arr)
        cparr = arr.reshape(-1)
        print(cparr)

obj = resharearr()
# obj.arr1()
# obj.arr2()
# obj.arr3()
# obj.arr4()
obj.arr5()