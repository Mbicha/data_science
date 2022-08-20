# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 19:16:10 2021

@author: Charles Mbithi
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('E:\Tutorials\Python Tutorials\Resources\cars.csv')

plt.boxplot(df['CO2'])
print(plt.show())
print(df.columns)