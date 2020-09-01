# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 11:16:59 2020

@author: aduzo
"""

# Create a calculator function
# The function should accept three parameters:
# first_number: a numeric value for the math operation
# second_number: a numeric value for the math operation
# operation: the word 'add' or 'subtract'
# the function should return the result of the two numbers added or subtracted
# based on the value passed in for the operator
#

def calculator(first_number,second_number,operator):
    if operator.upper() == 'ADD':
        result = first_number +  second_number
    elif operator.upper() == 'SUBTRACT':
        result =first_number -  second_number
    else:
        result = 'Type in  operator ADD or SUBTRACT'
    return result
first_number= float(input('Please enter the first number: '))
second_number = float(input('Please enter the second number: '))
operator =input('Please input ADD or SUBTRACT: ')

print(str(first_number) + ' ' + str(second_number) + ' ' + str(calculator(first_number,second_number,operator)))
# Test your function with the values 6,4, add 
# Should return 10
#
# Test your function with the values 6,4, subtract 
# Should return 2
# 
# BONUS: Test your function with the values 6, 4 and divide 
# Have your function return an error message when invalid values are received