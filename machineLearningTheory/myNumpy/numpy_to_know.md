# Numpy to know

----

Python

  - [Python and Vectorization](./python_and_vectorization.md)
  - [Python and Broadcasting](./python_and_broadcasting.md)
  - [note on python numpy vectors (tips and tricks)](./note_on_python_numpy_vectors_tips_and_tricks.md)

## Declare Arrays


```python
# Creates an numpy matrix.
x = np.array([[1.,2.],[3.,4.]])

# Creates a (2,2) numpy matrix full of zeros.
x = np.zeros((2,2))

# Creates a (2,2) numpy matrix full of ones.
x = np.ones((2,2), dtype=int)
```

## Arrays functions

<img src="../img/dotproduct_matrices.jpg" width="400" />


| Code                             | Function                                                                                   |
|----------------------------------|--------------------------------------------------------------------------------------------|
| ```np.sum(b, axis=1)``` | Sum of array elements over a given axis. |
| ```c=np.dot(a,b)```                    | Dot product of two arrays. |
| ```u=np.exp(v)```                      | Calculate the exponential of all elements in the input array |
| ```u=np.log(v)```                      | Natural logarithm, element-wise. |
| ```a=np.random.rand(100)```            | Random samples from a uniform distribution over [0, 1) |
| ```ndarray.shape```                    | Tuple of array dimensions. ex:(100,4) |
| ```np.maximum(a,b)```                  | Element-wise maximum of array elements. |
| ```a**2```                           | Element-wise square of all elements. |
| ```np.sum(a)```                        | Sum of array elements over a given axis. |
| ```a.sum(axis = 0)```                  | Sum the values in a matrix A vertically |
| ```a.T```                              | Transpose array. Same as self.transpose()  except that self is returned if self.ndim < 2. |

```python
def sigmoid(x):
    """
    Compute the sigmoid of x

    Arguments:
    x -- A scalar or numpy array of any size

    Return:
    s -- sigmoid(x)
    """
    
    ### START CODE HERE ### (≈ 1 line of code)
    s = 1/(1+np.exp(-x))
    ### END CODE HERE ###
    
    return s
```

## Create a numpy matrix

- np.ones()

```python
s = (2,2)
np.ones(s)
array([[ 1.,  1.],
       [ 1.,  1.]])
```

## Create a numpy matrix full of zero

- np.zeros()

```python
s = (2,2)
np.zeros(s, dtype=int)
array([[ 0,  0],
       [ 0,  0]])
```

