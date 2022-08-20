# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 14:57:11 2021

@author: Charles Mbithi
"""

import matplotlib.pyplot as plt

subjects = ['M', 'E', 'K', 'P', 'C', 'B']
marksformbithi = [97, 71, 63, 90, 94, 84]
marksforcharles = [92, 79, 55, 81, 96, 97]

plt.bar(subjects,marksformbithi, label = 'Mbithi')
plt.bar(subjects,marksforcharles, label = 'Charles', color='a')
#plt.barh(subjects, marks, color='blue')
plt.legend()
plt.xlabel('Subjects', color='green')
plt.ylabel('Marks', color='green')
plt.title('Students Bar Graph')

print(plt.show())