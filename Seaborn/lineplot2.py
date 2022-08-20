# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 10:57:29 2021

@author: Charles Mbithi
"""

import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd

x = [1, 2, 4, 8, 16, 32, 64, 128, 256]
y =  [175, 170, 205, 120, 220, 130, 105, 145, 190]

data_plot = pd.DataFrame({'X Label':x, 'Y Label':y})

sb.lineplot(x='X Label', y='Y Label', data=data_plot)

print(plt.show())