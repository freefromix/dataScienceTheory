import matplotlib
print(matplotlib.get_backend())

import matplotlib.pyplot as plt
import numpy as np
from pylab import *   

x = np.linspace(0, 5, 11)
y = x ** 2

plt.plot(x, y)

plt.xlabel('X label')
plt.ylabel('Y label')
plt.title('This is my plot title')

plt.subplot(1, 2, 1)
plt.plot(x, y, 'r')
plt.title("This is 1")

plt.subplot(1, 2, 2)
plt.plot(y, x, 'b')
plt.title("This is 2")

# plt.show()

#######################################
# Method with add_axes
# (Method with subplots is in 2_matplotlib_part2.py)
#######################################

fig = plt.figure()

# add_axes(left bottom width heigth)
 
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# 20% from the left
# 50% from the bottom
# 40% width
# 30% heigth
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

axes.plot(x, y)
axes2.plot(y, x)

axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Fig title bigger')

axes2.set_xlabel('Y Label 2')
axes2.set_ylabel('X Label 2')
axes2.set_title('Fig title smaller')




