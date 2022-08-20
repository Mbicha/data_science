# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 09:35:01 2021

@author: Charles Mbithi
"""

import matplotlib.pyplot as plt
import numpy as np

data = np.random.randint(1,100,100)
plt.hist(data, bins=10)
print(plt.show())