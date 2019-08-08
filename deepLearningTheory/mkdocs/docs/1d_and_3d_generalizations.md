# 1D and 3D Generalizations

## Convolution 2D

![](img/screenshot_from_2019-03-01_13-06-26.png)

Output size:

| First layer |    |
|-------------|----|
| Convolution 2D | $(14 \times 14)*(5 \times 3)=10\times{10}$ |

----

Another example:

| First layer |    |
|-------------|----|
| Convolution 2D with 16 filters | $(14 \times 14 \times 3)*(5 \times 5 \times 3)=10 \times 10 \times 16$ |

| Second layer |    |
|--------------|----|
| Convolution | $(10 \times 10 \times 16)*(5 \times 5 \times 16)= 6 \times 6 \times 32$ |

## Convolutions 1D

Example with electrocardiography signal (heartbeat signal).

![](img/screenshot_from_2019-03-01_17-22-15.png)

If you want to use Electrocardiography signals to make medical diagnoses then you would have 1D data. Electrocardiography signals are a time series.

So rather than a 2D 14x14 shape input, maybe **you just have a 1D 14 dimension input**.

![](img/screenshot_from_2019-03-01_13-07-44.png)

So rather than the 5x5 filter, **you just have a 5 
dimension filter**.

So here, you will convolve your 14 dimension Input with a 5 dimension filter.

What a 1D filter allows you to do:

- Is take your 5 dimensional filter 
- and similarly **apply that in lots of different positions throughout this 1D signal**. 

Output size:

| First layer |    |
|-------------|----|
| Convolution 1D | $14*5=10$ |
| Convolution 1D with 16 filters | $14*5=10 \times 16$ |

| Second layer |    |
|--------------|----|
| Convolution with 32 filters | $(10 \times 16)*(5 \times 16) =6 \times 32$ |

So all of these ideas apply also to 1D data, where you can have the same feature detector (filter) apply to a variety of positions along these time series. 

For example, to detect the different heartbeats in an EKG signal.

For 1D data applications, you actually use a **recurrent neural network** (specially designed for sequece data), but some people can also try using ConvNets in these problems.

## Convolutions 3D data

Computerized tomography (CT) scan combines a series of X-ray images.

Here you can look at different slices of the human torso to see how they look and so this data is fundamentally three dimensional:

<img src="../img/screenshot_from_2019-03-01_20-42-37.png" width="150" />
<img src="../img/screenshot_from_2019-03-01_20-42-58.png" width="150" />
<img src="../img/screenshot_from_2019-03-01_20-43-22.png" width="155" />
<img src="../img/screenshot_from_2019-03-01_20-44-15.png" width="160" /> etc...

3D data: So your data has some Width, Heigth and Depth:

<img src="../img/cube.png" width="100" />

![](img/screenshot_from_2019-03-01_21-00-01.png)

What the filters do is really detect features across your 3D data.

| Output |
|--------|
| $(10 \times 10 \times 10 \times n_C)*(5 \times 5 \times 5 \times n_C)=6 \times 6 \times 6 \times numberOfFilters$ |


Scans, medical scans as one example of 3D volumes.

But another example of data, you could treat as a 3D volume would be movie data, where the different slices could be different slices in time through a movie. And you could use this to detect motion or people taking actions in movies. 