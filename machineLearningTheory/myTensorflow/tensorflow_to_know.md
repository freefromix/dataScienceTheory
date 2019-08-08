# Tensorflow to know

<a href="../img/stanford_course_tensorflow_going_on_cs20si.zip">stanford_course_tensorflow_going_on_cs20si.zip</a>

## Basic program structure

```python
import tensorflow as tf

a = tf.constant([1, 2, 3, 4, 5, 6], shape=[3, 2], name="a")
b = tf.constant([7, 8, 9, 10, 11, 12], shape=[3, 2], name="b")

elementWiseProduct = tf.multiply(a, b, name="multiply")
writer = tf.summary.FileWriter('./graphs', tf.get_default_graph())

with tf.Session() as sess:
    print(sess.run(elementWiseProduct))

writer.close()
```

```bash
python3 ​my_program​.py
tensorboard --logdir "./graphs" --port 6006
```

## Tensor.eval() 

you cannot print the value of a tensor without running some code in a session.

If you have a Tensor t, calling t.eval() is equivalent to calling tf.get_default_session().run(t)

```python
t = tf.constant(42.0)
u = tf.constant(37.0)
tu = tf.mul(t, u)
ut = tf.mul(u, t)
with sess.as_default():
   tu.eval()  # runs one step
   ut.eval()  # runs one step
   sess.run([tu, ut])  # evaluates both tensors in a single step
```

equivalent with sess.as_default():

```python
t = tf.constant(42.0)
sess = tf.Session()
with sess.as_default():   # or `with sess:` to close on exit
    assert sess is tf.get_default_session()
    assert t.eval() == sess.run(t)
```

## To know

```python
# Creates a constant tensor. Values can not be modified.
tensor = tf.constant(-1.0, shape=[2, 3]) => [[-1. -1. -1.] [-1. -1. -1.]]

# Use it to reserve the memory for X (input) and Y (Output). Placeholder doesn’t require initial value.
# Placeholder simply allocates block of memory for future use. Later, we can use feed_dict to feed the
# data into placeholder.
x = tf.placeholder(tf.float32, [3, 1])

# Gets an existing variable with these parameters or create a new one.
tf.get_variable("W1", [4, 4, 3, 8], initializer = tf.contrib.layers.xavier_initializer(seed = 0))

# Tensorflow framework have overloaded *,+,-,/ etc. When you use Tensorflow variables the following lines  on the right are equivalent.
cost=tf.add(tf.add(w**2, tf.multiply(-10., w)), 25)
# same thing
cost=w**2-10*w+25

# Tensorflow matrix multiplication (math dot product)
tf.matmul(...,...)	
```
### Printing


1. **Comment these lines:** ```with  tf.Session() as sess:``` and ```sess.run(x)```
1. **Then add** ```tf.enable_eager_execution()``` **at the beginning of your code.** With eager execution enabled, TensorFlow functions execute operations immediately (as opposed to adding to a graph to be executed later in a tf.Session).
1. **You can now print with** ```tf.print```.



## Multiply matrices

### Math Dot Product tf.matmul

```python
import tensorflow as tf
import sys

tf.enable_eager_execution()

# 2-D tensor `a`
# [[1, 2, 3],
#  [4, 5, 6]]
a = tf.constant([1, 2, 3, 4, 5, 6], shape=[2, 3])
tf.print("\na:\n", a)

# 2-D tensor `b`
# [[ 7,  8],
#  [ 9, 10],
#  [11, 12]]
b = tf.constant([7, 8, 9, 10, 11, 12], shape=[3, 2])
tf.print("\nb:\n", b)

# Dot product of matrices will work
# We have [2, 3] * [3, 2]
mathDotProduct = tf.matmul(a, b)
tf.print("\nmathDotProduct:\n", mathDotProduct)

```

### Element wise multiplication tf.multiply or a*b

```python
# [[1 2]
# [3 4]
# [5 6]]
a = tf.constant([1, 2, 3, 4, 5, 6], shape=[3, 2])

# [[7 8]
# [9 10]
# [11 12]]
b = tf.constant([7, 8, 9, 10, 11, 12], shape=[3, 2])

# We have [3, 2] * [3, 2] so element wise is ok.
# or tf.multiply(a,b) = a*b
elementWiseProduct = a*b
# [[7 16]
# [27 40]
# [55 72]]
```

## placeholder

placeholder: Reserves the memory only. The values will be assigned later in this reserved memory later.

```python
x = tf.placeholder(tf.float32, [3, 1])
cost = x[0][0]*w**2 + x[1][0]*w + x[2][0]
values = np.array([[1.], [-20.], [100.]])
# ...
# ...
# Later
session.run(train, feed_dict={x:values})
```

## Code

```python
import numpy as np
import tensorflow as tf


# Create a Variable(<initial-value>, name=<optional-name>)
w = tf.Variable([0], dtype=tf.float32)

x = tf.placeholder(tf.float32, [3, 1])
cost = x[0][0]*w**2 + x[1][0]*w + x[2][0]

values = np.array([[1.], [-20.], [100.]])

# GradientDescentOptimizer: Optimizer that implements the gradient descent algorithm.
# GradientDescentOptimizer(learning_rate)
train = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

# Returns an Op that initializes global variables.
# TensorFlow Operations also known as Ops, are nodes that perform computations 
# on or with Tensor objects.
init = tf.global_variables_initializer()
# A `Session` object encapsulates the environment in which `Operation` objects
# are executed, and `Tensor` objects are evaluated.
session = tf.Session()
# This method runs one "step" of TensorFlow computation
session.run(init)
print(session.run(w))
# Output is: 0.0 because we have done nothing yet

for i in range(1000):
    session.run(train, feed_dict={x:values})
print(session.run(w))
```

## Code to explain

```python
def triplet_loss(y_true, y_pred, alpha = 0.2):
    """
    Implementation of the triplet loss as defined by formula (3)
    
    Arguments:
    y_true -- true labels, required when you define a loss in Keras, you don't need it in this function.
    y_pred -- python list containing three objects:
            anchor -- the encodings for the anchor images, of shape (None, 128)
            positive -- the encodings for the positive images, of shape (None, 128)
            negative -- the encodings for the negative images, of shape (None, 128)
    
    Returns:
    loss -- real number, value of the loss
    """
    
    anchor, positive, negative = y_pred[0], y_pred[1], y_pred[2]
    ### START CODE HERE ### (≈ 4 lines)
    # Step 1: Compute the (encoding) distance between the anchor and the positive, you will need to sum over axis=-1
    pos_dist = tf.reduce_sum(tf.square(tf.subtract(anchor, positive)), axis=-1)
    # Step 2: Compute the (encoding) distance between the anchor and the negative, you will need to sum over axis=-1
    neg_dist = tf.reduce_sum(tf.square(tf.subtract(anchor, negative)), axis=-1)
    # Step 3: subtract the two previous distances and add alpha.
    basic_loss = tf.add(tf.subtract(pos_dist, neg_dist), alpha)
    # Step 4: Take the maximum of basic_loss and 0.0. Sum over the training examples. 
    loss = tf.reduce_sum(tf.maximum(basic_loss, 0)) # not tf.reduce_max(basic_loss, axis=0)
    ### END CODE HERE ###
    
    return loss

# -------------------------------
with tf.Session() as test:
    tf.set_random_seed(1)
    y_true = (None, None, None)
    y_pred = (tf.random_normal([3, 128], mean=6, stddev=0.1, seed = 1),
              tf.random_normal([3, 128], mean=1, stddev=1, seed = 1),
              tf.random_normal([3, 128], mean=3, stddev=4, seed = 1))
    loss = triplet_loss(y_true, y_pred)
    
    print("loss = " + str(loss.eval()))

```

