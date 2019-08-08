# Language model and sequence generation

Let's say you're building this speech recognition system and you hear the sentence, the apple and pear salad was delicious.

Did I say?

- The apple and pair salad.
- The apple and pear salad.

A good speech recognition system would help with this problem even though these two sentences sound exactly the same.

And the way a speech recognition system picks the second sentence is by using a language model which tells it **what the probability is of either of these two sentences**.

For example, a language model might say that:

- P(The apple and pair salad)=$3.2 \times 10^{-13}$
- P(The apple and pear salad)=$5.7 \times 10^{-10}$

**Language systems and translation systems want to output sentences that are likely.**

Here the second sentence is much more likely.

So what a language model does is:

- given any random sentence
- What is the probability **P(Sentence)** of that particular sentence. More in details: Whats is the probability of that particular sequence of words $P(y^{<1>}, y^{<2>} \dots y^{<T_{y}>})$.
  - Example: What is the chance that the next sentence you use somewhere out there in the world will be a particular sentence like "the apple and pear salad"?

## How to build a language model

| Training set |
|--------------|
| Lage corpus of english text (Or text from whatever language you want to build a language model of) |

**Word corpus**: Is an NLP (Natural Language Processing) terminology that just means a large body or a very large set of english text of english sentences.

Example:

| $y^{<1>}$ | $y^{<2>}$ | $y^{<3>}$ | $y^{<4>}$ | $y^{<5>}$ | $y^{<6>}$ | $y^{<7>}$ | $y^{<8>}$ | $y^{<9>}$ |
|------|---------|----|-------|------|-----|---|-----|-----|
| Cats | average | 15 | hours | of | sleep | a | day. | EOS |

### EOS and period

![important](img/important.png) **Another common thing to do is to add an extra token called a EOS. That stands for End Of Sentence that can help you figure out when a sentence ends.** The EOS token can be appended to the end of every sentence in your training sets if you want your models explicitly capture when sentences end.

The sentence would then be: "Cats average 15 hours of sleep a day EOS"

And doing the tokenization step, you can decide whether or not the period (.) should be a token as well.

In this example, we are ignoring punctuation.

**If you want to treat the period or other punctuation as explicit token, then you can add the period to your vocabulary as well.**

| $y^{<1>}$ | $y^{<2>}$ | $y^{<3>}$ | $y^{<4>}$ | $y^{<5>}$ | $y^{<6>}$ | $y^{<7>}$ | $y^{<8>}$ | $y^{<9>}$ |
|------|---------|----|-------|------|-----|---|-----|-----|
| Cats | average | 15 | hours | of | sleep | a | day. | EOS |

### Tokenisation step: words in your training set that are not in your vocabulary

| Example |
|---------|
| "The Egyptian Mau is a bread of cat EOS" |

Your vocabulary:

- 10 000 most common words
- the word "Mau" (a special breed of cat) is not part of your 10 000 tokens

In that case you need to replace 'Mau' with a unique token called UNK (unknown words).

| Example |
|---------|
| "The Egyptian UNK is a bread of cat EOS" |

### Let's build the RNN model

| $y^{<1>}$ | $y^{<2>}$ | $y^{<3>}$ | $y^{<4>}$ | $y^{<5>}$ | $y^{<6>}$ | $y^{<7>}$ | $y^{<8>}$ | $y^{<9>}$ |
|------|---------|----|-------|------|-----|---|-----|-----|
| Cats | average | 15 | hours | of | sleep | a | day | EOS |

This will be the RNN:

![rnn language](img/rnn_language.png)

Remember the Probability Notation in math:

- P( something | something else ) = Probability of "something" **GIVEN** "something else".

Steps at time 0:

| $a^{<1>}$ |
|-----------|
| You end up computing some activation $a^{<1>}$ as a function of some inputs $x^{<1>}$, and $x^{<1>}$ will be a 0 vector. |
| $a^{<1>}$ will make a **softmax** prediction to try to figure out what is the probability of the first words $y^{<1>}$. |
| What is the probability of any word in the dictionary? <br> **P(10002 words)** because our $dictionnary = 10 000\ words + UNK + EOS$ |
| The result is then a **10 002 output softmax**. |

| $a^{<2>}$ |
|-----------|
| $a^{<2>}$ will try to figure out what is the second word. |
| But now we will also give it the correct first word ($y^{<1>}=cats$). Then we can write: $x^{<2>}=y^{<1>}=Cats$ |
| $P(10002\ words \vert Cats)$ |

| $a^{<3>}$ |
|-----------|
| $a^{<3>}$ will try to figure out what is the third word. |
| But now we will also give it the correct 2 words ($y^{<2>}=Cats\ average$). Then we can write: $x^{<3>}=y^{<2>}=Cats\ average$ |
| $P(10002\ words \vert Cats\ average)$ |

etc.

| $a^{<9>}$ |
|-----------|
| $a^{<9>}$ will try to figure out what is the last word. |
| But now we will also give it the correct precedent sequence of words ($y^{<2>}=Cats\ average\ 15\ hours\ of\ sleep\ a\ day$). Then we can write: $x^{<9>}=y^{<8>}=Cats\ average\ 15\ hours\ of\ sleep\ a\ day$ |
| $P(10002\ words \vert Cats\ average\ 15\ hours\ of\ sleep\ a\ day)$ |
| Should find EOS |

| Formula to know |
|-----------------|
| $P(y^{<1>}, y^{<2>}, y^{<3>}\dots) = P(y^{<1>})\ P(y^{<2>} \lvert y^{<1>})\ P(y^{<3>} \lvert y^{<1>}, y^{<2>}) \dots$ |

### Loss function

At a certain time t, if the true word was $y^{<t>}$ and the new networks softmax predicted some $\hat{y}^{<t>}$, then this is the soft max loss function:

| Loss function                                                                                                        |
|----------------------------------------------------------------------------------------------------------------------|
| $\mathcal{L}^{<t>}(\hat{y}^{<t>},y^{<t>})=-\displaystyle \sum_i y_{i}^{<t>} \log{(\hat{y}_{i}^{<t>})}$ |

And then the overall loss is just the sum overall time steps of the loss associated with the individual predictions.

| Overall Loss function                                                                                                        |
|----------------------------------------------------------------------------------------------------------------------|
| $\mathcal{L}=\displaystyle \sum_t \mathcal{L}^{<t>}(\hat{y}^{<t>}, y^{<t>})$ |

And if you train this RNN on the last training set, what you'll be able to do is given any initial set of words, such as "cats average 15 hours of", it can predict what is the chance of the next word.

