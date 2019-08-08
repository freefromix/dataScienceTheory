"""This module calculate the beta0 and beta1 values of a simple linear regression using least squares ( minimize the Residual sum of squares )

This is a demo program to see linear regression in action.

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def createRealValuesSample():
    """Create a sample of 100 random values for x, y and residualErrorValues

    Args:

    Returns:
        xValues: 100 random values for x
        yValues: 100 random values for y
        residualErrorValues: 100 random values for residualErrorValues
    """
    xValues = 2.5*np.random.randn(100)+1.5
    residualErrorValues = .5*np.random.randn(100)+0
    yValues = 2+.3*xValues+residualErrorValues
    return xValues, yValues, residualErrorValues


def createHatValuesSample(xValues):
    """Create a sample of 100 random for yHat

    Args:
        xValues: random values for x
    Returns:
        yHatValues: random values for yHat
    """
    yHatValues = 2+.3*xValues
    return yHatValues


def calculateNpMean(npArray):
    return np.mean(npArray)


def calculateLeastSquares(xValues, yValues):
    """ Simple regression, calculate Least Squares Beta0 and Beta1

    Parameters::
       xValues: xValues
       yValues: yValues

    Returns:
       beta0: beta0
       beta1: beta1
    """
    xmean = calculateNpMean(xValues)
    ymean = calculateNpMean(yValues)

    df = pd.DataFrame({'x values': xValues, 'y values': yValues})

    df['above'] = (df['x values']-xmean)*(df['y values']-ymean)
    df['below'] = (df['x values']-xmean)**2

    beta1 = df.sum()['above']/df.sum()['below']
    beta0 = ymean-beta1*xmean

    return beta0, beta1


def plotAllValues(xValues, yValues, residualErrorValues, yHatValues, beta0, beta1):

    df = pd.DataFrame({'x values': xValues, 'residual error values': residualErrorValues,
                       'y values': yValues, 'y predicted values': yHatValues})

    df['model'] = beta0+beta1*df['x values']
    plt.plot(xValues, yHatValues, color='red')
    plt.plot(xValues, yValues, 'ro', color='black')
    plt.plot(xValues, df['model'], color='blue')

    ymean = calculateNpMean(yValues)
    xlist = xValues.tolist()
    yAverage = [ymean for i in range(1, len(xlist)+1)]
    plt.plot(xValues, yAverage, color='orange')

    plt.title(
        'Actual (Black) vs Predicted (red) vs Model beta0 beta1(blue) vs yActualAverage (orange)')
    plt.show()


if __name__ == '__main__':
    x, y, residualError = createRealValuesSample()
    yHat = createHatValuesSample(x)

    beta0, beta1 = calculateLeastSquares(x, y)

    plotAllValues(x, y, residualError,
                  yHat, beta0, beta1)

    print('Formula simple linear regression: beta1*x + beta0')
    print('beta1:', beta1)
    print('beta0:', beta0)
    print('simple linear regression: ' + str(beta1)+'x + '+str(beta0))
