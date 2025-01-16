# from numpy import random
# x = random.multinomial(n=6,pvals=[1/6,1/6,1/6,1/6,1/6,1/6])
# print(x)


from numpy import random
import matplotlib.pyplot as plt     
import seaborn as sns   

sns.displot(random.multinomial(n=6,pvals=[1/6,1/6,1/6,1/6,1/6,1/6]))

plt.show()