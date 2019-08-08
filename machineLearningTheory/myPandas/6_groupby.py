import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

data={'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'], 'Person': [
    'Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'], 'Sales': [200, 120, 340, 124, 243, 350]}

#   Company   Person  Sales
# 0    GOOG      Sam    200
# 1    GOOG  Charlie    120
# 2    MSFT      Amy    340
# 3    MSFT  Vanessa    124
# 4      FB     Carl    243
# 5      FB    Sarah    350
df = pd.DataFrame(data)

# Define the group in a object
# You have not defined any operation so there is no result
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x7ffa14b61780>
byCompanyObject = df.groupby('Company')

# Mean of the values by company
#          Sales
# Company       
# FB       296.5
# GOOG     160.0
# MSFT     232.0
byCompanyMean = byCompanyObject.mean()

# Sums of the values by company
#          Sales
# Company       
# FB         593
# GOOG       320
# MSFT       464
byCompanySum = byCompanyObject.sum()

# Standard deviation of the values by company
#               Sales
# Company            
# FB        75.660426
# GOOG      56.568542
# MSFT     152.735065
byCompanyStandardDev = byCompanyObject.std()

# Minimum values by company
#           Person  Sales
# Company                
# FB          Carl    243
# GOOG     Charlie    120
# MSFT         Amy    124
byCompanyMin = df.groupby("Company").min()

# Standard deviation for FaceBook
# Sales    75.660426
FBStandardDev = byCompanyObject.std().loc['FB']

# Full line
# Sums of the values by for FaceBook 
# Sales    593
FBSum = df.groupby('Company').sum().loc['FB']


# A lot of informations in one shot in rows
#         Sales                                                        
#         count   mean         std    min     25%    50%     75%    max
# Company                                                              
# FB        2.0  296.5   75.660426  243.0  269.75  296.5  323.25  350.0
# GOOG      2.0  160.0   56.568542  120.0  140.00  160.0  180.00  200.0
# MSFT      2.0  232.0  152.735065  124.0  178.00  232.0  286.00  340.0
describeByCompany = df.groupby('Company').describe()

# A lot of informations in one shot in columns
# Company              FB        GOOG        MSFT
# Sales count    2.000000    2.000000    2.000000
#       mean   296.500000  160.000000  232.000000
#       std     75.660426   56.568542  152.735065
#       min    243.000000  120.000000  124.000000
#       25%    269.750000  140.000000  178.000000
#       50%    296.500000  160.000000  232.000000
#       75%    323.250000  180.000000  286.000000
#       max    350.000000  200.000000  340.000000
describeByCompany = df.groupby('Company').describe().transpose()

