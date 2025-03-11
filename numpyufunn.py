import numpy as np 

def fun1():
    a = [1,2,3,4]
    b = [5,6,7,8]
    c = []
    
    for i,j in zip(a,b):
        c.append(i+j)
    print(c)

def fun2():
    a = [11,22,33,44]
    b = [111,222,333,444]
    c = []
    for i,j in zip(a,b):
        c.append(i+j)
    print(c)

def fun3():
    a = [1,2,3,4]
    b = [5,6,7,8]
    c = np.add(a,b)
    print(c)

# fun1()
# fun2()
# fun3()




