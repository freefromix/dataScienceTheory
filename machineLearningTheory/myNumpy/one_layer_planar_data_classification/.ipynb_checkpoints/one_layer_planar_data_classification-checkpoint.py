#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 23:41:21 2019

@author: julien
"""

# Package imports
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.abspath('..'))
import imageNp as imgNp
import testCases_v2 as testCases
import planar_utils as planarUtils

def layer_sizes(X, Y):
    """
    Arguments:
        X: input dataset of shape (input size, number of examples)
        Y: labels of shape (output size, number of examples)

    Returns:
        n_x: the size of the input layer
        n_h: the size of the hidden layer
        n_y: the size of the output layer
    """

    n_x = X.shape[0] # size of input layer
    n_y = Y.shape[0] # size of output layer

    return (n_x, n_y)

def initialize_parameters(n_x, n_h, n_y):
    """
    Args:
        n_x: size of the input layer
        n_h: size of the hidden layer
        n_y: size of the output layer

    Returns:
        params: python dictionary containing your parameters:
                    W1: weight matrix of shape (n_h, n_x)
                    b1: bias vector of shape (n_h, 1)
                    W2: weight matrix of shape (n_y, n_h)
                    b2: bias vector of shape (n_y, 1)
    """

    print("\nWe initialize all the W and b for this new layer")
    print("Size of input Layer is:", n_x)
    print("Size of hidden layer is:", n_h)
    print("Size of output layer is:", n_y)
    print("W1 with an array of shape: ("+ str(n_h)+", "+str(n_x)+")")
    print("b1 with an array of shape: ("+ str(n_h)+", 1)")
    print("W2 with an array of shape: ("+ str(n_y)+", "+str(n_h)+")")
    print("b2 with an array of shape: ("+ str(n_y)+", 1)")

    # np.random.seed(2)
    W1 = np.random.randn(n_h, n_x)*0.01
    b1 = np.zeros((n_h, 1))
    W2 = np.random.randn(n_y, n_h)*0.01
    b2 = np.zeros((n_y, 1))

    assert W1.shape == (n_h, n_x)
    assert b1.shape == (n_h, 1)
    assert W2.shape == (n_y, n_h)
    assert b2.shape == (n_y, 1)

    parameters = {"W1": W1,
                  "b1": b1,
                  "W2": W2,
                  "b2": b2}

    return parameters



def nn_model(X, Y, n_h, num_iterations=10000, print_cost=False):
    """
    Args:
        X: dataset of shape (2, number of examples)
        Y: labels of shape (1, number of examples)
        n_h: size of the hidden layer
        num_iterations: Number of iterations in gradient descent loop
        print_cost: if True, print the cost every 1000 iterations

    Returns:
        parameters: parameters learnt by the model. They can then be used to predict.
    """

    np.random.seed(3)
    n_x, n_y = layer_sizes(X, Y)

    # Initialize parameters, then retrieve W1, b1, W2, b2.
    # Inputs: "n_x, n_h, n_y". Outputs = "W1, b1, W2, b2, parameters".
    parameters = initialize_parameters(n_x, n_h, n_y)

    # Loop (gradient descent)
    for i in range(0, num_iterations):
        # Forward propagation. Inputs: "X, parameters". Outputs: "A2, cache".
        A2, cache = forward_propagation(X, parameters)

        # Cost function. Inputs: "A2, Y, parameters". Outputs: "cost".
        cost = compute_cost(A2, Y, parameters)

        # Backpropagation. Inputs: "parameters, cache, X, Y". Outputs: "grads".
        grads = backward_propagation(parameters, cache, X, Y)

        # Gradient descent parameter update. Inputs: "parameters, grads". Outputs: "parameters".
        parameters = update_parameters(parameters, grads)

        # Print the cost every 1000 iterations
        if print_cost and i%1000 == 0:
            print("Cost after iteration %i: %f" % (i, cost))

    return parameters

def forward_propagation(X, parameters):
    """
    Args:
        X: input data of size (n_x, m)
        parameters: python dictionary containing your parameters (output of initialization function)

    Returns:
        A2: The sigmoid output of the second activation
        cache: a dictionary containing "Z1", "A1", "Z2" and "A2"
    """
    # Retrieve each parameter from the dictionary "parameters"
    W1 = parameters["W1"]
    b1 = parameters["b1"]
    W2 = parameters["W2"]
    b2 = parameters["b2"]

    # Implement Forward Propagation to calculate A2 (probabilities)
    Z1 = np.dot(W1, X)+b1
    A1 = np.tanh(Z1)
    Z2 = np.dot(W2, A1)+b2
    A2 = sigmoid(Z2)
    print("\n--------Forward propagation--------")
    print("Z1 = np.dot(W1, X)+b1\tZ1:" + str(Z1.shape) + "=" + str(W1.shape) + "dot" + str(X.shape) + "+" + str(b1.shape))
    print("A1 = np.tanh(Z1)\tA1:", A1.shape)
    print("Z2 = np.dot(W2, X)+A1\tZ2:", Z2.shape)
    print("A2 = sigmoid(Z2)\tZ2:", A2.shape)


    assert A2.shape == (1, X.shape[1])

    cache = {"Z1": Z1,
             "A1": A1,
             "Z2": Z2,
             "A2": A2}

    return A2, cache

def sigmoid(x):
    """
    Compute the sigmoid of x

    Args:
        x: A scalar or numpy array of any size.

    Returns:
        s: sigmoid(x)
    """
    s = 1/(1+np.exp(-x))
    return s



def backward_propagation(parameters, cache, X, Y):
    """
    Implement the backward propagation using the instructions above.

    Args:
        parameters: python dictionary containing our parameters
        cache: a dictionary containing "Z1", "A1", "Z2" and "A2".
        X: input data of shape (2, number of examples)
        Y: "true" labels vector of shape (1, number of examples)

    Returns:
        grads: python dictionary containing your gradients with respect to different parameters
    """
    m = X.shape[1]

    # First, retrieve W1 and W2 from the dictionary "parameters".
    # W1 = parameters["W1"]
    W2 = parameters["W2"]

    # Retrieve also A1 and A2 from dictionary "cache".
    A1 = cache["A1"]
    A2 = cache["A2"]

    # Backward propagation: calculate dW1, db1, dW2, db2.
    ### START CODE HERE ### (≈ 6 lines of code, corresponding to 6 equations on slide above)
    dZ2 = A2-Y
    dW2 = np.dot(dZ2, A1.T)/m
    db2 = np.sum(dZ2, axis=1, keepdims=True)/m
    dZ1 = np.dot(W2.T, dZ2)*(1 - np.power(A1, 2))
    dW1 = np.dot(dZ1, X.T)/m
    db1 = np.sum(dZ1, axis=1, keepdims=True)/m

    grads = {"dW1": dW1,
             "db1": db1,
             "dW2": dW2,
             "db2": db2}

    return grads

def compute_cost(A2, Y, parameters):
    """
    Computes the cross-entropy cost given in equation (13)

    Args:
        A2: The sigmoid output of the second activation, of shape (1, number of examples)
        Y: "true" labels vector of shape (1, number of examples)
        parameters: python dictionary containing your parameters W1, b1, W2 and b2

    Returns:
        cost: cross-entropy cost given equation (13)
    """

    m = Y.shape[1] # number of example

    # Compute the cross-entropy cost
    logprobs = np.multiply(np.log(A2), Y) + np.multiply((1 - Y), np.log(1 - A2))
    cost = -np.sum(logprobs)/m

    cost = np.squeeze(cost)

    # makes sure cost is the dimension we expect.
    # E.g., turns [[17]] into 17
    assert isinstance(cost, float)

    return cost

def update_parameters(parameters, grads, learning_rate=1.2):
    """
    Updates parameters using the gradient descent update rule

    Args:
        parameters: python dictionary containing your parameters
        grads: python dictionary containing your gradients

    Returns:
        parameters: python dictionary containing your updated parameters
    """
    # Retrieve each parameter from the dictionary "parameters"
    W1 = parameters["W1"]
    b1 = parameters["b1"]
    W2 = parameters["W2"]
    b2 = parameters["b2"]

    # Retrieve each gradient from the dictionary "grads"
    dW1 = grads["dW1"]
    db1 = grads["db1"]
    dW2 = grads["dW2"]
    db2 = grads["db2"]

    # Update rule for each parameter
    W1 = W1-(learning_rate*dW1)
    b1 = b1-(learning_rate*db1)
    W2 = W2-(learning_rate*dW2)
    b2 = b2-(learning_rate*db2)

    parameters = {"W1": W1,
                  "b1": b1,
                  "W2": W2,
                  "b2": b2}

    return parameters


def predict(parameters, X):
    """
    Using the learned parameters, predicts a class for each example in X

    Args:
        parameters: python dictionary containing your parameters
        X: input data of size (n_x, m)

    Returns
        predictions: vector of predictions of our model (red: 0 / blue: 1)
    """

    # Computes probabilities using forward propagation,
    # and classifies to 0/1 using 0.5 as the threshold.
    A2, _ = forward_propagation(X, parameters)
    predictions = np.round(A2)

    return predictions

if __name__ == '__main__':
    """
        We have 2 input features: x1, x2 and 400 samples
        So X.shape=(2, 400) and Y.shape=(1,400)
    Args:

    Returns:
        params: python dictionary containing your parameters:
                    W1: weight matrix of shape (n_h, n_x)
                    b1: bias vector of shape (n_h, 1)
                    W2: weight matrix of shape (n_y, n_h)
                    b2: bias vector of shape (n_y, 1)
    """


    np.random.seed(1) # set a seed so that the results are consistent
    imageNp = imgNp.getImageNpArray('classification_kiank.png')
    print(imageNp.shape)
    imgNp.drawImageWithNpArray(imageNp)

    imageNp = imgNp.getImageNpArray('grad_summary.png')
    imgNp.drawImageWithNpArray(imageNp)

    imageNp = imgNp.getImageNpArray('sgd.gif')
    imgNp.drawImageWithNpArray(imageNp)

    imageNp = imgNp.getImageNpArray('sgd_bad.gif')
    imgNp.drawImageWithNpArray(imageNp)

    X, Y = planarUtils.load_planar_dataset()
    n_x, n_h, n_y = testCases.initialize_parameters_test_case()

    try:
        n_h=int(input('Give me the hidden_layer_size:'))
    except ValueError:
        print("This is not a number.")


    print("\n------------Start------------")
    print("We have", len(X), "input features and", len(X[0]), "data samples")
    print("So X.shape=", X.shape, "and Y.shape=", Y.shape)

    # plt.figure(figsize=(16, 32))
    # hidden_layer_sizes = [1, 2, 3, 4, 5, 20, 50]
    # for i, n_h in enumerate(hidden_layer_sizes):

        # subplot(nrows, ncols, index, **kwargs)    
        # plt.subplot(5, 2, i+1)
        # plt.title('Hidden Layer of size %d' % n_h)
        # num_iterations=5000
    parameters = nn_model(X, Y, n_h, num_iterations=10)
    # planarUtils.plot_decision_boundary(lambda x: predict(parameters, x.T), X, Y)
    predictions = predict(parameters, X)
    accuracy = float((np.dot(Y, predictions.T) + np.dot(1-Y, 1-predictions.T))/float(Y.size)*100)
    print ("Accuracy for {} hidden units: {} %".format(n_h, accuracy))

