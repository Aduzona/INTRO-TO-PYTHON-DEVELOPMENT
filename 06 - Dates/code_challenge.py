# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 19:14:12 2020

@author: aduzo
"""

from datetime import datetime, timedelta

# print today's date
current_date = datetime.now()
# print yesterday's date
one_day = timedelta(days=1)
yesterday= current_date - one_day
print("yesterday was " + str(yesterday))

# ask a user to enter a date
ent_date = input("Please enter a date (dd/mm/yyy):")
print("you entered " + ent_date)
ent_date = datetime.strptime(ent_date, '%d/%m/%Y') # convert string to datetime object

# print the date one week from the date entered
one_week = timedelta(weeks=1)
last_week = ent_date - one_week
print("Last week's date was: "+ str(last_week))

one_week_later = ent_date + one_week
print('One week later it will be: ' + str(one_week_later))