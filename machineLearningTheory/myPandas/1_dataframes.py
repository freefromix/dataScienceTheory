import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']

my_data = [10, 20, 30]
arr = np.array(my_data)

d = {'a': 10, 'b': 20, 'c': 30}

ser = pd.Series(data=my_data, index=labels)
# print(ser, "\n")
# print(ser['b'], "\n")

ser1 = pd.Series([1, 2, 5, 6], ['USA', 'Germany', 'Different', 'Japan'])
ser2 = pd.Series([1, 2, 3, 6], ['USA', 'Germany', 'Italy', 'Japan'])

sertotal = ser1 + ser2
# Cannot add when labels doesn't match, so it writes: NaN
# sertotal is float even if ser1 and ser2 are int
print(sertotal[1])
