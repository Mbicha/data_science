# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 12:03:40 2021

@author: Charles Mbithi
"""

import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,30,40]

plt.scatter(x, y, color='green')
plt.xlabel('Serial Number', color='blue')
plt.ylabel('Distribution', color='blue')
plt.title('First Scatter Chart')

print(plt.show())