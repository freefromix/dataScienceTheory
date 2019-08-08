"""This module manipulate images in numpy"""

import matplotlib.pyplot as plt
import imageio


def getImageNpArray(imagePath):
    """Get the image as a numpy array

    The image is of shape (Height, Width, Channels)

    Args:
        imagePath: A path to an image

    Returns:
        imageNp: A vector of shape (Height, Width, Channels)
    """

    imageNp = imageio.imread(imagePath)
    return imageNp


def drawImageWithNpArray(imageNp):
    """ Draw the image

    Args:
        imageNp: A np array of an image (Height, Width, Channels)

    Returns:
    """

    plt.imshow(imageNp)
    plt.show()


def image2vector(imageNp):
    """ Transform the np array (Height, Width, Channels) in a flat vector

    Args:
        imageNp: A np array of an image (Height, Width, Channels)

    Returns:
        v: A vector of shape (Height*Width*Channels, 1)
    """
    v = imageNp.reshape(imageNp.shape[0]*imageNp.shape[1]*imageNp.shape[2], 1)
    return v


def imageSet2vectorSet(imageSetNp):
    """ Transform the np set of images in a np set of vectors

    Args:
        imageSetNp: A np set of images (m_examples, Height, Width, Channels)

    Returns:
        v:  A np set of vectors (m_examples, Height x Width x Channels)
    """
    v = imageSetNp.reshape(
        imageSetNp.shape[0], imageSetNp.shape[1]*imageSetNp.shape[2]*imageSetNp.shape[3])
    return v


if __name__ == '__main__':
    imgPath = '../_static/face.png'
    imageNpShape = getImageNpArray(imgPath)
    drawImageWithNpArray(imageNpShape)
    vectorImage = image2vector(imageNpShape)
