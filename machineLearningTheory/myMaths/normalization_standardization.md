# Normalization and standardization

## Normalize

Why would we normalize in the first place?

1. Normalization makes training less sensitive to the scale of features, so we can better solve for coefficients.
2. The use of a normalization method will improve analysis from multiple models.
3. Normalizing will ensure that a convergence problem does not have a massive variance, making optimization feasible.


**Normalization put all your data in a scale from 0 to 1.** This is usually called feature scaling.

Here your data Z is rescaled such that any specific z$ will now be $0\leq z \leq1$, and is done through this formula:

$z = \frac{x - min(x)}{max(x) - min(x)}$

Imagine the following problem:

During the last 14 days you have data. You do:

normalized = (today's close - lowest value of the 14 days) / (Highest high of 14 days - Lowest low of the 14 days)

## Standardize

On the other hand, you can use standardization on your data set. 

Why would we do this?

1. Compare features that have different units or scales.
2. Standardizing tends to make the training process well behaved because the numerical condition of the optimization problems is improved.

It will then transform it to have zero mean and unit variance, for example using the equation below.

All data is express in standard deviation.

$z = \frac{x_i - \mu}{\sigma}$

$\mu$: mean value
$\sigma$: standard deviation


Consider if you're doing PCA (principal component analysis), the output can only be interpreted correctly when the features have first been centred around their means. Again, understanding what you want to achieve and the model you'll be using, are necessary conditions to understanding different transformations decisions.

However, if you do standardize your data be warned you might be discarding some information. If that information is not needed, the process can be helpful else it will impede your results.

