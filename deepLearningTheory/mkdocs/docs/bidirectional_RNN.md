# bidirectional RNN

## Getting information from the future

A bidirectional RNN works as follows:

![rnn](img/rnn_bidirectional.png)

I'm going to use a simplified 4 inputs or maybe a 4 word sentence.

So we have 4 inputs. $x^{<1>}$ through $x^{<4>}$.

| This networks will have:  | |
|------------------------------|----------------------------|
| **Forward** recurrent components | $\overrightarrow{a}^{\ <t>}$ |
| **Backward** recurrent components | $\overleftarrow{a}^{\ <t>}$ |

And this $\overleftarrow{a}^{\ <t>}$ backward connections will be connected to each other **going backward in time**.

So, notice that this network defines an **"Acyclic graph"**.

## How does it work

Given an input sequence $x^{<1>}$ through $x^{<4>}$:

**STEP 1: FORWARD SEQUENCE**

- The **forward sequence (green lines)** will first compute $\overrightarrow{a}^{\ <1>}$,
  -  then use that to compute $\overrightarrow{a}^{\ <2>}$, then $\overrightarrow{a}^{\ <3>}$, then $\overrightarrow{a}^{\ <4>}$.
  - And also, each of these 4 recurrent units inputs the current x, and then feeds in to help predict $\hat{y}^{<1>}$, $\hat{y}^{<2>}$, $\hat{y}^{<3>}$, and $\hat{y}^{<4>}$.
  
**STEP 2: BACKWARD SEQUENCE**

- The **backward sequence (violet lines)** will first compute $\overrightarrow{a}^{\ <4>}$,
  -  then use that to compute $\overrightarrow{a}^{\ <3>}$, then $\overrightarrow{a}^{\ <2>}$, then $\overrightarrow{a}^{\ <1>}$.
  - And also, each of these 4 recurrent units inputs the current x, and then feeds in to help predict $\hat{y}^{<4>}$, $\hat{y}^{<3>}$, $\hat{y}^{<2>}$, and $\hat{y}^{<1>}$.


**STEP 3: PREDICTION**

And then finally having computed all you had in the activations, you can then make your predictions with your 
$[\overrightarrow{a}^{\ <t>}, \overleftarrow{a}^{\ <t>}]$ pairs:

| Formula $\hat{y}^{<t>}$ |
|---------|
| $\hat{y}^{<t>}=g(W_{y} [\overrightarrow{a}^{\ <t>}, \overleftarrow{a}^{\ <t>}]+b_{y})$ |

### Example

Let's look at the example $\hat{y}^{<3>}$ if we have 4 inputs.

The prediction at $\hat{y}^{<3>}$ take as input:

- Information from the past: Forward sequence $\overrightarrow{a}^{\ <1>}$, $\overrightarrow{a}^{\ <2>}$.
- Information from the future: Backward sequence $\overleftarrow{a}^{\ <4>}$.
- Information from the present: $x^{<4>}$


So, in particular, given a phrase like, "He said, Teddy Roosevelt..."

To predict whether Teddy is a part of the person's name, you take into account information from the past and from the future.

## A note on the bidirectional blocks

So this is the bidirectional recurrent neural network and these blocks here can be not just the standard RNN block but they can also be GRU blocks or LSTM blocks.

**In fact, for a lots of Natural Language Processing problems, a bidirectional RNN with a LSTM appears to be commonly used.**

So, we have NLP problem and you have the complete sentence, you try to label things in the sentence, **a bidirectional RNN with LSTM blocks both forward and backward would be a pretty views of first thing to try.**

## Bidirectional RNN disadvantage

The disadvantage of the bidirectional RNN is that:

- **You do need the entire sequence of data before you can make predictions anywhere.**

So, for example, if you're building a speech recognition system, then the BRNN will let you take into account the entire speech utterance.

**But if you use this straightforward implementation, you need to wait for the person to stop talking to get the entire utterance before you can actually process it and make a speech recognition prediction.**

So for a real type speech recognition applications, they're somewhat more complex modules as well rather than just using the standard bidirectional RNN as you've seen here.

But for a lot of natural language processing applications where you can get the entire sentence all the same time, the standard BRNN algorithm is actually very effective.

