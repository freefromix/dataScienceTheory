# A note on python numpy vectors (tips and tricks)

## Tricks

| Trick | Code |
|-------|------|
| Always use $n\times{m}$ matrices | ```np.random.randn(5,1)```      |
| Check dimensions with assert | ```assert(a.shape == (5,1))```  |
| Reshape simple n matrices into $n\times{m}$ matrices | ```a=a.reshape((5,1))``` |

## Bad behavior example

![](img/warning.png) If you take a row vector an add it to a vertical vector should be impossible! There should be a dimension mismatch or type error. But because of **broadcasting** you will get a matrix as a sum of the 2 vectors. It becomes a hard to find bug!!!!



## create your matrix forcing dimensions

![](img/warning.png) **CODE WITH ERROR:**

```python
a=np.random.randn(5)
print(a)
# [ 0.52674601 -2.00669464 -0.29534108  0.39718385 -0.49781891]
print(np.dot(a,a.T))
# 4.797089766861721
```

![](img/important.png) TRICK: use a=np.random.randn(5,1) instead:

### Row vector

```python
a=np.random.randn(5,1)
a.shape
# (5,1)
```
### Column vector

```python
a=np.random.randn(1,5)
a.shape
# (1,5)
```

**CODE WITH TRICK:**
```python
a=np.random.randn(5,1)
print(a)
# [[-0.72727558]
# [ 0.0863967 ]
# [-0.67375372]
# [-0.21493723]
# [-0.72344631]]

print(np.dot(a,a.T))
#[[ 0.52892976 -0.06283421  0.49000463  0.1563186   0.52614483]
# [-0.06283421  0.00746439 -0.0582101  -0.01856987 -0.06250337]
# [ 0.49000463 -0.0582101   0.45394407  0.14481476  0.48742464]
# [ 0.1563186  -0.01856987  0.14481476  0.04619801  0.15549554]
# [ 0.52614483 -0.06250337  0.48742464  0.15549554  0.52337456]]
```



