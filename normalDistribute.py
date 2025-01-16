# from numpy import random 
# x = random.normal(size=(23,65))
# print(x)


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(size=1000), hist=False)
sns.distplot(random.normal(size=100), hist=False)
sns.distplot(random.normal(size=20), hist=False)

plt.show()


