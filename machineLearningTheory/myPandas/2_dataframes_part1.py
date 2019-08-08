import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df)
print("\n------columns index--------")

# Index(['W', 'X', 'Y', 'Z'], dtype='object')
columns_index = df.columns
print(columns_index)

print("\n------call columns--------")

# Index(['A', 'B', 'C', 'D', 'E'], dtype='object')
index = df.index

# return the column W
df['W']
# You can also call df.W but this not recommended (too confusing)
df.W
# Call two columns
wx = df[['W', 'X']]

print("\n------call rows--------")

# Index(['A', 'B', 'C', 'D', 'E'], dtype='object')
rows_index = df.index

# Call a row
rowab=df.loc[['A', 'B']]
# Or with an index
rowc=df.iloc[2] # row['C']

print("\n####### Call a subset of columns or rows ######")
rowab_columnswy=df.loc[['A', 'B'], ['W', 'Y']]
print(rowab_columnswy)

print("\n------Add drop columns------")
# Create a new column
df['new col'] = df['W'] + df['X']
print(df)

# Drop a new column
# axis=0 -> rows          axis=1 -> columns
# inplace=True  is for panda to be sure that you won't loose information
df.drop('new col', axis=1, inplace=True)
print(df)

print('Drop row A')
df.drop('A', axis=0, inplace=True)
print(df)

