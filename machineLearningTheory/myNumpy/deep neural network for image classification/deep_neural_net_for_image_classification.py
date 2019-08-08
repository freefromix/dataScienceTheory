#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:10:00 2019

@author: julien
"""


import numpy as np
# import h5py
import matplotlib.pyplot as plt
import scipy
# from PIL import Image
from scipy import ndimage
from dnn_app_utils_v3 import load_data, initialize_parameters_deep, L_model_forward, compute_cost, L_model_backward, update_parameters, predict
 

plt.rcParams['figure.figsize'] = (5.0, 4.0) # set default size of plots
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'

np.random.seed(1)

def L_layer_model(X, Y, layers_dims, learning_rate, num_iterations, print_cost=False):#lr was 0.009
    """
    Implements a L-layer neural network: [LINEAR->RELU]*(L-1)->LINEAR->SIGMOID.
    
    Arguments:
    X -- data, numpy array of shape (number of examples, num_px * num_px * 3)
    Y -- true "label" vector (containing 0 if cat, 1 if non-cat), of shape (1, number of examples)
    layers_dims -- list containing the input size and each layer size, of length (number of layers + 1).
    learning_rate -- learning rate of the gradient descent update rule
    num_iterations -- number of iterations of the optimization loop
    print_cost -- if True, it prints the cost every 100 steps
    
    Returns:
    parameters -- parameters learnt by the model. They can then be used to predict.
    """

    np.random.seed(1)
    costs = []                         # keep track of cost
    
    # Parameters initialization. (≈ 1 line of code)
    ### START CODE HERE ###
    parameters = initialize_parameters_deep(layers_dims)
    ### END CODE HERE ###
    
    # Loop (gradient descent)
    for i in range(0, num_iterations):

        # Forward propagation: [LINEAR -> RELU]*(L-1) -> LINEAR -> SIGMOID.
        print("\n\n########### Forward propagation ###########")
        AL, caches = L_model_forward(X, parameters)
        
        # Compute cost.
        print("\n\n########### Compute cost ###########")
        cost = compute_cost(AL,Y)
        ### END CODE HERE ###
    
        # Backward propagation.
        print("\n\n########### Backward propagation ###########")
        grads = L_model_backward(AL, Y, caches)
 
        # Update parameters.
        print("\n\n########### Update parameters ###########")
        parameters = update_parameters(parameters, grads, learning_rate)
                
        # Print the cost every 100 training example
        if print_cost and i % 100 == 0:
            print ("Cost after iteration %i: %f" %(i, cost))
        if print_cost and i % 100 == 0:
            costs.append(cost)
            
    # plot the cost
    plt.plot(np.squeeze(costs))
    plt.ylabel('cost')
    plt.xlabel('iterations (per tens)')
    plt.title("Learning rate =" + str(learning_rate))
    plt.show()
    
    return parameters


def predictWithMyOwnImage():
    ## START CODE HERE ##
    my_image = "my_image.jpg" # change this to the name of your image file 
    my_label_y = [1] # the true class of your image (1 -> cat, 0 -> non-cat)
    ## END CODE HERE ##

    fname = "images/" + my_image
    image = np.array(ndimage.imread(fname, flatten=False))
    my_image = scipy.misc.imresize(image, size=(num_px,num_px)).reshape((num_px*num_px*3,1))
    my_image = my_image/255.
    my_predicted_image = predict(my_image, my_label_y, parameters)

    plt.imshow(image)
    print ("y = " + str(np.squeeze(my_predicted_image)) + ", your L-layer model predicts a \"" + classes[int(np.squeeze(my_predicted_image)),].decode("utf-8") +  "\" picture.")

if __name__ == '__main__':

    try:
        n_h = int(input('Give me the number of hiddent units for the layers:'))
        print('')
        num_iterations = int(input('Give me the number of iterations (must be > 100 to see the output, original value was 2500):'))
    except ValueError:
        print("This is not a number.")
        quit()
    
    train_x_orig, train_y, test_x_orig, test_y, classes = load_data()
    # Example of a picture
    # index = 10
    # plt.imshow(train_x_orig[index])
    # print ("y = " + str(train_y[0,index]) + ". It's a " + classes[train_y[0,index]].decode("utf-8") +  " picture.")
    
    m_train = train_x_orig.shape[0]
    num_px = train_x_orig.shape[1]
    m_test = test_x_orig.shape[0]

    print ("Each image is of size: (" + str(num_px) + ", " + str(num_px) + ", 3)")

    print ("\nNumber of training examples: " + str(m_train))
    print ("train_x_orig shape: " + str(train_x_orig.shape))
    print ("train_y shape: " + str(train_y.shape))
    print ("\nNumber of testing examples: " + str(m_test))
    print ("test_x_orig shape: " + str(test_x_orig.shape))
    print ("test_y shape: " + str(test_y.shape))
    
    # Reshape the training and test examples
    train_x_flatten = train_x_orig.reshape(train_x_orig.shape[0], -1).T   # The "-1" makes reshape flatten the remaining dimensions
    test_x_flatten = test_x_orig.reshape(test_x_orig.shape[0], -1).T

    # Standardize data to have feature values between 0 and 1.
    train_x = train_x_flatten/255.
    test_x = test_x_flatten/255.

    print ("After flatten train_x's shape: " + str(train_x.shape))
    print ("After flatten test_x's shape: " + str(test_x.shape))

    n_x = train_x.shape[0]     # num_px * num_px * 3
    n_y = train_y.shape[0]
    layers_dims = (n_x, n_h, n_y)
    print ("layers_dims: ", layers_dims)

    learning_rate = 0.0075
    
    parameters = L_layer_model(train_x, train_y, layers_dims, learning_rate, num_iterations, print_cost = True)
    pred_test = predict(test_x, test_y, parameters)

    print("Remember that the number of iterations should have been > 100 to see the results")