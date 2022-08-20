# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 23:39:49 2021

@author: Charles Mbithi
"""

import numpy as np
import pandas as pd

dict = {'Classes':['A','A','B','B','C','C','C'],
        'Students':['Charles', 'Ndanu','Mbithi','Polinah','Reginah','Ken','Kalunda'],
       'Score':[87, 89, 93, 71, 67, 92, 97]}

df = pd.DataFrame(dict)
dfstd = df.groupby('Classes').describe().transpose()['B']

print(df)
print(dfstd)