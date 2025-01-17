# from numpy import random  
# x = random.rayleigh(scale=2,size=(2,3))
# print(x)


from numpy import random   
import matplotlib.pyplot as plt     
import seaborn as sns  
# sns.displot(random.rayleigh(scale=8,size=(2,3)))
sns.distplot(random.rayleigh(size=10), hist=False)

plt.show()