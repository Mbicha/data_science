# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 12:48:52 2021

@author: Charles Mbithi
"""

import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,30,40,50]

plt.fill_between(x, y)

print(plt.show())