# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 20:14:09 2021

@author: Charles Mbithi
"""

import pandas as pd
import numpy as np

exl = pd.read_excel('simple_exel.xlsx', sheet_name='Sheet1')
print(exl)