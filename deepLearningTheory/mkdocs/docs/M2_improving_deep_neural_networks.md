# Improving Deep Neural Networks: Hyperparameter tuning, Regularization and Optimization

## Practical aspects of Deep Learning
  - [Setting up your Machine Learning Application](./setting_up_your_machine_learning_application.md)
  - [Regularizing your neural network](./regularizing_your_neural_network.md)
  - [Setting up your optimization problem](./setting_up_your_optimization_problem.md) (normalizing input, weight initialization, gradient checking)

## Optimization algorithms (speed-up gradient descent)
  - [Understanding mini-batch gradient descent](./understanding_mini-batch_gradient_descent.md)
  - [Exponentially weighted average](./exponentially_weighted_average.md)
  - [Gradient descent with momentum](./gradient_descent_with_momentum.md)
  - [RMSprop root mean square prop](./rmsprop_root_mean_square_prop.md)
  - [Adam optimization algorithm](./adam_optimization_algorithm.md) (many people have tried it and seen it work well on many problems)
  - [Learning rate decay](./learning_rate_decay.md) (Andrew NG: It is a bit lower down in the list of the things he would try)
  - [The problem of local optima](./the_problem_of_local_optima.md)

## Hyperparameter tuning, Batch Normalization and Programming Frameworks
  - Hyperparameter tuning
    - [Tunning process](./tunning_process.md)
    - [Using an appropriate scale to pick hyperparameters](./using_an_appropriate_scale_to_pick_hyperparameters.md)
    - [Hyperparameters tuning in practice Pandas vs Caviar](./hyperparameters_tuning_in_practice_pandas_vs_caviar.md)
  - Batch normalization
    - [Normalizing activations in a network](./normalizing_activations_in_a_network.md)
    - [Fitting Batch Norm into a neural network](./fitting_batch_norm_into_a_neural_network.md)
    - [Why does Batch Norm work](./why_does_batch_norm_work.md)
    - [Batch Norm at test time](./batch_norm_at_test_time.md)
  - Multi-class classification
    - [Softmax regression](./softmax_regression.md)
  - Introduction to programming frameworks
    - [Deep learning frameworks](./deep_learning_frameworks.md)
    - Tensorflow

## Python

<img src="../img/dotproduct_matrices.jpg" width="400" />

| Code                             | Function                                                                                   |
|----------------------------------|--------------------------------------------------------------------------------------------|
| $x = np.array([[1.,2.],[3.,4.]])$  | Creates an ndarray.                                                                        |
| c=np.dot(a,b)                    | Dot product of two arrays.                                                                 |
| u=np.exp(v)                      | Calculate the exponential of all elements in the input array                               |
| u=np.log(v)                      | Natural logarithm, element-wise.                                                           |
| a=np.random.rand(100)            | Random samples from a uniform distribution over [0, 1)                                     |
| ndarray.shape                    | Tuple of array dimensions. ex:(100,4)                                                      |
| np.maximum(a,b)                  | Element-wise maximum of array elements.                                                    |
| $a**2$                           | Element-wise square of all elements.                                                       |
| 1/a                              | Element-wise square of all elements                                                        |
| np.sum(a)                        | Sum of array elements over a given axis.                                                   |
| a.sum(axis = 0)                  | Sum the values in a matrix A vertically                                                    |
| a.T                              | Transpose array. Same as self.transpose()  except that self is returned if self.ndim < 2.  |

