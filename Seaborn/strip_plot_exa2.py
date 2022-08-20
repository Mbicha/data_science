# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 19:15:14 2021

@author: Charles Mbithi
"""

import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd

df = pd.read_csv('E:\Tutorials\Python Tutorials\Resources\Loan.csv')

#sb.stripplot(x=df['Property_Area'], y=df['LoanAmount'], data=df)

#swarmplot ro prevent data overlap
sb.swarmplot(x=df['Property_Area'], y=df['LoanAmount'], data=df)

print(df.columns)