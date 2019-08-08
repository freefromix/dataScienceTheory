#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 17:51:36 2019

@author: julien
"""

import pandas as pd

from bokeh.palettes import magma
from bokeh.plotting import figure, show, output_file
output_file('temp.html')

# ###############################
#
#   Doesn't work
print("Doesn't work")
#
# ###############################


df = pd.read_excel('tabn322.10.xls', header = 1)
print(df.head())

print('###############################')

# Delete rows 0, 1, 41, 42
df = df.drop([0, 1, 41, 42])

# Delete rows with NaN
df = df.drop([7, 13, 19, 25, 31, 37])

df['Field of study'] = df['Field of study'].str.replace('.','')
df['Field of study'] = df['Field of study'].str.replace('\n','')
df.set_index('Field of study', inplace=True)

timeIsX = df.transpose()


#the number of columns is the number of lines that we will make
numlines = len(timeIsX.columns)

#import color pallet
mypalette = magma(numlines)

p = figure(title="Title", width = 1000, height = 450)
p.xaxis.axis_label = 'Date'
p.yaxis.axis_label = 'Values'

xs=[timeIsX.index.values]*numlines
ys=[timeIsX[name].values for name in timeIsX]

print(numlines)
print(len(xs))
print(len(ys))
print(len(mypalette))
# print(timeIsX.head())

p.multi_line(xs, ys, line_color=mypalette, line_width=4)

show(p)