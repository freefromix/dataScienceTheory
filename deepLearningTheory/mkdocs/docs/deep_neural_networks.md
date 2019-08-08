# Deep Neural Networks

## Deep L-Layer neural network

<img src="../img/deep-l_layer.png" width="600" />

| Notation   | Meaning                       | Example above                                                      |
|------------|-------------------------------|--------------------------------------------------------------------|
|  L         | Number of layers              | L=4                                                                |
| $n^{[l]}$  | Number of units in layer $l$  | $n^{[0]}=n_{x}=3,n^{[1]}=5,n^{[2]}=5,n^{[3]}=3,n^{[4]}=n^{[l]}=1$  |
| $a^{[l]}$  | Activations in layer $l$      | $a^{[l]}=g^{[l]}(z^{[l]})$                                         |
| $W^{[l]}$  | Weights in layer $l$          |                                                                    |

## Forward Propagation in a Deep Network

<img src="../img/forward_propagation_in_deep_network.png" width="500" />

### Forward propagation general rule for m inputs:

|                                    |
|------------------------------------|
| $Z^{[l]}=W^{[l]}A^{[l-1]}+b^{[l]}$ |
| $A^{[l]}=g^{[l]}(Z^{[l]})$ |



## Getting your matrix dimensions right

### Not vectorized



<img src="../img/parameters_wl_and_zl.png" width="600" />


$W^{[l]}:(n^{[l]}, n^{[l-1]})$

$b^{[l]}:(n^{[l]}, 1)$


$dW^{[l]}:(n^{[l]}, n^{[l-1]})$

$db^{[l]}:(n^{[l]}, 1)$

$W^{[l]}:(n^{[l]}, n^{[l-1]})$

$Z^{[l]}:g^{[l]}(a^{[l]})$

### Vectorized

<img src="../img/vectorized.png" width="600" />

m is the number of training examples

$X:(n^{[0]}, m)$

$W^{[l]}:(n^{[l]}, n^{[l-1]})$

$b^{[l]}:(n^{[l]}, 1)$ but with broadcasting it will be $(n^{[l]}, m)$ during calculus.


$Z^{[l]},A^{[l]}: (n^{[l]}, m)$ with the exception when l=0

$A^{[0]}: (n^{[0]}, m)$

$dZ^{[l]},dA^{[l]}: (n^{[l]}, m)$ with the exception when l=0

## Why deep representations?

<img src="../img/intuition_about_deep_representation.png" width="400" />

THE DEEPER THE NN THE MORE COMPLEX THINGS ARE DONE.
For example: First layer find image edges and last layer recognize face

<img src="../img/circut_theory_and_deep_learning.png" width="400" />

In a shallow NN the first layer would be hudge.
## Building blocks of deep neural networks

<img src="../img/forward_and_backward_functions.png" width="400" />

<img src="../img/forward_and_backward_functions2.png" width="400" />

## Forward and backward functions

### Forward propagation layer l

<img src="../img/forward_propagation_layer_l.png" width="400" />

Non vectorized version:
<img src="../img/non_vectorized_version.png" width="400" />


Vectorized version:

$dZ^{[l]}=dA^{[l]}*g'^{[l]}(Z^{[l]})$

$dW^{[l]}=\frac{1}{m}dZ^{[l]}.A^{[l-1]T}$

$db^{[l]}=\frac{1}{m}np.sum(dZ^{[l]},axis=1,keepdims=True)$

$dA^{[l-1]}=W^{[l]T}.dZ^{[l]}$

#### Summary

<img src="../img/summary_forward_backward.png" width="400" />


$da^{[l]}=-\frac{y}{a}+\frac{1-y}{1-a}$


Vectorized version:

$dA^{[l]}=(-\frac{y{[1]}}{a{[1]}}+\frac{1-y{[1]}}{1-a{[1]}}\cdots-\frac{y{[m]}}{a{[m]}}+\frac{1-y{[m]}}{1-a{[m]}})$


----


![](img/forward_propagation_layer_l_formulas.png)


----


## Parameters vs Hyperparameters

Parameters: 

$W^{[1]}, b^{[1]}, W^{[2]}, b^{[1]}, W^{[3]}, b^{[3]}\cdots$


Hyperparameters:

* Learning rate $\alpha{}$
* Number of Iterations
* Number of hidden layers L
* Number of hidden units $n^{[1]}, n^{[2]}, \cdots$
* Choice of activation function
* Momentum
* Minibatch size
* Various forms of regularization parameters


<img src="../img/empirical_process.png" width="400" />

You have to try values to find the best hyperparameters values.

## Quizz


<img src="../img/deep_neural_networks_1.png" width="400" />
<img src="../img/deep_neural_networks_2-1.png" width="400" />
<img src="../img/deep_neural_networks_2-2.png" width="400" />
<img src="../img/deep_neural_networks_3.png" width="400" />
<img src="../img/deep_neural_networks_4.png" width="400" />
<img src="../img/deep_neural_networks_5.png" width="400" />
<img src="../img/deep_neural_networks_6.png" width="400" />
<img src="../img/deep_neural_networks_7.png" width="400" />
<img src="../img/deep_neural_networks_8.png" width="400" />
<img src="../img/deep_neural_networks_9-1.png" width="400" />
<img src="../img/deep_neural_networks_9-2.png" width="400" />
<img src="../img/deep_neural_networks_9-3.png" width="400" />
<img src="../img/deep_neural_networks_9-4.png" width="400" />
<img src="../img/deep_neural_networks_10.png" width="400" />

