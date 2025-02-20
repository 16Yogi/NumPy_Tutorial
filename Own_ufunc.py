import numpy as np 

def fun1(a,b):
    return a+b 

fun1 = np.frompyfunc(fun1,2,1)
print(fun1([1,2,3,4,5],[6,7,8,9,10]))


print(type(np.add))
print(type.)
