Python:
```python
import csv
import matplotlib.pyplot as plt
import numpy as np

with open('/home/julien/tmp/R/DataSets/Advertising.csv') as csvDataFile:
    # Import
    csvReader = csv.reader(csvDataFile)
    headers = next(csvReader, None)
    print('-----------headers-----------')
    print(headers)
    print('-----------------------------')
    column = {}
    for h in headers:
        column[h] = []
    for row in csvReader:
        for h, v in zip(headers, row):
            column[h].append(v)

    # code starts here

    X = np.array(column['TV']).astype(np.float)
    Y = np.array(column['sales']).astype(np.float)

    print('--------------')
    Xmean = np.mean(X, axis=0)
    Ymean = np.mean(Y, axis=0)

    print('Xmean = ', Xmean)
    print('Ymean = ', Ymean)

    beta1,beta0 = np.polyfit(X, Y, 1)
    
    # above = 0
    # below = 0

    # for i in range(0, len(X)):
    #    above = above + (X[i]-Xmean)*(Y[i]-Ymean)
    #    below = below + (X[i]-Xmean)**2

    # beta1 = above/below
    # beta0 = Ymean-beta1*Xmean

    print('-----------')

    print('beta1 =', beta1)
    print('beta0 =', beta0)

    print('########plot########')
    simpleLinearRegressionValues = []
    for i in range(0, len(X)):
        simpleLinearRegressionValues.append(beta1*X[i]+beta0)

    # fig, ax = plt.subplots()
    # ax.plot(X, Y, 'o', X, simpleLinearRegressionValues, '.')
    # plt.show()

    plt.scatter(X, Y, label='sales TV', color='B')
    plt.plot(X, simpleLinearRegressionValues, label='Simple linear regression', color='R')
    plt.title("Simple Plot")
    plt.legend()
    plt.show()

```

R:
```
Advertising <- read.csv("~/tmp/R/DataSets/Advertising.csv")
TV <- Advertising[,"TV"]
sales <- Advertising[,"sales"]

TVMean <- mean(TV)
salesMean <- mean(sales)

print('TVMean')
print(TVMean)
print('salesMean')
print(salesMean)

above <- 0
below <- 0

for (i in 1:length(TV)) {
    above <- above+(TV[i]-TVMean)*(sales[i]-salesMean)
    below <- below+(TV[i]-TVMean)**2
}

print('-------------')
beta1=above/below
beta0=salesMean-beta1*TVMean

print('beta1')
print(beta1)
print('beta0')
print(beta0)
```