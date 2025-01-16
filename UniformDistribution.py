# from numpy import random 
# x = random.uniform(size=(2,3))
# print(x)


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.uniform(size=500), hist=False)
sns.distplot(random.uniform(size=1000), hist=True)

plt.show()
