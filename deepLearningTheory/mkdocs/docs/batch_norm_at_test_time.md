# Batch Norm at test time

|   |                   |                                   |
|---|-------------------|-----------------------------------|
| 1 | Compute the means | $\mu=\frac{1}{m} \sum_{i}Z^{(i)}$ |
| 2 | Subtract the means from your training sets | $Z^{(i)}new=Z^{(i)}-\mu$ |
| 3 | Calculate the variance | $\sigma^{2} = \frac{1}{m}\sum_{i=1}^{m}(Z^{(i)}-\mu)^{2}=\frac{1}{m}\sum_{i=1}^{m}(Znew^{(i)})^{2}$ (element wise squaring) |
| 4 | Normalize the dataset according to the variances | $Z^{(i)}norm=\frac{Z^{(i)}new}{\sqrt{\sigma^{2}+\epsilon}}$ |
| 5 | If you want to use Ztilde as final value | $Ztilde^{(i)}=\gamma Z^{(i)}norm + \beta$ |

So, notice that $\mu$ and $\sigma^{2}$ which you need for this scaling calculation are computed on the entire mini batch.

**But at test time you might not have a mini batch of 6428 or 2056 examples to process at the same time.

So, you need some different way of coming up with $\mu$ and $\sigma^{2}$.**

## Estimate $\mu$ and $\sigma^{2}$ with exponentially weighted average

First remind that [exponentially weighted average](./exponentially_weighted_average.md) has already been explained.

Let's estimate this using a exponentially weighted average where the average is **across the mini batches**.

Example:

Let's pick a layer l

We are going through the minibatches: $X^{\{1\}},X^{\{2\}},X^{\{3\}}\cdots$

To each minibatch we are getting the corresponding $\mu$.

|             | $\mu=\frac{1}{m} \sum_{i}Z^{(i)}$ | $\sigma^{2}=\frac{1}{m}\sum_{i=1}^{m}(Znew^{(i)})^{2}$ |
|-------------|-----------------------------------|--------------------------------------------------------|
| $X^{\{1\}}$ | $\mu^{\{1\}[l]}$ | $\sigma^{2\{1\}[l]}$ |
| $X^{\{2\}}$ | $\mu^{\{2\}[l]}$ | $\sigma^{2\{2\}[l]}$ |
| $X^{\{3\}}$ | $\mu^{\{3\}[l]}$ | $\sigma^{2\{3\}[l]}$ |
| $\cdots$    | $\cdots$         | $\cdots$             |

When you calculate Znorm ($Z^{(i)}norm=\frac{Z^{(i)}new}{\sqrt{\sigma^{2}+\epsilon}}$) you would be using your exponentially weighted average of the $\mu$ and $\sigma^{2}$ whatever was the latest value you have to do the scaling here.

 And then you would compute $Ztilde^{(i)}=\gamma Z^{(i)}norm + \beta$ on your one test example using that Z norm that we just computed on the left and using the $\beta$ and $\gamma$ parameters that you have learned during your neural network training process. 

## Takeway

So the takeaway from this is that during training time $\mu$ and $\sigma^2$ are computed on an entire mini batch of say 64 engine, 28 or some number of examples. But at test time, you might need to process a single example at a time.

So, the way to do that is to estimate $\mu$ and $\sigma^2$ from your training set and there are many ways to do that. You could in theory run your whole training set through your final network to get $\mu$ and $\sigma^2$ squared.

But in practice, what people usually do is implement an exponentially weighted average where you just keep track of the $\mu$ and $\sigma^2$ squared values you're seeing during training and use an exponentially weighted average, also sometimes called the running average, to just get a rough estimate of $\mu$ and $\sigma^2$ and then you use those values of $\mu$ and $\sigma^2$ that test time to do the scale and you need the head and unit values Z.

In practice, this process is pretty robust to the exact way you used to estimate $\mu$ and $\sigma^2$.

----

Different than random initialization, Batch Norm is built into the network and back propagation is also works for Batch Norm. So it's part of the network, you cannot ignore them when using the network after training.

The problem here is for the normalization we need to calculate the mean and variance, which we don't have during testing. So we use a moving average to "remember" such value during training and reuse it for testing.

----

What he said was "any reasonable way to estimate the mean and variance of your hidden unit values Z should work fine at test" and offered the exponentially weighted average as one example of how it can be done.

Why he chose the exponentially weighted average? I think it's because that's the one he spoke about in the week before. I actually think your idea would work just fine, and I actually prefer it.

The original paper (https://arxiv.org/pdf/1502.03167.pdf) says that, at testing time, population statistics can be used (see 3.1). I'm not sure how that works for activations though.
