import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)


#           W         X         Y         Z
# A  2.706850  0.628133  0.907969  0.503826
# B  0.651118 -0.319318 -0.848077  0.605965
# C -2.018168  0.740122  0.528813 -0.589001
# D  0.188695 -0.758872 -0.933237  0.955057
# E  0.190794  1.978757  2.605967  0.683509
df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

# Returns a matrix of booleans matching the request >0
#       W      X      Y      Z
# A   True   True   True   True
# B   True  False  False   True
# C  False   True   True  False
# D   True  False  False   True
# E   True   True   True   True
booldf = df > 0

# Returns the values > 0 or NaN if <=0
#           W         X         Y         Z
# A  2.706850  0.628133  0.907969  0.503826
# B  0.651118       NaN       NaN  0.605965
# C       NaN  0.740122  0.528813       NaN
# D  0.188695       NaN       NaN  0.955057
# E  0.190794  1.978757  2.605967  0.683509
df[df > 0]

# df['X'] returns a boolean column
# df[df['X'] returns ONLY rows that are true
#           W         X         Y         Z
# A  2.706850  0.628133  0.907969  0.503826
# C -2.018168  0.740122  0.528813 -0.589001
# E  0.190794  1.978757  2.605967  0.683509
allsrowstrue = df[df['X'] > 0]
print(df)
print(df['X'] > 0)
print(allsrowstrue)
print("##############################")

# In dataframes:
# and is &
# or is |
# You cannot use 'and' that is only for single booleans
# In dataframes you have to use the symbol '&'
#           W         X         Y         Z
# A  2.706850  0.628133  0.907969  0.503826
# C -2.018168  0.740122  0.528813 -0.589001
# E  0.190794  1.978757  2.605967  0.683509
#           W         X         Y         Z
# E  0.190794  1.978757  2.605967  0.683509
isand = df[(df['W'] > 0) & (df['Y'] > 1)]

# Making your old index be a column in your dataframe and add a new numerical index
#   index         W         X         Y         Z
# 0     A  2.706850  0.628133  0.907969  0.503826
# 1     B  0.651118 -0.319318 -0.848077  0.605965
# 2     C -2.018168  0.740122  0.528813 -0.589001
# 3     D  0.188695 -0.758872 -0.933237  0.955057
# 4     E  0.190794  1.978757  2.605967  0.683509
df.reset_index(inplace=True)

#########
# Let's restart 
#########
df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

# Add a new column 'States' with values
#           W         X         Y         Z States
# A  0.302665  1.693723 -1.706086 -1.159119     CA
# B -0.134841  0.390528  0.166905  0.184502     NY
# C  0.807706  0.072960  0.638787  0.329646     WY
# D -0.497104 -0.754070 -0.943406  0.484752     OB
# E -0.116773  1.901755  0.238127  1.996652     CO
newcol = 'CA NY WY OB CO'.split()
df['States'] = newcol

# Make the new column 'States' an index
#                W         X         Y         Z
# States                                        
# CA      0.302665  1.693723 -1.706086 -1.159119
# NY     -0.134841  0.390528  0.166905  0.184502
# WY      0.807706  0.072960  0.638787  0.329646
# OB     -0.497104 -0.754070 -0.943406  0.484752
# CO     -0.116773  1.901755  0.238127  1.996652
df.set_index('States', inplace=True)

