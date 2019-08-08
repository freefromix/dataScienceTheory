# python objects

```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

# The self parameter is a reference to the class itself, and is used to access variables that belongs to the class.

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
p1.myfunc()
p1.age = 40
del p1.age

# Delete the p1 object:
del p1
```
