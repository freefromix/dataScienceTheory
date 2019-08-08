# List Tuple Set Dictionary

## Definitions

Unlike other programming languages, Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.

| Type       | A collection which is                 | Property                 | Example                                             |
| ---------- | ------------------------------------- | ------------------------ | --------------------------------------------------- |
| List       | **ordered and changeable**            | Allows duplicate members | [ 'abcd', 786 , 2.23, 'john', 70.2 ]                |
| Tuple      | **ordered and unchangeable**          | Allows duplicate members | ( 'abcd', 786 , 2.23, 'john', 70.2  )               |
| Set        | **unordered and unindexed**           | No duplicate members     | {1.0, "Hello", (1, 2, 3)}                           |
| Dictionary | **unordered, changeable and indexed** | No duplicate members     | {"brand": "Ford", "model": "Mustang", "year": 1964} |

- Lists declared with: ```[]```
- Tuple declared with: ```()```
- Dictionary declared with: ```{}```

## List

```python
mylist = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print mylist          # Prints complete list
# ['abcd', 786, 2.23, 'john', 70.2]
print mylist[0]       # Prints first element of the list
# abcd
print mylist[1:3]     # Prints elements starting from 2nd till 3rd 
# [786, 2.23]
print mylist[2:]      # Prints elements starting from 3rd element
# [2.23, 'john', 70.2]
print tinylist * 2  # Prints list two times
# [123, 'john', 123, 'john']
print mylist + tinylist # Prints concatenated lists
# ['abcd', 786, 2.23, 'john', 70.2, 123, 'john']

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
```

| Function  | Definition                                                                   |
| --------- | ---------------------------------------------------------------------------- |
| append()  | Adds an element at the end of the list                                       |
| clear()   | Removes all the elements from the list                                       |
| copy()    | Returns a copy of the list                                                   |
| count()   | Returns the number of elements with the specified value                      |
| extend()  | Add the elements of a list (or any iterable), to the end of the current list |
| index()   | Returns the index of the first element with the specified value              |
| insert()  | Adds an element at the specified position                                    |
| pop()     | Removes the element at the specified position                                |
| remove()  | Removes the item with the specified value                                    |
| reverse() | Reverses the order of the list                                               |
| sort()    | Sorts the list                                                               |

### Convert To list

```python
return list(dict.fromkeys(x))
```

## Tuple

Tuples can be thought of as read-only lists.

```python
mytuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print mytuple           # Prints complete list
# ('abcd', 786, 2.23, 'john', 70.2)
print mytuple[0]        # Prints first element of the list
# abcd
print mytuple[1:3]      # Prints elements starting from 2nd till 3rd 
# (786, 2.23)
print mytuple[2:]       # Prints elements starting from 3rd element
# (2.23, 'john', 70.2)
print tinytuple * 2   # Prints list two times
# (123, 'john', 123, 'john')
print mytuple + tinytuple # Prints concatenated lists
# ('abcd', 786, 2.23, 'john', 70.2, 123, 'john')

mytuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
mytuple = ( 'efgh', 123 , 4.56, 'jules', 140.1  ) # Ok because you redeclare the whole tuple
# tuple[2] = 1000    # Invalid syntax with tuple

```

## Dictionary

Dictionaries are written with curly brackets, and they have keys and values.

- Lists declared with: []
- Tuple declared with: ()
- Dictionary declared with: {}

```python
mydict = {}
mydict['one'] = "This is one"
mydict[2]     = "This is two"

tinydict = {'name': 'john', 'code':6734, 'dept': 'sales'}

# Change Values
tinydict['name'] = Jean

print mydict['one']         # Prints value for 'one' key
# This is one
print mydict[2]             # Prints value for 2 key
# This is two
print tinydict              # Prints complete dictionary
# {'dept': 'sales', 'code': 6734, 'name': 'john'}
print tinydict.keys()       # Prints all the keys
# ['dept', 'code', 'name']
print tinydict.values()     # Prints all the values
# ['sales', 6734, 'john']

len(tinydict) # Size of dictionary

for myKey in tinydict:
  print(x)
  
for myKey, myValue in tinydict.items():
  print(myKey, myValue)
  
if aKey in tinydict
  print("Yes, 'aKey' is one of the keys in the dictionary")

# Add an item
tinydict["Job")
```

## Iterators

```python
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
```

