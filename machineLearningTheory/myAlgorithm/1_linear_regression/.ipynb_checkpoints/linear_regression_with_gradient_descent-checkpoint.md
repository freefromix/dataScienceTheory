# Linear regression with gradient descent

## Hypothesis with multiple features (multivariate)

![](img/multivariate_features.png)

We have:
- n: number of features
- m: number of trainning examples
- $X_{j}$: The feature X selected
- $x^{(i)}$: input feature of the $i^{th}$ trainning example.
- $x_{j}^{(i)}$: value of feature $j$ of the $i^{th}$ trainning example
- $x_{n}^{(m)}$: last feature of the last training example

### Hypothesis

$h_{\theta}(x) = \theta^{T}x  = \theta_{0}x_{0} + \theta_{1}x_{1}+\theta_{2}x_{2}+\cdots \theta_{n}x_{n}$

$J(\theta)= J(\theta_{0},\theta_{1},\cdots,\theta_{n})=\frac{1}{2m}\sum_{i=1}^{m}(h_{\theta}(x^{(i)})-y^{(i)})^2$

We need to minimize the cost function.

Now we're faced with a classical optimization problem: we have some parameters $\theta$ we can tweak, and some cost function $J(\theta)$ we want to minimize.

The topic of mathematical optimization is vast, but what ends up working very well for machine learning is a fairly simple algorithm called gradient descent.

### Gradient descent

Gradient descent:

----

Repeat until optimized {

    for all j {

$$\theta_{j}:=\theta_{j}-\alpha \frac{\partial}{\partial \theta_{j}}J(\theta)$$

    }
}

----

More explicitly:

Repeat until optimized {

$\theta_{0}:=\theta_{0}-\alpha \frac{1}{m}\sum_{i=1}^{m}(h_{\theta}(x^{(i)})-y^{(i)})$

$\theta_{1}:=\theta_{0}-\alpha \frac{1}{m}\sum_{i=1}^{m}(h_{\theta}(x^{(i)})-y^{(i)})x_{1}^{(i)}$

$\vdots$

$\theta_{n}:=\theta_{n}-\alpha \frac{1}{m}\sum_{i=1}^{m}(h_{\theta}(x^{(i)})-y^{(i)})x_{n}^{(i)}$

}

----

Summarized:

```bash
Repeat until optimized {

 for j=0 to m {
```

$$\theta_{j}:=\theta_{j}-\alpha \frac{1}{m}\sum_{i=1}^{m}(h_{\theta}(x^{(i)})-y^{(i)})x_{j}^{(i)}$$

```bash
 }
}
```

