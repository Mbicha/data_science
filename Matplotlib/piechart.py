# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 12:54:34 2021

@author: Charles Mbithi
"""

import matplotlib.pyplot as plt

cars = ['BMW', 'Audi', 'CRV', 'Pajero','Prado']
data = [20,37,48, 77, 101]

plt.pie(data, labels=cars)

print(plt.show())