# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 18:53:38 2021

@author: Charles Mbithi
"""

import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd

df = pd.read_csv('E:\Tutorials\Python Tutorials\Resources\Diabetes.csv')

sb.jointplot(x=df['BMI'], y=df['DiabetesPedigreeFunction'], kind='scatter')