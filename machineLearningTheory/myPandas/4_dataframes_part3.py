import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]

# Creates tuples with the 2 vectors
# [('G1', 1), ('G1', 2), ('G1', 3), ('G2', 1), ('G2', 2), ('G2', 3)]
hier_index = list(zip(outside, inside))

# Creates a multilevel index
# levels=[['G1', 'G2'], [1, 2, 3]],
# codes=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 1, 2]]
#
# To understand:
# In the codes: 0 is G1 and 1 is G2
# In the codes: 0 is 1, 1 is 2, 2 is 3
hier_index = pd.MultiIndex.from_tuples(hier_index)
print("\n", hier_index)

# We have two indexes
# First index: G1 and G2
# Sublevel index: 1,2,3
#               A         B
# G1 1  2.706850  0.628133
#    2  0.907969  0.503826
#    3  0.651118 -0.319318
# G2 1 -0.848077  0.605965
#    2 -2.018168  0.740122
#    3  0.528813 -0.589001
df = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])

# Get the rows G1
#           A         B
# 1  2.706850  0.628133
# 2  0.907969  0.503826
# 3  0.651118 -0.319318
G1 = df.loc['G1']

# Get the row 1 of G1
# A    2.706850
# B    0.628133
G1_1 = df.loc['G1'].loc[1]


# Name your indexes columns
#                    A         B
# Groups Num
# G1     1    2.706850  0.628133
#        2    0.907969  0.503826
#        3    0.651118 -0.319318
# G2     1   -0.848077  0.605965
#        2   -2.018168  0.740122
#        3    0.528813 -0.589001
df.index.names = ['Groups', 'Num']


# We can now select individual cells
# 0.7401220570561068
G2_2_B = df.loc['G2'].loc[2]['B']

# Return a cross series of rows or columns when you have a multi level index
# We want a all rows where Num = 1
# Groups
# G1      2.706850  0.628133
# G2     -0.848077  0.605965
num_equal_1 = df.xs(1, level='Num')
print(num_equal_1)
