# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 21:05:23 2021

@author: Charles Mbithi
"""

import pandas as pd

sal = pd.read_csv('Salaries.csv')
salhead = sal.info()
avbasepay = sal['BasePay'].mean()
overtimepay = sal['OvertimePay'].max()
jobtitleforjoseph = sal[(sal['EmployeeName']=='JOSEPH DRISCOLL')]['JobTitle']
totalamounjosephearns = sal[(sal['EmployeeName']=='JOSEPH DRISCOLL')]['TotalPayBenefits']

highestpaid = sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName']
lowestpaid = sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]['EmployeeName']
meanbtw20112014 = sal.groupby('Year').mean()['BasePay']
uniquejobtt = sal['JobTitle'].nunique()
topfivecommonjobs = sal['JobTitle'].value_counts().head(6)

def chief_string(title):
    if 'chief' in title.lower().split():
        return True
    else:
        return False
    
numofjobswithchief = sum(sal['JobTitle'].apply(lambda x:chief_string(x)))

print(salhead)
print('\nAverage Base Pay is:',avbasepay)
print('\nHigest OvertimePay is:',overtimepay)
print('\nEmployee Data:',jobtitleforjoseph)
print('\nTotal PaBenefits for Joseph D:',totalamounjosephearns)
print('\nHigest Paid:',highestpaid)
print('\nLowest Paid:',lowestpaid)
print('\nMean:',meanbtw20112014)
print('\nUnique Job Titles:',uniquejobtt)
print('\nTop 5 common Jobs:',topfivecommonjobs)
print('\nJobs with chief:', numofjobswithchief)
