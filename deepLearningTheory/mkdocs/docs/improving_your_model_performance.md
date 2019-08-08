# Improving your model performance

The 2 fundamentals assumptions of supervised learning:

- You can fit the training set pretty well (achieve low avoidable bias).
- The training set performance generalizes pretty well to the dev/test set (achieve low Variance).


![](img/avoidable_bias_variance.png)

----

**Improve Avoidable bias:**

- Train Bigger model
- Train longer/Use a better optimization algorithm (momentum, RMSprop, Adam...) 
- NN architecture/hyperparameters search
  - Changing the activation function
  - Changing the number of layers or hidden units
  - Changing the model size
  - Try other model architectures such as RNN (Recurent Neural Networks) or CNN (Convolutional Neural Networks).


----

**Improve Variance:**

- More data
- Regularization (L2, dropout,data augmentation)
- NN architecture/hyperparameters search
  - Changing the activation function
  - Changing the number of layers or hidden units
  - Changing the model size
  - Try other model architectures such as RNN (Recurent Neural Networks) or CNN (Convolutional Neural Networks).
 
