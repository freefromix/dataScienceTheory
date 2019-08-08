# Gradient descent with momentum

Here an example of gradient descent **without** momentum: <img src="../img/gradien_descent_without_momentum.png" width="300" />
<img src="../img/slower_learning_faster_learning.png" width="150" />


Here an example of gradient descent **without** momentum if we apply a much larger learning rate (you might end up over shooting and end up diverging a lot): <img src="../img/gradien_descent_without_momentum_and_much_larger_learning_rate.png" width="300" /><img src="../img/slower_learning_faster_learning.png" width="150" />

Here an example of gradient descent **with** momentum. Note that the learning rate is faster (red line): <img src="../img/gradien_descent_with_momentum.png" width="300" /><img src="../img/slower_learning_faster_learning.png" width="150" />

In the equations:

|                                   |
|-----------------------------------|
| $V_{dW}=\beta V_{dW}+(1-\beta)dW$ |
| $V_{db}=\beta V_{db}+(1-\beta)db$ |

You can consider that:

<img src="../img/screenshot_from_2019-01-02_20-05-20.png" width="400" />


* Friction
* Velocity
* Acceleration



## Algorithm

<img src="../img/implementation_gradient_descent_with_momentum.png" width="400" />

----

On iteration t:

{

dW, db = Compute dW and db on current mini-batch.

$V_{dW}=\beta V_{dW}+(1-\beta)dW$

$V_{db}=\beta V_{db}+(1-\beta)db$
   
# Update W and b

$W=W-\alpha V_{dW}$

$b=b-\alpha V_{db}$

}

----

You now have 2 hyperparameters:

|           |               |
|-----------|---------------|
| $\alpha$  | Learning rate |
| $\beta$   | Control the exponentially weighted average. The most common value for $\beta$ is 0.9 (last 10 iteration's gradient) |

But what about the bias correction: $\frac{V_{t}}{1-\beta^{t}}$

In practice, people don't usually do this because after just ten iterations, your moving average will have warmed up and is no longer a bias estimate.

<img src="../img/warning.png" width="20" /> So in practice, **I don't really see people bothering with bias correction when implementing gradient descent or momentum**.


----

Initialization:

|            |
|------------|
| $V_{dW}=0$ |
| $V_{db}=0$ |

Just for info, sometimes in the AI literature you see:

|                          |                           |
|--------------------------|---------------------------|
| $V_{dW}=\beta V_{dW}+dW$ | with $+(1-\beta)$ omitted |
| $V_{db}=\beta V_{db}+db$ | with $+(1-\beta)$ omitted |

The net effect of using this version is that $V_{dW}$ ends up being scaled by a factor of 1 minus Beta, or really 1 over 1 minus Beta. And so when you're performing these gradient descent updates, alpha just needs to change by a corresponding value of 1 over 1 minus Beta.

In practice, both of these will work just fine, it just affects what's the best value of the learning rate alpha. But I find that this particular formulation is a little less intuitive.

so let's keep:


|                                   |
|-----------------------------------|
| $V_{dW}=\beta V_{dW}+(1-\beta)dW$ |
| $V_{db}=\beta V_{db}+(1-\beta)db$ |