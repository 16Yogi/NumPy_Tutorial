# from numpy import random  
# x = random.chisquare(df=2,size=(2,3))
# print(x)


from numpy import random  
import matplotlib.pyplot as plt 
import seaborn as sns 

sns.displot(random.chisquare(df=6,size=(2,3))) 

plt.show()
