import numpy as np  

class datatype: 
    def data1(self):
        arr = np.array([12,32,1])
        print(arr)
        print(type(arr)) 
    
    def data2(self):
        arr = np.array([12,11,23,"fw",True,2.0,2j])
        print(arr) 
        print(type(arr))
    
    def data3(self):
        arr = np.array(['heloo','hi','what'])
        print(arr)
        print(type(arr))

    def data4(self):
        arr = np.array([1,2,3,4,5],dtype='S')
        print(arr)
        print(type(arr))

    def data5(self):
        arr = np.array([1,2,3,4,5],dtype='uint8')
        print(arr)
        print(type(arr))

    def data6(self):
        arr = np.array([1,2,3,4,5],dtype='i4')
        print(arr)
        print(type(arr))
    
    def data7(self):
        arr = np.array([1.2,1.23,5.2,12.8])
        cparr = arr.astype('i')
        print(arr)
        print(cparr)
        print(cparr.dtype)

    def data8(self):
        arr = np.array([1.1,1.2,1.3,1.4])
        cparr = arr.astype(int)
        print(arr)
        print(cparr)
        print(arr.dtype)
        print(cparr.dtype)
    
    def data9(self):
        arr = np.array([1,0,2,4,])
        cparr = arr.astype(bool)
        print(arr)
        print(cparr)
        print(arr.dtype)
        print(cparr.dtype)

obj = datatype()
# obj.data1()
# obj.data2()
# obj.data3()
# obj.data4()
# obj.data5()
# obj.data6()
# obj.data7()
obj.data8()
obj.data9()