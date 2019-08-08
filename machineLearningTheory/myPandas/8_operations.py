import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

#    col1  col2 col3
# 0     1   444  abc
# 1     2   555  def
# 2     3   666  ghi
# 3     4   444  xyz
df = pd.DataFrame({'col1': [1, 2, 3, None],
                   'col2': [444, 555, 666, 444],
                   'col3': ['abc', 'def', 'ghi', 'xyz']})

# Returns the 5 first rows
df.head()

# Returns the unique values in col2
# [444 555 666]
df['col2'].unique()

# Number of unique numbers
# 3
df['col2'].nunique()

# Counts the number of times each values appears
# 444    2
# 555    1
# 666    1
df['col2'].value_counts()

#    col1  col2 col3
# 3     4   444  xyz
col1_sup_2_and_col2_eq_444 = df[(df['col1'] > 2) & (df['col2'] == 444)]

# 0    False
# 1    False
# 2     True
# 3     True
bool_values = df['col1'] > 2


def times2(x):
    return x*2


# Apply a function to a column
# 0    2
# 1    4
# 2    6
# 3    8
df['col1'].apply(times2)

# 0    3
# 1    3
# 2    3
# 3    3
df['col3'].apply(len)


# 0     888
# 1    1110
# 2    1332
# 3     888
df['col2'].apply(lambda x: x*2)

# Index(['col1', 'col2', 'col3'], dtype='object')
columns_index = df.columns

# RangeIndex(start=0, stop=4, step=1)
rows_index = df.index

# Sort the dataframe thanks to col2
#    col1  col2 col3
# 0     1   444  abc
# 3     4   444  xyz
# 1     2   555  def
# 2     3   666  ghi
dd = df.sort_values(by='col2')

#     col1
# 0  False
# 1  False
# 2  False
# 3   True
tmpdf = pd.DataFrame({'col1': [1, 2, 3, None]})
isnull = tmpdf.isnull()


data = pd.DataFrame({'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar', ],
                     'B': ['one', 'one', 'two', 'two', 'one', 'one'],
                     'C': ['x', 'y', 'x', 'y', 'x', 'y'],
                     'D': [1, 3, 2, 5, 4, 1], })

#      A    B  C  D
# 0  foo  one  x  1
# 1  foo  one  y  3
# 2  foo  two  x  2
# 3  bar  two  y  5
# 4  bar  one  x  4
# 5  bar  one  y  1
df = pd.DataFrame(data)

# The values are the D column
# The index are the A and B column
# My actual columns are defined by the C column
# C          x    y
# A   B            
# bar one  4.0  1.0
#     two  NaN  5.0
# foo one  1.0  3.0
#     two  2.0  NaN
pivot = df.pivot_table(values='D', index=['A', 'B'], columns=['C'])
print(pivot)