# Transfer learning

Transfer learning: One of the most powerful ideas in deep learning is that sometimes you can take knowledge the neural network has learned from one task and apply that knowledge to a separate task.

So for example, maybe you could have the neural network learn to recognize objects like cats and then use that knowledge or use part of that knowledge to help you do a better job reading x-ray scans.

----

Let's say you've trained your neural network on image recognition. And you want to transfer what is learned to radiology diagnosis.

## Transfer learning: image recognition example

- You have: **Image recognition**
- You want: **Radiology diagnosis**

<img src="../img/screenshot_from_2019-01-23_16-43-06.png" width="400" />

__What you have to do is:__

|   |                                                         |
|---|---------------------------------------------------------|
| 1 | **Delete the last output layer of the neural network.** |
| 2 | **Delete also the weights feeding into that last output layer.** |
| 3 | **Create a new set of randomly initialized weights $(W^{[L]},b^{[L]})$ just for the last layer and have that now output radiology diagnosis.** |


You have a couple options of how you retrain neural network with radiology data:

1. You have a **small radiology dataset, you might want to just retrain the weights of the last layer** $(W^{[L]},b^{[L]})$ and keep the rest of the parameters fixed. Or maybe you can retrain the last two layers.
2. If you have** enough data, you could also retrain all the layers** of the neural network.
   1. If you retrain all the parameters in the neural network, then this initial phase of **training on Image recognition is sometimes called pre-training**, because **you're using image recognition data to pre-initialize or really pre-train the weights of the neural network**.
   2. And then **if you are updating all the weights afterwards**, **then training on the radiology data** sometimes **that's called fine tuning**.


| Term | Source |
|------|--------|
| Pre-training weights | Original source (Image recognition) |
| Fine tuning | Transfer learning source (radiology data) |

## Why does Transfer learning work in the above example
 
The reason Transfer learning work is that a lot of the low level features such as detecting edges, detecting curves, detecting positive objects. Learning from that, from a very large image recognition data set, might help your learning algorithm do better in radiology diagnosis. 

So having learned to recognize images, it might have learned enough about you know, just what parts of different images look like, that that knowledge about lines, dots, curves, and so on, maybe small parts of objects...

|                                                                                                          |
|----------------------------------------------------------------------------------------------------------|
| **Pre-training could help your radiology diagnosis network learn a bit faster or learn with less data**. | 

## Transfer learning: Speech recognition example

- You have: You've trained in speech recognition system to output your transcripts. 

- You want: You now want to build a "wake words" or a "trigger words" detection system (such as saying "Alexa" to wake up an Amazon Echo or "OK Google" to wake up a Google device or "hey Siri" to wake up an Apple device or saying "Ni hao baidu").


__What you have to do is:__

|   |                                                         |
|---|---------------------------------------------------------|
| 1 | **Delete the last output layer of the neural network.** |
| 2 | **Delete also the weights feeding into that last output layer.** |
| 3 | Create a new output layer. Sometimes another thing you could do is actually **create not just a single new output**, but actually **create several new layers to your neural network** to try to put the labels Y for your wake word detection problem. Then again, depending on how much data you have, you might just retrain the new layers of the network or maybe you could retrain even more layers of this neural network. |

## So, when does transfer learning make sense?

It makes sense when you have:

- **A lot of data for the problem you're transferring from.**
- **Relatively less data for the problem you're transferring to.**

For example:

__Radiology diagnosis__

|                                                  |                                                                                                             |
|--------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| You have 1 million example of image recognition. | **Lot of data to learn** a lot of **low level or useful features in the earlier layers** in neural network. |

|                                      |                                                                                                                 |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| You have only **a hundred examples** | **Use transfer learning**. For example, a lot of knowledge you learn from image recognition can be transferred. |

__ Speech recognition__

|                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| You have 10 000 hours of speech data (really a lot): You've trained the speech recognition system on it so you've learned a lot about what human voices sounds like. |

|                                                                                                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| That can be really helpful for building a good wake word detector, even though you have a relatively small dataset or at least a much smaller dataset for the wake word detection task. |

## Summary/Guideline

**When transfer learning makes sense:**

- **Task A and B have the same input x.**
- **You do have a lot more data for Task A than Task B.**
- **Low level features from A could be helpful for learning B.**



