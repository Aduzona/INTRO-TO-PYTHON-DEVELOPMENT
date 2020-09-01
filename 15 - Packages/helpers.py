# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 13:38:44 2020

@author: aduzo
"""
'''
What is a module?
A Python file with functions, classes and other components
Why use modules?
Break code down into reusable structures

'''

# To Create a module:
'''
1. create a file e.g helpers.py
2. Add the appropriate code e.g a method
'''

'''
def display(message, is_warning=False):
    if is_warning:
        print('Warning!!')
    print(message)
    
'''
from colorama import init, Fore

def display(message, is_warning=False):
    if is_warning:
        print(Fore.RED + 'Warning!!')
    else:
        print(Fore.BLUE + message)