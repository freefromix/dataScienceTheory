import matplotlib
print(matplotlib.get_backend())

import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 5, 11)
y = x ** 2

#######################################
# Method with subplots
# (Method with add_axes is in 1_matplotlib_part1.py)
#######################################

# Warning: Be careful with the 's' at the end of subplots
fig, axes = plt.subplots(nrows=1, ncols=2)



# for current_ax in axes:
    # current_ax is a <class 'matplotlib.axes._subplots.AxesSubplot'>
    # Same object as when we created fig.add_axes in the previous lesson
#    print(type(current_ax))
#    current_ax.plot(x, y)

# Or you could do
axes[0].plot(x, y)
axes[0].set_title("First plot")

axes[1].plot(y, x)
axes[1].set_title("Second plot")

# Automatically adjust subplot parameters to give specified padding.
# Adjust padding between each plot
plt.tight_layout()


#######################################
# Figure size aspect ratio and DPI
# (Method with add_axes is in 1_matplotlib_part1.py)
#######################################

# figsize=(width in inches, height in inches)
# dpi: Dots per inch
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8,2), dpi=100)

axes[0].plot(x,y)
axes[0].set_title('Title 1')
axes[0].set_ylabel('Y')
axes[0].set_xlabel('X')

axes[1].plot(y,x)
axes[1].set_title('Title 2')
axes[1].set_ylabel('Y')
axes[1].set_xlabel('X')

plt.tight_layout()

# Save to file
fig.savefig('my_picture.png', dpi=200)
fig.savefig('my_picture.jpg', dpi=200)


#######################################
# Legends
#######################################

fig = plt.figure()

ax = fig.add_axes([0,0,1,1])
ax.plot(x, x**2, label='X squared', color='purple', linewidth=5, alpha=0.5, linestyle='-.')
ax.plot(x, x**3, label='X cubed', color='red', marker='o', markersize=10, markerfacecolor='yellow', markeredgecolor='green')
  
# ax.legend writes the label as legend
# All kinds of locations goes from 0 to 10
ax.legend(loc=0)

# Using coordinates x, y tuple
ax.legend(loc=(0.1,0.1))

ax.set_xlim([0,10])
ax.set_ylim([0,20])
