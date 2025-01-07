import numpy as np   

class searchshort:
    def arr1(self):
        arr1 = np.array([11,22,33,1,2321,13,21,2,4,32,14,7,23])
        cparr = np.searchsorted(arr1,2)
        print(cparr)
        print(arr1[cparr])
        # for i in cparr:
            # print(arr1[i])

    def arr2(self):
        arr1 = np.array([11,22,33,1,2321,13,21,2,4,32,14,7,23])
        cparr = np.searchsorted(arr1,4,side='right')
        print(cparr)
        print(arr1[cparr])

    def arr3(self):
        arr1 = np.array([11,22,33,1,2321,13,21,2,4,32,14,7,23])
        cparr = np.searchsorted(arr1,[1,4,22])
        print(cparr)
        for i in cparr:
            print(arr1[i])

obj = searchshort()
# obj.arr1()
# obj.arr2()
obj.arr3()