# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 13:50:47 2021

@author: Charles Mbithi
"""

import pandas as pd

ecom = pd.read_csv('Ecommerce Purchases')
avpurchaseprice = ecom['Purchase Price'].mean()
highestpurchaseprice = ecom['Purchase Price'].max()
lowestpurchaseprice = ecom['Purchase Price'].min()
enlang = sum(ecom['Language'] == 'en')
am = sum(ecom['AM or PM'] == 'AM')
pm = sum(ecom['AM or PM'] == 'PM')
commonjobtt = ecom['Job'].value_counts().head(5)
combpp = ecom[ecom['Lot'] == '90 WT']['Purchase Price']#confirm
email = ecom[ecom['Credit Card'] == 4926535242672853]['Email']
card = ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price']>95)].count()

def string_laywer(title):
    if 'Lawyer' in title.split():
        return True
    else:
        return False
    
def card_expire(expiary):
    if '25' in expiary.split():
        return True
    else:
        return False
    
jobtitle = sum(ecom['Job'].apply(lambda t: string_laywer(t)))
cardexp = sum(ecom['CC Exp Date'].apply(lambda e: card_expire(e)))

print(ecom.head())
print('\nAverage Purchase Price:',avpurchaseprice)
print('\nHighest Purchase Price:',highestpurchaseprice)
print('\nLowest Purchase Price:',lowestpurchaseprice)
print('\nLanguage:',enlang)
print('\nJob Title:',jobtitle)
print('\nAm count is :',am,'\nPm count is: ', pm)
print('\nFive top common jobs:',commonjobtt)
print('\nPurchase Price for Item bought from 90 WT:',combpp)
print('\nEmail:',email)
print('\nCard Provider:',card)
print('\nCard Expiary:',cardexp)

for col in ecom.columns:
    print(col)