# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 19:12:22 2021

@author: Charles Mbithi
"""

import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd

df = sb.load_dataset('tips')

sb.stripplot(x='day', y='total_bill', data=df)

print(df)