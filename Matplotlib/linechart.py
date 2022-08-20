# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 11:39:18 2021

@author: Charles Mbithi
"""

import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,30,40]

plt.plot(x,y, color='red')
plt.xlabel('Serial Number')
plt.ylabel('Distribution')
plt.title('First Line Chart')

print(plt.show())