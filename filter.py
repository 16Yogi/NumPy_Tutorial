import numpy as np   

class filterArr:
    def arr1(self):
        arr1 = np.array([11,2,24,32,3,56,123,87,90])
        arr2 = [True,False,True,False,True,True,False,True,True]
        cparr = arr1[arr2]
        print(cparr)

    def arr2(self):
        arr1 = np.array([11,2,24,32,3,56,123,87,90])
        filterArr = []
        for i in arr1:
            if i>=50:
                filterArr.append(True)
            else:
                filterArr.append(False)
        newarr = arr1[filterArr]
        print(filterArr)
        print(newarr)

    def arr3(self):
        arr1 = np.array([11,2,24,32,3,56,123,87,90])
        arr2 = []
        for i in arr1:
            if i%2==0:
                arr2.append(True)
            else:
                arr2.append(False)
        arr3 = arr1[arr2]
        print(arr3)
        print(arr2)

    def arr4(self):
        arr1 = np.array([11,2,24,32,3,56,123,87,90])
        arr2 = arr1<=50
        arr3 = arr1[arr2]
        print(arr3)
        print(arr2)

    def arr5(self):
        arr1 = np.array([11,2,24,32,3,56,123,87,90])
        arr2 = arr1%2==0 
        arr3 = arr1[arr2]
        print(arr3)
        print(arr2)

obj = filterArr()
# obj.arr1()
# obj.arr2()
# obj.arr3()
# obj.arr4()
obj.arr5()