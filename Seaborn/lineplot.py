# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 10:34:53 2021

@author: Charles Mbithi
"""

import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd

df = pd.read_csv('E:\Tutorials\Python Tutorials\Resources\hrdata.csv')
x = df['Salary']
y = df['Sick Days remaining']

data_plot = pd.DataFrame({'Salary':x,'Sick Days':y})

sb.lineplot(x='Salary', y='Sick Days', data=data_plot)

print(plt.show())