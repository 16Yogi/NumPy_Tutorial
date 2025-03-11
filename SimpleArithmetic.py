# import numpy as np   

# arr1 = np.array([1,2,3,4])
# arr2 = np.array([5,6,7,8])

# res = np.add(arr1,arr2)
# print(res)   



# import numpy as np    

# arr1 = np.array([1,2,3,4])
# arr2 = np.array([5,6,7,8])

# res = np.subtract(arr1,arr2)

# print(res)

import numpy as np 
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

def mul(a,b):
    return np.multiply(a,b)  
print(mul(a,b))

def div(a,b):
    return np.divide(a,b) 
print(div(a,b)) 

def pow(a,b):
    return np.power(a,b)  
print(pow(a,b))  

def mod(a,b):
    return np.mod(a,b)  
print(mod(a,b))

def rem(a,b):
    return np.remainder(a,b)  
print(rem(a,b))

