# modules

Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application.

To create a module just save the code you want in a file with the file extension mymodule.py:

```python
import mymodule

mymodule.greeting("Jonathan")
```

## Variables in a module

Save this code in the file mymodule.py

```python
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
```

In another file:

```python
import mymodule
from anothermodule import theperson

a = mymodule.person1["age"]
print(a)

print (theperson["age"])
```

## Naming a module

Naming a Module

```python
import mymodule as mym

```

```python
from mymodule import person1

print (person1["age"])
```
