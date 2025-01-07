import numpy as np  
class iterArr:
    def arr1(self):
        arr = np.array([1,2,3,4,5])
        for i in arr: 
            print(i)  

    def arr2(self):
        arr = np.array([[1,2,3,4],[11,22,33,44]])
        for i in arr:
            print(i)
    
    def arr3(self):
        arr = np.array([[1,2,3,4],[11,22,33,44]])
        for i in arr:
            for j in i:
                print(j)
    
    def arr4(self):
        arr = np.array([[1,2,3,4],[11,22,33,44]])
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                print(f"{i} : {j}")
                print(arr[i][j]) 
    
    def arr5(self):
        arr = np.array([[1,2,3,4],[11,22,33,44]])
        # cparr = arr.shape[1]
        # print(cparr)
        for i in range(arr.shape[0]):
            for j in range(arr.shape[1]):
                print(arr[i][j])
                print(f"{i} : {j}")

    def arr6(self):
        arr = np.array([[
            [1,2,3,4],[11,22,33,44],[111,222,333,444]
        ]])
        print(arr[0][2][1])
        for i in arr: 
            for j in i:
                for k in j:
                    print(k)

    def arr7(self):
        arr = np.array([[
            [1,2,3,4],[11,22,33,44],[111,222,333,444]
        ]])
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                for k in range(len(arr[i])):
                    print(f"{i} : {j} : {k}")
                    print(arr[i][j][k])
    
    def arr8(self):
        arr = np.array([[
            [1,2],[11,22]],
            [[111,222],[1111,2222]]
        ])
        for i in np.nditer(arr):
            print(i)
    
    def arr9(self):
        arr = np.array([1,2,3])
        for i in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
            print(i)

    def arr10(self):
        arr = np.array([[1,2,3],[11,22,33]])
        for i in np.nditer(arr[:,::2]): #(:,:) (::)
            print(i)
    
    def arr11(self):
        arr = np.array([1,2,3])
        for idx,i in np.ndenumerate(arr): #need to 2 array 1st is index and 2nd is value
            print(idx,i)
    
    def arr12(self):
        arr = np.array([[1,2,3],[11,22,33]])
        for idx,i in np.ndenumerate(arr):
            print(idx,i)
        

obj = iterArr()
# obj.arr1()
# obj.arr2()
# obj.arr3()
# obj.arr4()
# obj.arr5()
# obj.arr6()
# obj.arr7()
# obj.arr8()
# obj.arr9()
# obj.arr10()
# obj.arr11()
obj.arr12()