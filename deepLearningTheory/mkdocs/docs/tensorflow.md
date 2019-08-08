# Tensorflow

## Dataset

class Dataset: Represents a potentially large set of elements.

A Dataset can be used to represent an input pipeline as a collection of elements (nested structures of tensors) and a "logical plan" of transformations that act on those elements.

### Dataset: from from_tensors vs from_tensor_slices

- from_tensors combines the input and returns a dataset with a single element:

```python
t = tf.constant([[1, 2], [3, 4]])
ds = tf.data.Dataset.from_tensors(t)   # [[1, 2], [3, 4]]
```

- from_tensor_slices creates a dataset with a separate element for each row of the input tensor:

```python
t = tf.constant([[1, 2], [3, 4]])
ds = tf.data.Dataset.from_tensor_slices(t)   # [1, 2], [3, 4]
```
