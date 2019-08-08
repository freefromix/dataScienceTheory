# Computer Vision

<img src="../img/screenshot_from_2019-01-29_07-42-26.png" width="400" />

If you have three million input features, then this means that X here will be three million dimensional.

- If you use a standard or fully connected network fist layer has  1000 hidden units.
- The weight matrix W1, will be (1000, 3M) dimensional matrix. 
  - Because of this, **W1 will have 3 billion parameters** which is just very, very large. And with that many parameters, it's **difficult** to get enough data to **prevent a neural network from overfitting**. And also, the computational requirements and the **memory requirements to train a neural network with three billion parameters is just a bit infeasible.**
