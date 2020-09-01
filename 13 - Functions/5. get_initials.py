# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 10:52:05 2020

@author: aduzo
"""

# here the code looks slightly different but we are doing the same logic 
# over and over again.

# Ask for a name and return the initials
first_name = input('Enter your first name: ')
first_name_initial = first_name[0:1]

middle_name = input('Enter your middle name: ')
middle_name_initial = middle_name[0:1]

last_name = input('Enter your last name: ')
last_name_initial = last_name[0:1]

print('Your initials are: '+ first_name_initial \
      + middle_name_initial + last_name_initial)