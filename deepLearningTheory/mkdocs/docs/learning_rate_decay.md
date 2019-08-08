# Learning rate decay

Definition: Is to slowly reduce your learning rate $\alpha$ over time.

## Andrew NG It is a bit lower down in the list of the things he would try


## Why

<img src="../img/screenshot_from_2019-01-04_01-35-27.png" width="400" />

|                               |           |                                                                                                                                             |
|-------------------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Mini-batch without rate decay | Blue line | Then as you iterate, your steps will be a little bit noisy. And it will tend towards this minimum over here, but it won't exactly converge. |
| Mini-batch without rate decay | Green line | You can still have relatively fast learning. But then as alpha gets smaller, your steps you take will be slower and smaller. And so you end up oscillating in a tighter region around this minimum. |

## Implementation

Training set : $X^{\{1\}}, X^{\{2\}}, X^{\{3\}} \cdots X^{\{n\}}$

epoch 1 = 1 pass through the data (The whole training set or all mini-batches).

epoch 2 = $2^{nd}$ pass through the data (The whole training set or all mini-batches).

|                                                          |
|----------------------------------------------------------|
| $\alpha=\frac{1}{1+decayRate\times{epochNum}}\alpha_{0}$ |

Example with $\alpha_{0}$=0.2 and $decayRate=1$ :

| Epoch number | $\alpha$ |
|--------------|----------|
| 1 | 0.1 |
| 2 | 0.067 |
| 3 | 0.05 |
| 4 | 0.04 |
| ... | ... |

Note that the decay rate here becomes another hyper-parameter, which you might need to tune. 

## Other learning rate decay method

|                                 |                          |
|---------------------------------|--------------------------|
| Exponential learning rate decay | $\alpha=0.95^{epochNum}$ |

Another method:

$\alpha=\frac{k}{\sqrt{epochNum}}\alpha_{0}$

or $\alpha=\frac{k}{\sqrt{t}}\alpha_{0}$

