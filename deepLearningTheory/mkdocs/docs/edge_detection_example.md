# Edge Detection Example

<img src="../img/screenshot_from_2019-01-29_14-44-39.png" width="400" />
## How to detect edges

6x6x1 grayscale image, only one channel because it is grayscale and not rgb channels.

In order to detect edges or lets say vertical edges in his image, what you can do is construct a 3x3 filter.

|                 |   |                                       |
|-----------------|---|---------------------------------------|
| ![](img/warning.png) | **filter is sometimes called kernel** |

| Convolution |    |
|-------------|----|
| In math | "*" asterisk means convolution. |
| In python | conv_forward |
| In math | tf.nn.conv2d |

<img src="../img/screenshot_from_2019-01-29_18-58-58.png" width="400" />

## Convolution calculus

$Square_{1,1}=3\times{1}+1\times{1}+2\times{1}+0\times{0}+5\times{0}+7\times{0}+1\times{-1}+8\times{-1}+2\times{-1}=-5$

<img src="../img/screenshot_from_2019-01-29_19-00-01.png" width="400" />

$Square_{2,1}=0\times{1}+5\times{1}+7\times{1}+1\times{0}+8\times{0}+2\times{0}+2\times{-1}+9\times{-1}+5\times{-1}=-4$

$\vdots$

<img src="../img/screenshot_from_2019-01-29_19-04-48.png" width="400" />

$Square_{1,2}=1\times{1}+2\times{1}+0\times{1}+5\times{0}+7\times{0}+1\times{0}+8\times{-1}+2\times{-1}+3\times{-1}=-1$

$\vdots$

<img src="../img/screenshot_from_2019-01-29_19-08-37.png" width="400" />

## Why convolution operation detect edges

Example with vertical edges detection:

<img src="../img/screenshot_from_2019-01-29_21-30-31.png" width="400" />

$Original\_image * filter = edge\_image$

Result of the convolution: The bright region in the middle is just the output images way of saying that it looks like there is a strong vertical edge right down the middle of the image.

Maybe one intuition to take away from vertical edge detection is that a vertical edge is a 3 by 3 region since we are using a 3 by 3 filter where there are bright pixels on the left, you do not care that much what is in the middle and dark pixels on the right.
