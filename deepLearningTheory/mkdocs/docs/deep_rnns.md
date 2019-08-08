# Deep RNNs

For learning very complex functions sometimes is useful to stack multiple layers of RNNs together to build even deeper versions of these models.

| Notation     | Explanation                     |
| ------------ | ------------------------------- |
| $a^{[l]<t>}$ | activation layer l over time t. |

![deep_rnns](img/deep_rnns.png)

Example:

$a^{[2]<3>}= g(W_a[a^{[2]<2>}, a^{[1]<3>}]+b_a^{[2]})$

Quite often the blocks don't just have to be standard RNN, the simple RNN model.

They can also be **GRU blocks** or **LSTM blocks**.

And finally, you can also build deep versions of the **bidirectional RNN**.

## How deep

For RNNs, having **3 layers is already quite a lot**.

Because of the temporal dimension, these networks can already get quite big even if you have just a small handful of layers.

One thing you do see sometimes is that you have recurrent layers that are stacked on top of each other.

You just have a bunch of deep layers that are not connected horizontally but have a deep network here that then finally predicts $y^{<1>}$.

Like this for example:

<img src="../img/deep_rnns_deepa.png" width="200" />

## RNNs are quite computationally expensive to train

Because deep RNNs are quite computationally expensive to train, there's often a large temporal extent already, though you just don't see as many deep recurrent layers.

You don't see as many deep recurrent layers as you would see in a number of layers in a deep conventional neural network.

