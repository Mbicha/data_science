# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 21:40:04 2021

@author: Charles Mbithi
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('E:\Tutorials\Python Tutorials\Resources\hrdata.csv')
#x = df['Sick Days remaining']
#y = df['Salary']
#plt.scatter(x, y, color='g')

names = df['Name']
salary = df['Salary']

plt.xlabel('Salary', color='blue')
plt.ylabel('Employee Name', color='blue')
plt.title('Employee Data', color='g')
plt.bar(names, salary, color='gold')

print(plt.show())