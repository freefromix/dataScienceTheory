# Refinements to Beam Search

In this course, you'll learn some little changes that make the beam search algorithm work even better.

## Change to the algorithm

### Change product to sum of log

Length normalization is a small change to the beam search algorithm that can help you get much better results.

**Beam search is maximizing this probability:**

$\displaystyle \arg \max_y \prod_{t=1}^{T_y} P(y^{<t>}|x, y^{<1>},\dots,y^{<t-1>})$

Another way to write the $\displaystyle \prod_{t=1}^{T_y}$ part:

- $P(y^{<1>} y^{<T_y>}|x)=P(y^{<1>}|x)P(y^{<2>}|x,y^{<1>}) \dots P(y^{<T_y>}|x,y^{<1>} \dots y^{<T_y - 1>})$

All probabilities are all numbers less than 1. Often they're much less than 1.

And multiplying a lot of numbers less than 1 will result in:

- A tiny, tiny, tiny number, which can result in numerical underflow.
- Meaning that it's too small for the floating part representation in your computer to store accurately.

**So in practice, instead of maximizing this product, we will take logs:**

Let's insert a log in the first equation:

$\displaystyle \arg \max_y \log{\left(\prod_{t=1}^{T_y} P(y^{<t>}|x, y^{<1>},\dots,y^{<t-1>}\right)}$

Now let's use the properties of logs:

| Properties of logs                          |                                      |
| ------------------------------------------- | ------------------------------------ |
| The log of a product is the sum of the logs: | $\log_{a}xy = \log_{a}x + \log_{a}y$ |

Let's apply:

$\displaystyle \arg \max_y  \sum_{t=1}^{T_y} \log{\left(P(y^{<t>}|x, y^{<1>},\dots,y^{<t-1>})\right)}$

So by taking logs, you end up with a more numerically stable algorithm that is less prone:

- to rounding errors
- numerical rounding errors
- or to numerical underflow.

And because the logarithmic function ![log mono](img/log_mono.png)

is a strictly monotonically increasing function, we know that maximizing:

- $\log P(y|x)$ should give you the same result as maximizing $P(y|x)$.

So in most implementations, you keep track of the sum of logs of the probabilities rather than the product of probabilities.

### Length normalization

$\displaystyle \prod_{t=1}^{T_y} P(y^{<t>}|x, y^{<1>},\dots,y^{<t-1>})$

Looking at this original objective up here, if you have a very long sentence:

- The probability of that sentence is going to be low, because you're multiplying many terms that are less than 1 to estimate the probability of that sentence.
- And so if you multiply all the numbers that are less than 1 together, you just tend to end up with a smaller probability.

**And so this objective function has an undesirable effect: It unnaturally tends to prefer very short translations. It tends to prefer very short outputs.**

Because the probability of a short sentence is determined just by multiplying fewer of these numbers are less than 1.

And so the product would just be not quite as small.

And by the way, the same thing is true for this:

$\log{\left(P(y^{<t>}|x, y^{<1>},\dots,y^{<t-1>})\right)}$

The log of our probability is always less than or equal to 1. You're actually in this range of the log: ![log_x_before_1](img/log_x_before_1.png)

So the more terms you have together, the more negative this thing becomes.

So there's one other change to the algorithm that makes it work better which is:

- instead of using this as the objective you're trying to maximize, **one thing you could do is normalize** this by the number of words in your translation:

Normalization:

$\frac{1}{T_{y}}\log{\left(P(y^{<t>}|x, y^{<1>},\dots,y^{<t-1>})\right)}$

- This takes the average of the log of the probability of each word.
- This significantly reduces the penalty for outputting longer translations.

In practice, as a heuristic instead of dividing by $T_{y}$ (the number of words in the output sentence) sometimes you use a softer approach:

We have $\frac{1}{T_{y}}$:

- If $\alpha=1$ then it is completly normalized by length.
- If $\alpha=0$ then you are not normalizing at all.

Using $\alpha=0.7$:

- is somewhat in between full normalization, and no normalization.
- $\alpha$ is another hyper parameter. You can tune it to try to get the best results.

And I have to admit, using $\alpha$ this way, there isn't a great theoretical justification for it, but people have found this works well in practice. Many people use it.
But if you want you can try out different values of $\alpha$ and see which one gives you the best result.

## To summarize

As you run beam search you see a lot of sentences:

- with length equals 1 (${T_{y}=1$)
- with length equals 2 (${T_{y}=2$)
- with length equals 3 (${T_{y}=3$)
- and so on.. maybe you run beam search for 30 steps and you consider output sentences up to $length=30$
  - If you use a beam width of 3, you will be keeping track of the top 3 possibilities for each of these possible sentence lengths (1, 2, 3, 4 and so on, up to 30).
  
**After that:**

- You can take your top sentences and just compute this objective function onto sentences that you have seen through the beam search process:

$\frac{1}{T_{y}}\log{\left(P(y^{<t>}|x, y^{<1>},\dots,y^{<t-1>})\right)}$

**And then finally:**

- You pick the one that achieves the highest value on this normalized log probability objective (sometimes it's called a normalized log likelihood objective).
- **And then that would be the final translation, your output.**

## how do you choose the beam width B

| pros and cons | The larger B is:  |
|---------------|-------------------|
| Pro: The **more possibilities** you're considering. |
| Pro: **The better the sentence** you probably find. |
| Cons: The **more computationally expensive** your algorithm is because you're also **keeping a lot more possibilities** around. |
| Cons: it will be **slower** |
| And the **memory requirements** will also **grow** |

In our example, we used beam width of B = 3

- In practice, that is on the small side.

| ![important](img/important.png) Commonly used Beam with values in production |
|--------------------------------|
| In production systems, it's not uncommon to see a beam width maybe around 10. |
| A beam width of 100 would be considered very large for a production system, depending on the application. |
| But for research systems where people want to squeeze out every last drop of performance in order to publish the paper with the best possible result. It's not uncommon to see people use beam widths of 1,000 or 3,000, but this is very application, that's why it's a domain dependent. |

So I would say try other variety of values of B as you work through your application.

But when B gets very large, there is often diminishing returns.

- So for many applications, I would expect to see a huge gain as you go from a beam width of 1, which is very greedy search, to 3 or maybe 10.
- But the gains as you go from 1,000 to 3,000 in beam width might not be as big.

And for those of you that have taken maybe a lot of computer science courses before, if you're familiar with computer science search algorithms like BFS, Breadth First Search, or DFS, Depth First Search.

But if you've heard of Breadth First Search and Depth First Search then unlike those algorithms (which are exact search algorithms), beam search runs much faster but does not guarantee to find the exact maximum for this arg max that you would like to find.
