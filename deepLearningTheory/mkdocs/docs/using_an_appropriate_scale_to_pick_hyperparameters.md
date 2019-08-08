# Using an appropriate scale to pick hyperparameters

## Picking hyperparameters at random

### $\alpha$ between 0.0001 ($10^{-4}$) and 1

You want to pick a random value of $\alpha$ between 0.0001 ($10^{-4}$) and 1.

Use this formula:

|                         |
|-------------------------|
| $r=-4*np.random.rand()$ |
| $\alpha=10^{r}$ |

### $\beta$ between 0.9 and 0.999

You want $\beta$ randomly between 0.9 and 0.999.

So you want $1-\beta$ between 0.1 and 0.001.

|                                   |                    |
|-----------------------------------|--------------------|
| $0.1=10^{-1}$ and $0.001=10^{-3}$ | so $r \in [-3,-1]$ |

|                  |
|------------------|
| $1-\beta=10^{r}$ |
| $r=-3*np.random.rand()$ |
| $\beta=1-10^{r}$ |

----

|                                       |                                                               |
|---------------------------------------|---------------------------------------------------------------|
| If $\beta$ goes from 0.9000 to 0.9005 | It's no big deal, it's averaging between 10 and 10.05 values. |
| If $\beta$ goes from 0.999 to 0.9995 | It's really big deal, it's averaging over roughly 1000 and 2000  values. |
 
Indeed remember the formula is $\frac{1}{1-\beta}$