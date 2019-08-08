# Notation Recurrent Neural Networks

## Example

Recognition systems can be used to find:

- people's names
- companies names
- times
- locations
- countries names
- currency names
- and so on in different types of text.

|  Input   |   Sentence                  |
|----------|-----------------------------|
| x        | "Harry Potter and Hermione Granger invented a new spell" |

You want a sequence model to automatically tell you where are the peoples names in this sentence.

So, this is a problem called:

- **Named-entity recognition**

Named-entity recognition is **used by search engines** for example:

- to index all of say the last 24 hours news of all the people mentioned in the news articles so that they can index them appropriately.

Now, given this input x let's say that you want:

- a model to operate y
  - that has one outputs per input word
- and the target output tells you for each of the input words
  - if it is that part of a person's name.

For example

**INPUT:**

| Harry | Potter | and | Hermione | Granger | invented | a | new | spell |
|-------|--------|-----|----------|---------|----------|---|-----|-------|
| $x^{<1>}$ | $x^{<2>}$ | $x^{<3>}$ | $x^{<4>}$ | $x^{<5>}$ | $x^{<6>}$ | $x^{<7>}$ | $x^{<8>}$ | $x^{<9>}$ |

**OUTPUT:**

| $y^{<1>}$ | $y^{<2>}$ | $y^{<3>}$ | $y^{<4>}$ | $y^{<5>}$ | $y^{<6>}$ | $y^{<7>}$ | $y^{<8>}$ | $y^{<9>}$ |
|-------|--------|-----|----------|---------|----------|---|-----|-------|
| 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 |

## Notation

| notation | Definition |
|-----------|----------------------------------------------|
| $x^{<t>}$ | t = index into the positions in the sequence |
| $T_x$ | length of the input sequence | (Example above: $T_x=9$) |
| $T_y$ | length of the output sequence | (Example above: $T_y=9$) |
| $T_{x}^{(i)}$ | length of the input sequence for training example i |
| $T_{y}^{(i)}$ | length of the output sequence for training example i |
| $x^{(i)<t>}$ | the output sequence for training example i and training example t |
| $y^{(i)<t>}$ | output sequence for training example i and training example t |
| $W_{ax}$ | The fist subscript letter $a$ means that this matrix is used to compute $a^{<t>}$ output.  |
| $W_{ya}$ | The fist subscript letter $y$ means that this matrix is used to compute $\hat{y}^{<t>}$ output.  |


## Dictionnary

Let's talk about how we would represent individual words in a sentence:

Sometimes also called a Dictionary and that means making a list of the words that you will use in your representations.

$\begin{bmatrix}
    a \\
    aaron \\
    \vdots \\
    and \\
    \vdots \\
    harry \\
    \vdots \\
    potter \\
    \vdots \\
    zulu
\end{bmatrix}\begin{matrix}
    1 \\
    2 \\
    \vdots \\
    367 \\
    \vdots \\
    4075 \\
    \vdots \\
    6830 \\
    \vdots \\
    10000
\end{matrix}$

10,000 words is quite small by modern NLP applications.

For commercial applications:

- dictionary sizes of 30 to 50,000 are more common and 100,000 is not uncommon.
- And then some of the large Internet companies will use dictionary sizes that are maybe a million words or even bigger than that.

- But you see a lot of commercial applications used dictionary sizes of maybe 30,000 or maybe 50,000 words.

- Here we use 10,000 for illustration.

## Example representation

| Harry | Potter | and | Hermione | Granger | invented | a | new | spell |
|-------|--------|-----|----------|---------|----------|---|-----|-------|
| $x^{<1>}$ | $x^{<2>}$ | $x^{<3>}$ | $x^{<4>}$ | $x^{<5>}$ | $x^{<6>}$ | $x^{<7>}$ | $x^{<8>}$ | $x^{<9>}$ |

| x  |   | x |   |
|---|---|---|---|
| $x^{<1>}$ | $=\begin{bmatrix} 0 \\ 0 \\ \vdots \\ 0 \\ \vdots \\ 1 \\ \vdots \\ 0 \\ \vdots \\ 0 \end{bmatrix}\begin{matrix} 1 \\ 2 \\ \vdots \\ 367 \\ \vdots \\ 4075 \\ \vdots \\ 6830 \\ \vdots \\ 10000 \end{matrix}$ | $x^{<2>}$ | $=\begin{bmatrix} 0 \\ 0 \\ \vdots \\ 0 \\ \vdots \\ 0 \\ \vdots \\ 1 \\ \vdots \\ 0 \end{bmatrix}\begin{matrix} 1 \\ 2 \\ \vdots \\ 367 \\ \vdots \\ 4075 \\ \vdots \\ 6830 \\ \vdots \\ 10000 \end{matrix}$ |
| $x^{<3>}$ | $=\begin{bmatrix} 0 \\ 0 \\ \vdots \\ 1 \\ \vdots \\ 0 \\ \vdots \\ 0 \\ \vdots \\ 0 \end{bmatrix}\begin{matrix} 1 \\ 2 \\ \vdots \\ 367 \\ \vdots \\ 4075 \\ \vdots \\ 6830 \\ \vdots \\ 10000 \end{matrix}$ | $\cdots$ | $\cdots$ |
| $x^{<7>}$ | $=\begin{bmatrix} 0 \\ 0 \\ \vdots \\ 1 \\ \vdots \\ 0 \\ \vdots \\ 0 \\ \vdots \\ 0 \end{bmatrix}\begin{matrix} 1 \\ 2 \\ \vdots \\ 367 \\ \vdots \\ 4075 \\ \vdots \\ 6830 \\ \vdots \\ 10000 \end{matrix}$ | $\cdots$ | $\cdots$ |


- Superscript $[l]$ denotes an object associated with the $l^{th}$ layer. 
    - Example: $a^{[4]}$ is the $4^{th}$ layer activation. $W^{[5]}$ and $b^{[5]}$ are the $5^{th}$ layer parameters.

- Superscript $(i)$ denotes an object associated with the $i^{th}$ example. 
    - Example: $x^{(i)}$ is the $i^{th}$ training example input.

- Superscript $\langle t \rangle$ denotes an object at the $t^{th}$ time-step. 
    - Example: $x^{\langle t \rangle}$ is the input x at the $t^{th}$ time-step. $x^{(i)\langle t \rangle}$ is the input at the $t^{th}$ timestep of example $i$.
    
- Lowerscript $i$ denotes the $i^{th}$ entry of a vector.
    - Example: $a^{[l]}_i$ denotes the $i^{th}$ entry of the activations in layer $l$.