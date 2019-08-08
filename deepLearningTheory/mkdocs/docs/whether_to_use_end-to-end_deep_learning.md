# Whether to use end-to-end deep learning

## Pros and cons of end-to-end deep learning

Pros:

- Let the data speak.
- Less hand-designing of components needed.

Cons:

- May need large amount of data.
- Exclude potentially useful hand-designed components.

----

**Let the data speak**: If you ave enough data, whatever the function x -> y that you try to map, hopefully the big NN will figure it out. And by having a pure machine learning approach, your neural network learning input from X to Y may **be more able to capture whatever statistics are in the data, rather than being forced to reflect human preconceptions**.
  - Speech recognition example: Earlier speech systems had this notion of a phoneme (basic unit of sound like C, A, and T for the word cat). I think that phonemes are an artifact created by human linguists. I actually think that phonemes are a fantasy of linguists. And if you let your learning algorithm learn whatever representation it wants to learn rather than forcing it to use phonemes then its overall performance might end up being better.

**Less hand designing of components needed**: It simplifies your design work flow, that you just don't need to spend a lot of time hand designing features, hand designing these intermediate representations.

----

**May need large amount of data**.


**Exclude potentially useful hand-designed components**: If you don't have a lot of data, then your learning algorithm doesn't have that much insight it can gain from your data if your training set is small. And so hand designing a component can really be a way for you to inject manual knowledge into the algorithm, and that's not always a bad thing. And hand-designed components could be very helpful if well designed. They could also be harmful if it really limits your performance, such as if you force an algorithm to think in phonemes when maybe it could have discovered a better representation by itself.

## Applying end-to-end deep learning

Key question : Do you have sufficient data to learn a function of the complexity needed to map x to y?

Example Autonomous vehicle:

<img src="../img/screenshot_from_2019-01-26_11-22-39.png" width="400" />

What this example illustrates is that you want:

- Use Deep Learning to learn individual components.
- Carefuly choose X->Y depending on what task you can get data for.

<img src="../img/screenshot_from_2019-01-26_11-35-53.png" width="400" />

And in contrast, it is exciting to talk about a pure end-to-end deep learning approach where you input the image and directly output a steering.

But given data availability and the types of things we can learn with neural networks today, **end-to-end learning**:

- **This is actually not the most promising approach.**
- **Or this is not an approach that I think teams have gotten to work best.**



