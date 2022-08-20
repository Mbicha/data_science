# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 11:11:43 2021

@author: Charles Mbithi
"""

import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd

df = pd.read_csv('E:\Tutorials\Python Tutorials\Resources\Diabetes.csv')
x = df['BMI']
y = df['DiabetesPedigreeFunction']

data_plot = pd.DataFrame({'BMI':x, 'DiabetesPedigreeFunction': y})

sb.lmplot(x='BMI', y='DiabetesPedigreeFunction', data=data_plot)

print(plt.show())