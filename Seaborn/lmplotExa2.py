# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 18:17:04 2021

@author: Charles Mbithi
"""

import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
import numpy as np

x = np.random.randn(100)
y = np.random.randn(100)

data_plot = pd.DataFrame({'X-Axis': x, 'Y-Axis':y})

sb.lmplot(x='X-Axis', y='Y-Axis', data=data_plot)

print(plt.show())