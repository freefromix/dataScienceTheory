# Numbers

```python
myint = 7

myfloat = 7.0; myfloat = float(7)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)

# Python 3 has only one integer type, int(). But it actually corresponds to Python 2’s long()

# Type int(x) to convert x to a plain integer.
# Type long(x) to convert x to a long integer.
# Type float(x) to convert x to a floating-point number.
```

## Squared cubed

```python
squared = 7 ** 2
# 49
cubed = 2 ** 3
# 8
```

## Random Number Functions

```python
import random

print ("random() : ", random.random())
# random() :  0.5038306594366878

# randomly select an odd number between 1-100 
print ("randrange(1,100, 2) : ", random.randrange(1, 100, 2))
# randrange(1,100, 2) :  61

# randomly select a number between 0-99 
print ("randrange(100) : ", random.randrange(100))
# randrange(100) :  47
```
