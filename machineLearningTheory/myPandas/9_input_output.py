import pandas as pd
from sqlalchemy import create_engine


df = pd.read_csv('example.csv')

# write csv
df.to_csv('my_output.csv', index=False)

# You could read from an excel file
# conda install xlrd
# pd.read_excel('!Excel_Sample.xlsx', sheetname='Sheet1')
# df.to_excel('Excel_sample2.xlsx')


# Read html tables
data = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')

# list
type(data)

#                                            Bank Name  ...       Updated Date
# 0                Washington Federal Bank for Savings  ...   February 1, 2019
# 1    The Farmers and Merchants State Bank of Argonia  ...  February 21, 2018
# 2                                Fayette County Bank  ...   January 29, 2019
# 3  Guaranty Bank, (d/b/a BestBank in Georgia & Mi...  ...     March 22, 2018
# 4                                     First NBC Bank  ...   January 29, 2019
data[0].head()

# SQL #########

engine = create_engine('sqlite:///:memory:')

df.to_sql('my_table', engine)

sqldf = pd.read_sql('my_table', con=engine)

print(sqldf)




