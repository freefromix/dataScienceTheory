# Neural Style Transfer cost function FINAL definition

## Remember the Neural Style Transfer cost function SIMPLE definition

In [Neural Style Transfer cost function SIMPLE definition](./neural_style_transfer_cost_function_simple_definition.md)

We defined the overall Neural Style Transfer cost function as:

|                                                     |
|-----------------------------------------------------|
| $J(G)=\alpha J_{Content}(C,G)+\beta J_{Style}(S,G)$ |

With this equation you can use gradient descent or a more sophisticated optimization algorithm if you want in order to try to find an image G that tries to minimize this cost function.

## Remember the Content cost function

In [Content cost function](./content_cost_function.md) we defined

|                                                                                |
|--------------------------------------------------------------------------------|
| $J_{Content}(C,G)=\frac{1}{2}\left\lVert a^{[l](C)}-a^{[l](G)} \right\rVert^2$ |

With $\frac{1}{2}$ not really important.

## Remember Neural Style Transfer cost function FINAL definition

In [Style Cost Function](./style_cost_function.md) we defined:

| Overall STYLE cost function |
|-----------------------------|
| $J_{style}^{[l]}(S,G)=\sum_l \lambda^{[l]} J_{style}^{[l]}(S,G)$ |

- As sum over all the different layers of the style cost function for that layer. 
- Weighted by some set of parameters, by some set of additional hyperparameters, which we'll denote as $\lambda^{[l]}$.

__And:__


|                                                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------|
| $J_{style}^{[l]}(S,G)=\frac{1}{(2n_H^{[l]}n_W^{[l]}n_C^{[l]} )^2}\sum_{k}\sum_{k'} (G_{kk'}^{[l](S)}-G_{kk'}^{[l](G)})$ |



