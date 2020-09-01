# arrays are collections of same data types
# to use an array, you must first create an array object
# and you will get there by bringing in from the array library

from array import array
scores = array('d')# d means that we are using numeric data type double
scores.append(97)
scores.append(98)
print(scores)
print(scores[1]) # assess second item which is 98.0


'''
Difference between Array and a List.

Arrays: Numerical data types and Must all be the same type.
This helps you to avoid bugs like putting in a string when 
you are dealing with numbers.

Lists: Store anything and Store any type


'''