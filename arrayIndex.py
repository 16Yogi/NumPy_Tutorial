import numpy as np  

class arrIndex:
    def arr1d(self):
        arr = np.array([12,23,1,645,3])
        print(arr[1]) 
        for i in range(len(arr)):
            print(arr[i])  
    
    def arr2d(self):
        arr = np.array([[1,2,23,4,12],[2,1,4,1,345]])
        print(arr[1][2])
        # for i in range(len(arr)): 
        #     for j in range(len(arr[i])):  
        #         print(arr[i][j], end=" ")
        #     print()

        for i in range(len(arr)):
            for j in range(len(arr[i])):
                print(arr[i][j],end=" ")
            print("")
    
    def arr3d(self):
        arr = np.array([
                    [[1, 2, 3], [11, 22, 33]],  
                    [[111, 222, 333], [1111, 2222, 3333]]  
                ])
        print(arr[1][1][0])

obj = arrIndex()
# obj.arr1d()
# obj.arr2d()
obj.arr3d()        