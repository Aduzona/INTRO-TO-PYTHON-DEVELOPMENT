# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 10:44:48 2020

@author: aduzo
"""

# You can use a function by passing in parameters
from datetime import datetime

# Define a function to print the current time and task name
#  task_name: Name of the task to display to output screen
def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()
    
first_name = 'Susan'
# Call print_time() function to display message and current time
# pass in name of task completed
print_time('first name assigned')

for x in range(0,10):
    print(x)
    
# Call print_time() function to display message and current time
# pass in name of task completed
print_time('loop completed')