# Setting up your Machine Learning Application

## Train Dev Test sets

<img src="../img/dataset.png" width="500" />

And so the workflow is the following:

|              |                                                        |
|--------------|--------------------------------------------------------|
| Training set | You keep on training algorithms on your training sets. |
| Dev set | You use your dev set to see which of many different models performs best. Do that until you have a final  model. So the dev set just needs to be big enough for you to evaluate, say, two different algorithm choices or ten different algorithm choices and quickly decide which one is doing better. And you might not need a whole 20% of your data for that. |
| Test set | When you have a final model that you want to evaluate, you can take the best model you have found and evaluate it on your test set. |

----

So in the previous era of machine learning, it was common practice to take all your data and split it according to maybe a 70/30% in terms of a people often talk about the 70/30 train test splits. I


| Era           | Dataset size                | Repartition              |
|---------------|-----------------------------|--------------------------|
| Previous era of machine learning | 100-1000-10000 records  | 70% training, 30% tests  |
| Big Data  | 1 000 000 records  | 98% training, 1% dev, 1% test |

<img src="../img/screenshot_from_2018-12-23_18-18-27.png" width="400" />

Make sure that your test and training data come from the same distribution (same kind of resolution for images etc.).

Make sure that your test and dev data come from the same distribution. 

Not having a test set is ok. (only dev set).

## Bias / Variance

<img src="../img/bias_variance.png" width="400" />

  * The bias is an error from erroneous assumptions in the learning algorithm. High bias can cause an algorithm to miss the relevant relations between features and target outputs (underfitting).
  * The variance is an error from sensitivity to small fluctuations in the training set. High variance can cause an algorithm to model the random noise in the training data, rather than the intended outputs (overfitting).



<img src="../img/screenshot_from_2018-12-23_18-45-11.png" width="500" />

High bias + high variance:
<img src="../img/screenshot_from_2018-12-23_18-48-11.png" width="300" />

So this classifier kind of has high bias because it was mostly linear, but you need maybe a curve function or quadratic function. And it has high variance, because it had too much flexibility to fit those two mislabel, or those live examples in the middle as well. In case this seems contrived, well, this example is a little bit contrived in two dimensions, but with very high dimensional inputs. You actually do get things with high bias in some regions and high variance in some regions, and so it is possible to get classifiers like this in high dimensional inputs that seem less contrived. 

## Basic Recipe for Machine Learning



| Symptom                                | What you can do                                                                                                          |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| High bias (training data performance)  | Try **bigger network** or **train longer** or find a **new network architecture** that's better suited for this problem  |
| High variance                          | Get **more data** or **regularization** or find a **new network architecture** that's better suited for this problem                                                                                                                        |

Bias–variance tradeoff: In the modern deep learning, big data era: 
  * So long as you can keep training a bigger network, and so long as you can keep getting more data, then getting a bigger network almost always just reduces your bias without necessarily hurting your variance, so long as you regularize appropriately.
  * And getting more data pretty much always reduces your variance and doesn't hurt your bias much.

Training a bigger NN almost never hurts.
