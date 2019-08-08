# Vectorization

<img src="../img/vectorization.png" width="300" />

On a CPU your code actually runs over 300 times faster!!!!

They're sometimes called SIMD instructions. This stands for a single instruction multiple data. But what this basically means is that, if you use built-in functions such as this np.function or other functions that don't require you explicitly implementing a for loop. 

It enables Phyton Pi to take much better advantage of parallelism to do your computations much faster. And this is true both computations on CPUs and computations on GPUs. 



```python
# Dot product of two arrays.

# Calculate the exponential of all elements in the input array.
u=np.exp(v)

# Natural logarithm, element-wise.
u=np.log(v)

# Random values in a given shape.
# Create an array of the given shape and populate it with random samples 
# from a uniform distribution over [0, 1)
a=np.random.rand(100)
b=np.random.rand(100)

# ndarray.shape: Tuple of array dimensions.
print(a.shape)
# (100,)

# Element-wise maximum of array elements.
np.maximum(a,b)

# Element-wise square of all elements.
a**2

# Element-wise inverse of all elements.
1/a

# Sum of array elements over a given axis.
np.sum(a)

# Sum the values in a matrix A vertically
a.sum(axis = 0)

# Transpose array
# ndarray.T: Same as self.transpose(), except that self is returned if self.ndim < 2.
print(a.T)

# x = np.array([[1.,2.],[3.,4.]])
# >>> x
# array([[ 1.,  2.],
#       [ 3.,  4.]])
# >>> x.T
# array([[ 1.,  3.],
#       [ 2.,  4.]])
```

```python
import time
import numpy as np

# numpy.zeros(shape, dtype=float, order='C') --> Return a new array of given shape and type, filled with zeros.
a=np.random.rand(1000000)
b=np.random.rand(1000000)

tic=time.time()
# numpy.dot(a, b, out=None) --> Dot product of two arrays
c=np.dot(a,b)
toc=time.time()

print("Vectorized version, time used: "+str(1000*(toc-tic)))

```

