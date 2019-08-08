# Functions

## Modify multiple values in a function

### Tuple

```python
def f(x):
    y0 = x + 1
    y1 = x * 3
    y2 = y0 ** y3
    return (y0,y1,y2)
```

### Dictionary

```python
def h(x):
    result = [x + 1]
    result.append(x * 3)
    result.append(y0 ** y3)
    return result
```

### Class

```python
class ReturnValue(object):
    def __init__(self, y0, y1, y2):
        self.y0 = y0
        self.y1 = y1
        self.y2 = y2

def g(x):
    y0 = x + 1
    y1 = x * 3
    y2 = y0 ** y3
    return ReturnValue(y0, y1, y2)
```

```python
class ReturnValue(object):
    __slots__ = ["y0", "y1", "y2"]
    def __init__(self, y0, y1, y2):
        self.y0 = y0
        self.y1 = y1
        self.y2 = y2

def g(x):
    y0 = x + 1
    y1 = x * 3
    y2 = y0 ** y3
    return ReturnValue(y0, y1, y2)
```

### List

```python
def h(x):
    result = [x + 1]
    result.append(x * 3)
    result.append(y0 ** y3)
    return result
```
