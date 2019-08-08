# Addressing data mismatch

For a speech recognition system:

|                                                                                                        |
|--------------------------------------------------------------------------------------------------------|
| **Carry out manual error analysis** to try to understand difference between training and dev/test sets |

* Noisy, car noise
* Mis-recognizing street numbers


|                                                       |
|-------------------------------------------------------|
| **Make training data more similar to dev/test sets**  |

* If you find that car noise in the background is a major source of error, one thing you could do is simulate noisy in-car data.
* If you're having a hard time recognizing street numbers, maybe you can go and deliberately try to get more data of people speaking out numbers and add that to your training set.


## Artificial data synthesis

So, let's say that you've recorded a large amount of clean audio without this car background noise. 

<img src="../img/screenshot_from_2019-01-23_11-58-10.png" width="400" />

Let's say you have:

|                                              |              |
|----------------------------------------------|--------------|
| The quick brown fox jumps over the lazy dog. | 10 000 hours |
| Car noise | 1 hour |

You could take this 1 hour of car noise and multiply it 10 000 times and then add it to 10 000 hours of "Quick brown fox jumps ...".

|                 |                                                                                                                                                                                                            |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](img/warning.png) | You could take this 1 hour of car noise and multiply it 10 000 times and then add it to 10 000 hours of "Quick brown fox jumps ...". What will happen is that **you will overfit to 1 hour of car noise.** |

Try to find multiple car noise examples. You must find a solution to have more diversity to you car noise.

## You want to detect cars

So you create a dataset of pictures coming from a video game. Your images are perfect but the video game has only 20 kind of cars.

|                 |                                                                                                                                                                                    |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](img/warning.png) | Again you will overfit to this kind of cars. The world has thousands of car types. Your system might be stuck to the 20 kind of cars he knows and not recognize other car designs. |

Find a way to have a lot of different car images. 

## Conclusion: What you have to do

- Do error analysis. Look at the training set. Look at the dev set to try to try to gain insight into how these two distributions of data might differ.
- Then see if you can find some ways to get more training data that looks a bit more like your dev set.
  - One of the ways we talked about is artificial data synthesis. Artificial data synthesis does work. In speech recognition, I've seen artificial data synthesis significantly boost the performance of what were already very good speech recognition system. But, if you're using artificial data synthesis, just be cautious and bear in mind whether or not you might be accidentally simulating data only from a tiny subset of the space of all possible examples.

