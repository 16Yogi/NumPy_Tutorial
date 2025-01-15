import numpy as np  
from numpy import random 

arr1 = np.array([1,2,12,33])
random.shuffle(arr1)
print(arr1)


arr2 = np.array([1,2322,12,423])
random.shuffle(arr2)
print(arr2)

arr3 = np.array([12,23,123,223,453])
print(random.permutation(arr3))
