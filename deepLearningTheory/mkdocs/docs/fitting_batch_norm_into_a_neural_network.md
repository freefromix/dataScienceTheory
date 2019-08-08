

# Fitting Batch Norm into a neural network

Here is the new process now:

|                                             |   |
|---------------------------------------------|---|
| <img src="../img/batch_norm_into_a_neural_network.png" width="650" /> |

Parameters are now $W^{[l]},b^{[l]},\beta^{[l]},\gamma^{[l]}$ for each layer.
 
During the process you will have to:

|   |                                                  |
|---|--------------------------------------------------|
| 1 | Calculate $d\beta^{[l]}$ and then update $\beta$ |
| 2 | Update $\beta^{[l]}$ with: $\beta^{[l]}=\beta^{[l]}-\alpha d\beta^{[l]}$ |

|                  |   |                                                                                                                                                                                                            |
|------------------|---|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <img src="../img/warning.png" width="70" /> | If you are using a Deep Learning Programming Framework, usually you won't have to implement the Batch Norm step on Batch Norm layer yourself. So the probing frameworks, that can be sub one line of code. |

## Working with mini-batches

You compute the same thing as bove for each mini-batch: 

|                           |                                             |   |
|---------------------------|---------------------------------------------|---|
| $X^{\{1\}}$: mini batch 1 | <img src="../img/batch_norm_into_a_neural_network.png" width="650" /> |
| $X^{\{2\}}$: mini batch 2 | <img src="../img/batch_norm_into_a_neural_network.png" width="650" /> |
| $\vdots$ ||
| $X^{\{n\}}$: mini batch n | <img src="../img/batch_norm_into_a_neural_network.png" width="650" /> |

## Batch norm eliminates $b^{[l]}$

Normally the parameters in batch norm are $W^{[l]},b^{[l]},\beta^{[l]},\gamma^{[l]}$

Remember that:
$Z^{[l]}=W^{[l]}a^{[l-1]}+b^{[l]}$

But because the first steps in batch norm is to (see [Normalizing activations in a network](./normalizing_activations_in_a_network.md) for more info):

|   |                                |
|---|--------------------------------|
| 1 | Compute the means of $Z^{[l]}$ | 
| 2 | Subtract the means from your training sets | 


Then whatever the value of $b^{[l]}$, it is actually going to just get subtracted out, because during that Batch Normalization step:
- you are going to compute the means of the ZL's 
- subtract the mean. 

**And so adding any constant like $b^{[l]}$ to all of the examples in the mini-batch, it doesn't change anything.Indeed it will get cancelled out by the mean subtractions step.**

So if you are using batch norm you can:

|                                                 |
|-------------------------------------------------|
| Eliminate $b^{[l]}$: $Z^{[l]}=W^{[l]}a^{[l-1]}$ |
| Make $b^{[l]}$ permanently 0|

## Recap for batch norm

|                            |
|----------------------------|
| $Z^{[l]}=W^{[l]}a^{[l-1]}$ |
| $Znorm^{[l]}$ |
| $Ztilde^{[l]}=\gamma^{[l]}Znorm^{[l]}+\beta^{[l]}$ |


## Implementing batch norm

----

For t=1 ... num Mini-batches
{

Compute forward prop on $X^{\{t\}}$

In each hidden layer, use  Batch Norm to replace $Z^{[l]}$ with $Ztilde^{[l]}$

Use back prop to compute $dW^{[l]}, d\beta^{[l]}, d\gamma^{[l]}$

Update parameters: 
$W^{[l]}=W^{[l]}-\alpha dW^{[l]}\\
\beta^{[l]}=\beta^{[l]}-\alpha d\beta^{[l]}\\
\gamma^{[l]}=\gamma^{[l]}-\alpha d\gamma^{[l]}$

}

----


**It works with gradient descent, momentum, RMSprop or Adam.
**