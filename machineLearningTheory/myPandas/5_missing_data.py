import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

# np.nan is NaN
# {'A': [1, 2, nan], 'B': [5, nan, nan], 'C': [1, 2, 3]}
data = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}

#      A    B  C
# 0  1.0  5.0  1
# 1  2.0  NaN  2
# 2  NaN  NaN  3
df = pd.DataFrame(data)

# Drop all rows that have NaN in it
#      A    B  C
# 0  1.0  5.0  1
no_NaN_rows = df.dropna()

# Drop all columns that have NaN in it
#    C
# 0  1
# 1  2
# 2  3
no_NaN_columns = df.dropna(axis=1)

# Drop all columns that have at least 2 NaN values in it
# If it has only one NaN it is ok
#      A  C
# 0  1.0  1
# 1  2.0  2
# 2  NaN  3
no_2_NaN = df.dropna(thresh=2, axis=1)


#                         A                       B  C
# 0                       1                       5  1
# 1                       2  FILL VALUE replacement  2
# 2  FILL VALUE replacement  FILL VALUE replacement  3
replacedNaN = df.fillna(value='FILL VALUE replacement')
print(replacedNaN)

# Fill NaN of A column with the mean value of A
# 0    1.0
# 1    2.0
# 2    1.5
replaceNaN_with_mean = df['A'].fillna(value=df['A'].mean())
print(replaceNaN_with_mean)
