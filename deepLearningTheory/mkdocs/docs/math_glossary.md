

**Stochastics**: An ongoing process where the next state might depend on both the **previous state** and **some random elements**.

**Multinomial distribution**: It is a generalisation of the binomial distribution. It is used when there is more than 2 possible outcomes.

**Harmonic mean**: Typically, the harmonic mean is appropriate for situations when the average of rates or ratios is desired.

$$Harmonic\_mean = \frac{n}{1/x_1 + 1/x_2 + ... + 1/x_n} = \frac{n}{\sum_{i=1}^{n} \frac{1}{x_{i}}}$$

**classification_report**:

- precision: For all instances classified positive, what percent was correct?
  
$$precision = \frac{truePositives}{truePositives+falsePositives}$$

- recall: For all instances that were actually positive, what percent was classified correctly?

$$recall = \frac{truePositives}{truePositives+falseNegatives}$$

- f1 score: Combining Precision and Recall using harmonic mean.

$$f1Score = 2*\frac{precision \times{recall}}{precision + recall}$$