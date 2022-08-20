# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 09:46:21 2021

@author: Charles Mbithi
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('E:\Tutorials\Python Tutorials\Resources/Cricket.csv')

india = df['score_india']
pk = df['score_pk']
legend = ['India', 'Parkistan']
plt.hist([india, pk], color=['green','blue'])

print(plt.show())