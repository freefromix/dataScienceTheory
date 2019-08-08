# Normalizing activations in a network

## Reminder: Normalizing input X in a network

<img src="../img/screenshot_from_2019-01-08_10-02-58.png" width="150" />

|   |                   |                                  |
|---|-------------------|----------------------------------|
| 1 | Compute the means | $\mu=\frac{1}{m} \sum_{}X^{(i)}$ |
| 2 | Subtract the means from your training sets | $Xnew=X-\mu$ |
| 3 | Calculate the variance | $\sigma^{2} = \frac{1}{m}\sum_{i=1}^{m}(Xnew^{(i)})^{2}$ (element wise squaring) |
| 4 | Normalize the dataset according to the variances | $Xnorm=Xnew/\sigma^{2}$ |

<img src="../img/screenshot_from_2019-01-08_09-43-59.png" width="200" /> 

This can turn the contours of your learning problem from something that might be very elongated to something that is more round, and easier for an algorithm like gradient descent to optimize.

## Normalizing the activation layers

<img src="../img/screenshot_from_2019-01-08_10-01-28.png" width="300" /> Now if you want to train the parameters, say $w^{[3]}$, $b^{[3]}$.

**Can we normalize the mean and variance of $a^{[2]}$ to make the training of $w^{[3]}$, $b^{[3]}$ faster?**

## Implementing batch norm

Given some intermediate values in your neural net: $Z^{[l](1)} \cdots Z^{[l](m)}$

|                  |                                        |
|------------------|----------------------------------------|
| $(i)$            | Denote the $i^{th}$ training example.  |
| $[l]$            | Denote the $l^{th}$ layer.  |

|   |                   |                                   |
|---|-------------------|-----------------------------------|
| 1 | Compute the means | $\mu=\frac{1}{m} \sum_{i}Z^{(i)}$ |
| 2 | Subtract the means from your training sets | $Z^{(i)}new=Z^{(i)}-\mu$ |
| 3 | Calculate the variance | $\sigma^{2} = \frac{1}{m}\sum_{i=1}^{m}(Z^{(i)}-\mu)^{2}=\frac{1}{m}\sum_{i=1}^{m}(Znew^{(i)})^{2}$ (element wise squaring) |
| 4 | Normalize the dataset according to the variances | $Z^{(i)}norm=\frac{Z^{(i)}new}{\sqrt{\sigma^{2}+\epsilon}}$ |
| 5 | If you want to use Ztilde as final value | $Ztilde^{(i)}=\gamma Z^{(i)}norm + \beta$ |

|                    |
|--------------------|
| **Just for info:** |
| $\beta$ in momentum $\neq \beta$ in Adam $\neq \beta$ in RMSprop $\neq \beta$ in Batch Norm |
| Indeed The authors of the Adam paper use $\beta$ on their paper to denote that hyperparameter, the authors of the Batch Norm paper had used Beta to denote this parameter, but these are two completely different Betas. |

**Notice that the effect of $\gamma$ and $\beta$ is that it allows you to set the mean of Ztilde to be whatever you want it to be.**

$\gamma$ and $\beta$ are learnable parameters of the model.


So if we're using **gradient descent** (or some other like gradient descent with **momentum**, or **adam** etc.)  you would update the parameters $\gamma$ and $\beta$, just as you would update the weights of your neural network.

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

