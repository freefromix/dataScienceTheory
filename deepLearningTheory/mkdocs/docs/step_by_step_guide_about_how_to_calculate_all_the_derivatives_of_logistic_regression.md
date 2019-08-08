# Derivatives for logistic regression - step by step

Motivation

The training step in logistic regression involves updating the weights and the bias by a small amount. The amount that each weight and bias is updated by is proportional to the gradients, which are calculated as the partial derivative of the loss function, with respect to the weight (or bias) we are updating.

This blog post will cover how to calculate the partial derivatives of the weights and the bias, step by step. I would recommend reading my previous two blog posts which cover how to perform derivatives along a computational graph ([Simple tutorial about derivatives along a computational graph](./simple_tutorial_about_derivatives_along_a_computational_graph.md)) and the derivative of the sigmoid function ([Simple tutorial about how to calculate derivatives of Sigmoid](./simple_tutorial_about_how_to_calculate_derivatives_of_sigmoid.md)).


## Logistic Regression computational graph

The computational graph of logistic regression can be visualised as follows:

![](img/1_logistic_regression_graph.png)

w and x are vectors, whose size depend on the number of input features. In order to keep things simple, we will consider the case where we only have two input features. We can therefore represent the computational graph more clearly as follows:

![](img/2_logistic_regression_graph_expanded.png)
## Desired partial derivatives

The partial derivatives we are particularly interested are the following two:

![](img/3_dl_dw_and_dl_db_intro.jpg)

## Strategy for solving partial derivatives

In order to solve the partial derivatives, we can make use of the chain rule, which allows us to simplify the process by considering small components at a time.

![](img/4_dl_dw_and_dl_db.jpg)

Which can be visualized on the computational graph as follows:

![](img/5_dl_dw_and_dl_db_on_graph.jpg)

Once we calculate those five smaller components, we can solve the partial derivatives we want more easily. So lets start solving each compoment.

## Component 1

Be aware that the logs used in the loss function are natural logs, and not base 10 logs.

![](img/6_dl_da.jpg)

## Component 2

The full calculation of this component was explained in my previous blog post for calculating the derivative of the sigmoid function. Be sure to check out that post if you want to know how it was calculated.

![](img/7_da_dz.jpg)

## Component 3

![](img/8_dl_dz.jpg)

## Component 4

![](img/9_dz_dw.jpg)

## Component 5

![](img/10_dz_db.jpg)

## Putting the components together

![](img/11_dl_dw.jpg)

![](img/12_dl_db.jpg)

## The final product

To summarize, the derivatives we are interested have been summarized in the following two formulas.

![](img/13_dl_dw_and_dl_db_final.jpg)