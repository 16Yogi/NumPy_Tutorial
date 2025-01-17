# from numpy import random 
# x = random.zipf(a=2,size=(2,5))
# print(x)


from numpy import random
import matplotlib.pyplot as plt    
import seaborn as sns 
sns.displot(random.zipf(a=2,size=(2,5)))  
plt.show()