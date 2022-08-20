# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 10:52:41 2021

@author: Charles Mbithi
"""

import numpy as np
import pandas as pd

df1 = pd.DataFrame({'Form':['F1','F2','F3'],
                    'Name':['Mbithi','Charles','Rhonda'],
                    'Score':[1178, 985, 1172]},
                   index=[0,1,2])

df2 = pd.DataFrame({'Form':['F3','F2','F3'],
                    'Name':['Ndanu','Polina','Sammi'],
                    'Score':[1154, 1098, 874]},
                   index=[3,4,5])

df3 = pd.DataFrame({'Form':['F1','F2','F3'],
                    'Name':['Kalundi','Rehina','Rhoda'],
                    'Score':[1012, 1156, 941]},
                   index=[6,7,7])

pdconca = pd.concat([df1,df2,df3])
print(pdconca)

"""
Merging
"""
left = pd.DataFrame({'Key':['F1','F2','F3'],
                    'Name':['Mbithi','Charles','Rhonda'],
                    'Score':[1178, 985, 1172]},
                   index=[0,1,2])

right = pd.DataFrame({'Key':['F1','F2','F3'],
                    'Name':['Ndanu','Polina','Sammi'],
                    'Score':[1154, 1098, 874]},
                   index=[3,4,5])
pdmerge = pd.merge(left,right,on='Key')
print(pdmerge)