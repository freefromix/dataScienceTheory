# Practical aspects of Deep Learning

## Train / Dev / Test sets

Your data will be split into three parts:

- Training set. (Has to be the largest set)
- Hold-out cross validation set / Development or "dev" set.
- Testing set.


The trend on the ratio of splitting the models:

- If size of the dataset is 100 to 1000000 ==> 60/20/20
- If size of the dataset is 1000000 to INF ==> 98/1/1 or 99.5/0.25/0.25

|                                                                           |
|---------------------------------------------------------------------------|
| **Make sure the dev and test set are coming from the same distribution.** |

For example if cat training pictures is from the web and the dev/test pictures are from users cell phone they will mismatch. It is better to make sure that dev and test set are from the same distribution.

- The dev set rule is to try them on some of the good models you've created.
- Its OK to only have a dev set without a testing set. But a lot of people in this case call the dev set as the test set. A better terminology is to call it a dev set as its used in the development