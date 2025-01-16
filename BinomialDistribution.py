# from numpy import random
# x = random.binomial(n=2,p=0.2,size=10) 
# print(x)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns 

sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)
sns.distplot(random.binomial(n=10, p=0.5, size=120), hist=False, kde=True)

plt.show()
