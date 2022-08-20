# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 12:37:22 2021

@author: Charles Mbithi
"""
import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['V','W','X','Y'])
print(df)
"""
print(df[['W','X']])
#df['Z'] = df['V'] + df['W']
print("\nNew Column\n:", df)
print("Selecting Row using loc:\n", df.loc['D'])
print("Selecting Row using iloc:\n", df.iloc[3])
print("Selecting range Row and Colum using loc:\n", df.loc[['D','E'],['V','W','X']])
print("Select range:\n", df.loc[['A','C'],['X','Y']])

Conditions

print(df[df['W']>0][['V','X']])
print(df[df['X']<0][['V','W','X']])
print("\nMultiple Conditions\n")
print(df[(df['W']<0) & (df['X']>1)])
print(df.reset_index())


newind = "KE UG TZ SU ET".split()
df['States'] = newind
df.set_index('States')
print(df)

"""
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
df.index.names = ['Groups','Num']
#_g1 = df.loc['G1']
print(df)
print(df.loc['G2'].loc[3]['B'])
print(df.loc['G1'].loc[2]['A'])
#print('G1 Data Frame:\n', _g1)
