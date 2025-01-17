# from numpy import random   
# x = random.pareto(a=2,size=(2,3))
# print(x)


from numpy import random  
import matplotlib.pyplot as plt    
import seaborn as sns 
sns.displot(random.pareto(a=2,size=(2,3)))                
plt.show()