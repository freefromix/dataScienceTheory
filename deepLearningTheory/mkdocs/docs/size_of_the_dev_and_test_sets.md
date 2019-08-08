# Size of the dev and test sets

## Before deep learning

<img src="../img/screenshot_from_2019-01-17_07-24-51.png" width="400" />

Your sets contains 100, 1000, 10000 examples:
* Train 70% / Test 30%
* Train 60% / Dev 20% / Test 20%

## Deep learning era

<img src="../img/screenshot_from_2019-01-17_07-34-43.png" width="400" />

Your sets contains 1 000 000 examples:
* Train 98% / Dev 1% / Test 1%

## Guideline

**Set your test set to big enough to give high confidence in the overall performance of your system.
**

The **trend** has been to use **more data for training and less for dev and test**, especially when you have a **very large data sets**.

Maybe you don't need millions and millions of examples in a test set.
Maybe for your application if you think that having 10,000 examples gives you enough confidence to find the performance on maybe 100,000 or whatever it is, that might be enough. 
And this could be much less than, say 30% of the overall data set, depend on how much data you have.

For some applications, maybe you don't need a high confidence in the overall performance of your final system. Maybe all you need is a train and dev set.

And I think, not having a test set might be okay. 

Although I think in the history of machine learning, not everyone has been completely clean and completely records of about calling the dev set when it really should be treated as test set.