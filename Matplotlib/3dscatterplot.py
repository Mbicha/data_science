# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 19:20:05 2021

@author: Charles Mbithi
"""

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

ax = plt.axes(projection='3d')

z = [1,2,3,4,5,6,7,8,9,10]
x = [2,3,4,6,7,9,10,13,8,5]
y = [3,5,9,12,5,17,19,21,7,27]

ax.scatter3D(x,y,z)

print(plt.show())