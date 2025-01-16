# from numpy import random
# x = random.poisson(lam=2,size=10)
# print(x)


# from numpy import random
# import matplotlib.pyplot as plt 
# import seaborn as sns  

# sns.displot(random.poisson(lam=2,size=10)) 
# sns.displot(random.poisson(lam=4,size=20))  

# plt.show()


# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
# sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')
# plt.show()



from numpy import random   
import matplotlib.pyplot as plt  
import seaborn as sns  
sns.distplot(random.binomial(n=1000, p=0.01, size=1000), hist=False, label='binomial')
sns.distplot(random.poisson(lam=10, size=1000), hist=False, label='poisson')
plt.show()