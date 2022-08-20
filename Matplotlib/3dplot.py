# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 17:54:14 2021

@author: Charles Mbithi
"""
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes(projection='3d')

z = np.linspace(0,1,100)
x = z * np.sin(30 * z)
y = z * np.cos(30 * z)

ax.plot3D(x,y,z,color='green')

print(plt.show())