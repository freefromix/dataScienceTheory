#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 18:06:47 2019

@author: julien
"""
import pandas as pd


my_data = pd.read_csv('data/home.csv',names=["size","bedroom","price"])

# We need to normalize the features using mean normalization
my_data = (my_data - my_data.mean())/my_data.std()

print(my_data.columns)

X = my_data[['size', 'bedroom']]
y = my_data['price']

print(X.shape)
print(y.shape)

from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X, y)

print("theta0:", lm.intercept_)
print("theta1:", lm.coef_[0])
print("theta2:", lm.coef_[1])

### Comparing these matrics
from sklearn import metrics
predictions = lm.predict(X)
mse=metrics.mean_squared_error(y, predictions)
print("\nfinalCost:",mse)
