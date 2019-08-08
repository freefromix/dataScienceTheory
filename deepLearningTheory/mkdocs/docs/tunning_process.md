# Tuning process

## Hyperparameters

| Importance to have tuning results  | Hyperparameter                  | From                         | Infos                                                                                |
|------------------------------------|---------------------------------|------------------------------|--------------------------------------------------------------------------------------|
| 1                                  |  $\alpha$                       | Learning rate                |                                                                                      |
| 2                                  |  $\beta$                        | Momentum term                | $\approx 0.9$                                                                        |
| 2                                  | # hidden units                  | Number of hidden units       |                                                                                      |
| 2                                  | mini-batch size                 |                              |                                                                                      |
| 3                                  | # layers                        | Number of layers             |                                                                                      |
| 3                                  | learning rate decay             |                              |                                                                                      |
| 4                                  | $\beta_{1},\beta_{2},\epsilon$  | Adam optimization algorithm  | Generally Andrew NG don't touch it: $\beta_{1}=0.9,\beta_{2}=0.99,\epsilon=10^{-8}$  |

First: Don't use a grid to try values, try random values
<img src="../img/screenshot_from_2019-01-06_20-03-07.png" width="400" />

Choose maybe of same number of points, right? 25 points and then try out the hyperparameters on this randomly chosen set of points. The reason you do that is that it's **difficult to know in advance which hyperparameters are going to be the most important for your problem**. 

Remember some hyperparameters are more important than others:

Let's say hyperparameter one turns out to be alpha, the learning rate. And to take an extreme example, let's say that hyperparameter two was that value epsilon that you have in the denominator of the Adam algorithm. So your choice of alpha matters a lot and your choice of epsilon hardly matters.

This example, using just two hyperparameters. In practice, you might be searching over many more hyperparameters than these.

<img src="../img/screenshot_from_2019-01-06_22-39-33.png" width="200" />

Another solution:

You found that some point work the best and maybe a few other points around it tend to work really well.

One solution would be to zoom in to a smaller region of the hyperparameters and then sample more density within this space.

<img src="../img/screenshot_from_2019-01-06_22-41-56.png" width="200" />

Or maybe again use random, but then focusing more on searching within this blue square.

