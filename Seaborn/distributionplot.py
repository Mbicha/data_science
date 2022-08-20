# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 19:47:15 2021

@author: Charles Mbithi
"""

import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
import numpy as np

data = np.random.randn(50)
sb.distplot(data, color = 'green')

#df = pd.read_csv('E:\Tutorials\Python Tutorials\Resources\hrdata.csv')

#hrdat = df['Salary']

#sb.distplot(hrdat)

print(plt.show())