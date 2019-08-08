import seaborn as sns
import numpy as np
# Comes from here: https://github.com/mwaskom/seaborn-data

tips = sns.load_dataset('tips')

print(tips.head())



# Estimator is a function that you can pass to seaborn
# Here rather than showing the data in tips, it calculate the standard deviation from the data
# sns.barplot(x='sex', y='total_bill', data=tips, estimator=np.std)


# argument for matplotlib 
# bins is the number of grouping values. If there is 40 bins there will be 40 bars (except if some are 0).
# sns.distplot(tips['total_bill'], kde=True, bins=40)

# Add the number of total_bill at the top of the graph
# and add the number of tip on the right
# kind: reg = regression line
sns.jointplot(x='total_bill',y='tip', data=tips, kind='reg')

# kind: hex = hexagon representation
# More points, hexagone gets darker
# Less points, hexagone gets lighter
sns.jointplot(x='total_bill',y='tip', data=tips, kind='hex')




