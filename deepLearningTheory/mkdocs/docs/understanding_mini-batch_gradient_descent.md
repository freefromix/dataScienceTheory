# Understanding mini-batch gradient descent

## Batch vs mini-batch gradient descent

<img src="../img/screenshot_from_2018-12-31_15-56-31.png" width="800" />

|       |      |
|-------|------|
| Batch | X, Y |
| Mini-batch | $X^{\{t\}}, Y^{\{t\}}$ |

<img src="../img/mini-batch_gradient_descent.png" width="800" />

| Term   | Definition                                                                       |
|--------|----------------------------------------------------------------------------------|
| Epoch  | One epoch = one forward pass and one backward pass of all the training examples  |

<img src="../img/screenshot_from_2019-01-01_11-02-54.png" width="800" />

So if you plot $J^{\{t\}}$, as you're training mini batch in descent it may be over multiple epochs. It doesn't go down on every derivation, but it should trend downwards. 

The reason it'll be a little bit noisy is that, maybe $X^{\{1\}}$, $Y^{\{1\}}$ is just the rows of easy mini batch so your cost might be a bit lower, but then maybe just by chance, $X^{\{2\}}$, $Y^{\{2\}}$ is just a harder mini batch.

## Choose the size of your mini-batch

| Mini-batch size  | Name | Example | Color in image |
|------------------|------|---------|----------------|
| mini-batch size = m | Batch gradient descent | $(X^{\{1\}}, Y^{\{1\}}) = (X,Y)$ | Blue line |
| mini-batch size = 1 | Stochastic gradient descent, you process one single example all the time. | Every example is his own mini-batch $(X^{\{1\}}, Y^{\{1\}}) \cdots (X^{\{m\}}, Y^{\{m\}})$ | Violet line |
| mini-batch size between 1 and m | Solution: faster learning | Solution | Green line |

Here what happens during gradient descent:
<img src="../img/screenshot_from_2019-01-01_11-43-40.png" width="200" />

### Ideal size of your mini-batch

|  Training set size                      | Mini-batch size                                                                                                                  |
|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Small training set: $m\leqslant 2000$  | Use batch gradient descent                                                                                                       |
| Big training set: $m\geqslant 2000$    | Use a power of 2 mini-batch size: 64, 128, 256, 512, 1024 ... etc. Make sure that you mini-batch size fit in you CPU/GPU memory  |

In practice of course the mini batch size is another hyper parameter that you might do a quick search over to try to figure out which one is most sufficient of reducing the cost function j. 

So what i would do is just try several different values. Try a few different powers of two and then see if you can pick one that makes your gradient descent optimization algorithm as efficient as possible. 