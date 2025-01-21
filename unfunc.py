# a = [1,23,1,32,12]
# b = [32,1234,2,12,1]
# c = []
# for i, j in zip(a,b):
#     c.append(i+j)
# print(c)


import numpy as np  
a = np.array([13,2,234,2])
b = np.array([3,21,64,12])
c = np.add(a,b)  
print(c)