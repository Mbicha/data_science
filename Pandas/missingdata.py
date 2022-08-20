# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 19:17:01 2021

@author: Charles Mbithi
"""

import numpy as np
import pandas as pd

d = {'A':[1,2,np.nan],'B':[5, np.nan, np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)
print(df)
print("Drop rows with nan:\n",df.dropna())
print("Drop columns with nan:\n",df.dropna(axis=1))
print(df.dropna(thresh=2))