# from numpy import random 
# x = random.logistic(loc=1,scale=10,size=(2,5))
# print(x)


from numpy import random
import matplotlib.pylab as plt     
import seaborn as sns    
sns.displot(random.logistic(loc=1,scale=10,size=(2,5)))  
plt.show()