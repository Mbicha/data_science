# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 15:17:30 2021

@author: Charles Mbithi
"""

import numpy as np
import pandas as pd

dict = pd.DataFrame({'Name':['Mbi','Thi', 'Nda', 'Nu','Poli', 'Nah'],
                     'Score':[90,97,91,90,90,97],
                     'Grade':['B','A','B','B','B','A']})

#unique and length of unique
uni = dict['Score'].unique()
unilen = dict['Score'].nunique()

#count
countval = dict['Grade'].value_counts()

#apply
apppd = dict['Score'].apply(lambda y: y-1)

#sort
sotdictbyscore = apppd.sort_values()

print('Unique Values\n',uni)
print('\nLength of Unique Values is\n',unilen)
print('\nValue Count\n',countval)
print('\nUsing Apply\n',apppd)
print('\nUsing Apply\n',sotdictbyscore)