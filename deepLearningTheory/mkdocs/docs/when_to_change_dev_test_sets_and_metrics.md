# When to change dev/test sets and metrics

Cat dataset examples

Metric classification error:

| Algorithm | Error | Other behavior |
|-----------|-------|----------------|
| Algorithm A | 3% error | Shows pornographic images to the user |
| Algorithm B | 5% error | Does not show pornographic images to the user |

A is the best algorithm, but **you/your users prefer algorithm B**.

Then that's a sign that **you should change your evaluation metric** or perhaps **your development set or test set**.
## Solution

### Changing your evaluation metric

$Error=\frac{1}{m_{dev}}\sum_{i=1}^{m_{dev}}I\{y_{pred}^{(i)}\neq y^{(i)}\}$ 

With $I\{y_{pred}^{(i)}\neq y^{(i)}\}$=Indicator of the fact that the prediction is valid or not = True or False = (1 or 0)

**One way of changing the evaluation metric is to add**: $w^{(i)}$

|                                        |  |
|----------------------------------------|--|
| $w^{(i)}$ = 1 if $X^{(i)}$ is not porn |  |
| $w^{(i)}$ = 10 or larger value if $X^{(i)}$ is porn | In this example you are giving 10 times bigger weights to classify pornographic images correctly |
| $Error=\frac{1}{\sum_{i=1} w^{(i)}}\sum_{i=1}^{m_{dev}}w^{(i)}I\{y_{pred}^{(i)}\neq y^{(i)}\}$ | Note: To still have the error between 0 and 1 you have to multiply by $\frac{1}{\sum_{i=1} w^{(i)}}$ |

### How to well on this new metric

To do so, modify the cost function in order to incorporate these weights and maybe end up changing this normalization constant as well. 

$J=\frac{1}{\sum_{i=1} w^{(i)}}\sum_{i=1}^{m_{dev}}w^{(i)}L(\hat{y}^{(i)},y^{(i)})$ 

## Another example

We have a cat app, here are the result of the dev set:

| Algorithm | Error | Other behavior |
|-----------|-------|----------------|
| Algorithm A | 3% error |  |
| Algorithm B | 5% error |  |

Algorithm A works better on the dev set, but when you deploy your algorithm product, you find that Algorithm B actually is  performing better.

You discover why:

|              |                                                                                     |
|--------------|-------------------------------------------------------------------------------------|
| Training set | You've been training off very nice high quality images downloaded off the Internet. |
| Real world deployed app | Users are uploading all sorts of pictures, they're much less framed, cats have funny facial expressions, maybe images are much blurrier. |

<img src="../img/screenshot_from_2019-01-17_16-44-47.png" width="400" />

|                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------|
| **If doing well on your metric + dev/test set does not correspond to doing well on your application**, **change your metric and/or dev/test set**. |

## Guideline

- Having an evaluation metric and the dev set allows you to much more quickly make decisions
- It really speeds up how quickly you and your team can iterate. 

So my recommendation is, even if you can't define the perfect evaluation metric and dev set, just set something up quickly and use that to drive the speed of your team iterating. 

And if later down the line you find out that it wasn't a good one, you have better idea, change it at that time, it's perfectly okay. B

ut what I recommend against for the most teams is **don't run for too long without any evaluation metric and dev set up** because that can slow down the efficiency of what your team can iterate and improve your algorithm. 
