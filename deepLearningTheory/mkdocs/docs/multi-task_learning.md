# Multi-task learning

## Multi-task learning example

__Simplified autonomous driving example__

<img src="../img/screenshot_from_2019-01-24_01-51-42.png" width="400" />

$X^{(i)}$ is the image input

Here is the output:

| Thing to detect | $y^{(i)}$ |
|-----------------|----------|
| Pedestrians | 0 |
| Cars | 1 |
| Stop signs | 1 |
| Traffic lights | 0 |


<img src="../img/screenshot_from_2019-01-24_11-29-04.png" width="650" />

One image can results in multiple labels, therefore the output is not a [Softmax regression](./softmax_regression.md), **this is a Usual Logistic Loss**. In a [Softmax regression](./softmax_regression.md) you can't have multiple output activated a the same time. Here, for example you can detect a car and a stop sign at the same time.

$J(w,b)=\frac{1}{m}\times{\sum_{i=1}^{m}\sum_{j=1}^{4}{\mathcal{l}(\hat{y}_{j}^{(i)},y_{j}^{(i)})}}$

$\sum_{j=1}^{4}$ : Sum only over values of j with a 0 or 1 label.

|               |                                                                                                         |
|---------------|---------------------------------------------------------------------------------------------------------|
| Logistic loss | $\mathcal{l}(\hat{y},y)=-y_{j}^{(i)}\log{\hat{y}_{j}^{(i)}}-(1-y_{j}^{(i)})\log{(1-\hat{y}_{j}^{(i)})}$ |


One image can have multiple labels. If you train a neural network to minimize this cost function, you are carrying out **multi-task learning**.

Indeed... You're building a single neural network that is looking at each image and **basically solving four problems** (does each image have each of these four objects in it?).

**We could use one NN for each of these tasks (4 NN in our case) but training one neural network to do four things results in better performance.**

### Training with images that are fully labeled

In one image, let's say there's a pedestrian, there's no car, but they didn't bother to label whether or not there's a stop sign or whether or not there's a traffic light.

| Label | Result |
|-------|--------|
| Pedestrian | 1 |
| Car | 1 |
| Stop | ? |
| Traffic light | ? |


$$Y=
 \begin{pmatrix}
  1 & 1 & 0 & ? \\
  0 & 1 & 1 & 1 \\
  \vdots  & \vdots  & \vdots & \vdots  \\
  ? & ? & 1 & 0 \\
  ? & 0 & 1 & ? \\
 \end{pmatrix}$$

|                                                 ||||
|-------------------------------------------------||||
| **It works but be careful with the following:** ||||
| <img src="../img/warning.png" width="80" />| Even when some of these labels are question marks in this sum over j from 1 to 4 | **Sum only over values of j with a 0 or 1 label** | **"?" can not enter the loss calculus. Only 0 or 1 enter the loss calculus.** |

## When multi-task learning makes sense

- **Training on a set of tasks that could benefit from having shared lower-level features.**
- **Usually: Amount of data you have for each task is quite similar.** Imagine you need to recognize 100 objects, may have 1,000 examples per each object.
  - **If you focus on one task, the other tasks should have in total more examples than the focused task.**
  - For example: Focused task:1000 examples, other tasks: much more than 1000 examples in total.
- **Can train a big enough neural network to do well on all the tasks.** What a researcher, Rich Carona, found many years ago was that the only times multi-task learning hurts performance compared to training separate neural networks is if your neural network isn't big enough. 


Remember: If you can train a big enough neural network, then **multi-task learning certainly should not or should very rarely hurt performance. **And hopefully it will actually help performance** compared to if you were training neural networks to do these different tasks in isolation. 


Maybe the one example is computer vision. In object detection I see more applications of multi-task any where** one neural network trying to detect a whole bunch of objects at the same time works better than different neural networks trained separately to detect objects.**

