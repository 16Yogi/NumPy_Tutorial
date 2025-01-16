# from numpy import random 
# x = random.exponential(scale=3,size=(4,9))
# print(x)

from numpy import random
import matplotlib.pyplot as plt    
import seaborn as sns  
sns.displot(random.exponential(scale=3,size=(4,9)))
sns.displot(random.exponential(scale=2,size=(4,3)))

plt.show()