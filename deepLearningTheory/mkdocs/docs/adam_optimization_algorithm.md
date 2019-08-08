# Adam optimization algorithm

!!! Many people have tried it and seen it work well on many problems !!!

Adam optimization algorithm is basically taking **momentum** and   **RMSprop** and putting them together. 

Adam is for: Adaptive moment estimation. But everyone just calls it the Adam authorization algorithm.

$V_{dW}=0$, $S_{dW}=0$

On iteration t:

**{**

dW,db = Compute dW,db using current mini-batch

__Momentum__

|                                          |                                          |
| ---------------------------------------- | ---------------------------------------- |
| $V_{dW}=\beta_{1}V_{dW}+(1-\beta_{1})dW$ | $V_{db}=\beta_{1}V_{db}+(1-\beta_{1})db$ |

__RMSprop__

|                                              |                                              |
| -------------------------------------------- | -------------------------------------------- |
| $S_{dW}=\beta_{2}V_{dW}+(1-\beta_{2})dW^{2}$ | $S_{db}=\beta_{2}V_{db}+(1-\beta_{2})db^{2}$ |

__Correction__

|                                                  |                                                  |
| ------------------------------------------------ | ------------------------------------------------ |
| $Vcorrected_{dW}=\frac{V_{dW}}{(1-\beta_{1}^t)}$ | $Vcorrected_{db}=\frac{V_{db}}{(1-\beta_{1}^t)}$ |
| $Scorrected_{dW}=\frac{S_{dW}}{(1-\beta_{2}^t)}$ | $Scorrected_{db}=\frac{S_{db}}{(1-\beta_{2}^t)}$ |

__Update values__

|                                                                     |                                                                     |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| $W=W-\alpha\frac{Vcorrected_{dW}}{\sqrt{Scorrected_{dW}}+\epsilon}$ | $b=b-\alpha\frac{Vcorrected_{db}}{\sqrt{Scorrected_{db}}+\epsilon}$ |

**}**

## Hyperparameters choice

| Hyperparameter | Value     | Explanation                                                                                                           |
| -------------- | --------- | --------------------------------------------------------------------------------------------------------------------- |
| $\alpha$       |           | Needs to be tune                                                                                                      |
| $\beta_{1}$    | 0.9       | dW                                                                                                                    |
| $\beta_{2}$    | 0.999     | $(dW^{2})$                                                                                                            |
| $\epsilon$     | $10^{-8}$ | Indeed $\epsilon$ is only here to avoid a divide by zero in $\frac{Vcorrected_{db}}{\sqrt{Scorrected_{db}+\epsilon}}$ |

