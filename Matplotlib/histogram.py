# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 08:57:26 2021

@author: Charles Mbithi
"""

from matplotlib import pyplot as plt
import numpy as np

a = np.array([22,82,5,91,73,74,81,86,55,41,67,33,20,17,27,66,77,89,99])
plt.hist(a,bins=[0,20,40,60,80,100],color='blue')

print(plt.show())