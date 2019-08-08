#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 11:00:19 2019

@author: julien

SciPy Sigh Pie is a free and open-source Python library used for scientific computing and technical computing.
"""
import sklearn
import sklearn.datasets
import sklearn.linear_model
from planar_utils import plot_decision_boundary, load_planar_dataset
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    X, Y = load_planar_dataset()


    print("X.shape:", X.shape)
    print("Y.shape:", Y.shape)
    m = X.shape[1]
    print("Training set size m =", m)

    plt.scatter(X[0, :], X[1, :], c=Y[0, :], s=40, cmap=plt.cm.Spectral)
    
    # Train the logistic regression classifier m
    # cv: Cross Validation: It’s a model validation technique for assessing how the
    # results of a statistical analysis will generalize to anindependent data set.
    # Mainly used in settings where the goal is prediction and one wants
    # to estimate howaccurately a model will perform in practice.
    # The goal of cross-validation is to define a data set to test the model in
    # the training phase (i.e. validation data set) in order to limit problems
    # like overfitting, and get an insight on how the model will generalize
    # to an independent data set.
    # LogisticRegressionCV: The default cross-validation generator used is Stratified K-Folds
    # cv: If an integer is provided, then it is the number of folds used.
    # Changed in version 0.20: cv default value if None will change from 3-fold to 5-fold in v0.22.
    clf = sklearn.linear_model.LogisticRegressionCV(cv=3)
    clf.fit(X.T, Y[0, :].T)
    
    # Plot the decision boundary for logistic regression
    plot_decision_boundary(lambda x: clf.predict(x), X, Y)
    plt.title("Logistic Regression")
    
    # Print accuracy
    LR_predictions = clf.predict(X.T)
    print ('\nAccuracy of logistic regression: %d ' % float((np.dot(Y,LR_predictions) + np.dot(1-Y,1-LR_predictions))/float(Y.size)*100) +
           '% ' + "(percentage of correctly labelled datapoints)")
    