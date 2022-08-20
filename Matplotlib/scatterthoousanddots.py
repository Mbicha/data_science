# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 12:25:26 2021

@author: Charles Mbithi
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.random.random(1000)
y = np.linspace(1,100,1000)

plt.scatter(x, y, color='green')

print(plt.show())