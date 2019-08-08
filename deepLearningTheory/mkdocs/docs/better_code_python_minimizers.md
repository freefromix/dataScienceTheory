```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

xValues=2.5*np.random.randn(100)+1.5
residualErrorValues=.5*np.random.randn(100)+0
yPredictiveValues=2+.3*xValues
yActualValues=2+.3*xValues+residualErrorValues
xmean=np.mean(xValues)
ymean=np.mean(yActualValues)
xlist=xValues.tolist()
yAverage=[ymean for i in range(1,len(xlist)+1)]

df=pd.DataFrame({'x values':xValues, 'residual error values':residualErrorValues, '
y actual values': yActualValues, 'y predictive values': yPredictiveValues})

df['above']=(df['x values']-xmean)*(df['y actual values']-ymean)
df['below']=(df['x values']-xmean)**2

beta1=df.sum()['above']/df.sum()['below']
beta0=ymean-beta1*xmean

print('beta1')
print(beta1)
print('beta0')
print(beta0)

df['model']=beta0+beta1*df['x values']
plt.plot(xValues,yPredictiveValues, color='red')
plt.plot(xValues,yActualValues,'ro', color='black')
plt.plot(xValues,df['model'], color='blue')
plt.plot(xValues,yAverage, color='orange')

plt.title('Actual (Black) vs Predicted (red) vs Model beta0 beta1(blue) vs yActualA
verage (orange)')
plt.show()

```