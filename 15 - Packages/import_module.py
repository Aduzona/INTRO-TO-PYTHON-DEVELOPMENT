# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 13:44:58 2020

@author: aduzo
"""

# To use a module,
# import module as namespace
# this code pulled in all of the functions and made it available
# inside a little collection, or inside what is known as a namespace
import helpers # the name of the python file we created
helpers.display('Sample message',True) # there is a display function inside it

# from module helpers, I want to import everything.
# Everything in  this module will become globally available
# import all into current namespace
from helpers import *
display('Not a warning')

# Just grab one item
#import specific item into current namespace
from helpers import display
display('Not a warning')

'''
It is best to import only items you need else you will see
more suggestions from your intelliscence
'''



'''

'''