# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 11:35:39 2021

@author: Charles Mbithi
"""
import numpy as np
import pandas as pd

labels = ["a","b","c"]
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10, 'b':20, 'c':30}
print(pd.Series(my_data))
print(pd.Series(my_data, labels))
print(pd.Series(arr, labels))
print(pd.Series(d))