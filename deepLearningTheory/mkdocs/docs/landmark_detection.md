# Landmark detection

landmark = repère, point de repère

Let's say you're building a face recognition application and for some reason, you want the algorithm to tell you where are the corners of someone's eye.

<img src="../img/screenshot_from_2019-02-17_11-50-31.png" width="400" />

So you can just add to your face recognition NN 4 more outputs to just tell you the coordinates of the corners of the person's eye:

|                    |
|--------------------|
| $l_{1}x$, $l_{1}y$ |
| $l_{2}x$, $l_{2}y$ |
| $l_{3}x$, $l_{3}y$ |
| $l_{4}x$, $l_{4}y$ |

But what if you don't want just those four points but more points?

- Points along the eye
- Points along the mouth (to tell if the person is smiling or frowning)
- Points along the edges of the nose

For the sake of argument, let's say 64 face points:

<img src="../img/screenshot_from_2019-02-17_11-52-02.png" width="300" />

The output is: output vector_size = 64x +64y + faceOrNot = 64 +64 + 1 = 69

So, this is a basic building block for recognizing emotions from faces.

AR augmented reality filters like the Snapchat photos can draw a crown on the face and have other special effects by using landmarks detection.

<img src="../img/snapchat-flower-crown-filter-720x720.jpg" width="200" />
## Pose detection

<img src="../img/screenshot_from_2019-02-17_12-03-04.png" width="200" />

If you are interested in people pose detection, you could also define a few key positions like:
- the midpoint of the chest
- the left shoulder
- left elbow
- the wrist
- etc.

- And just have a neural network to annotate key positions in the person's pose.
- And by having a neural network output, all of those points I'm annotating, you could also have the neural network output the pose of the person.

And of course, to do that you also need to specify on these key landmarks like maybe l1x and l1y is the midpoint of the chest down to maybe l32x, l32y, if you use 32 coordinates to specify the pose of the person

**The identity of landmark one must be consistent across different images** like maybe landmark one is always this corner of the eye, landmark two is always this corner of the eye, landmark three, landmark four, and so on. So, the labels have to be consistent across different images.

But if you can hire labelers or label yourself a big enough data set to do this, then a neural network can output all of these landmarks which is going to used to carry out other interesting effect such as with the pose of the person, maybe try to recognize someone's emotion from a picture, and so on.
