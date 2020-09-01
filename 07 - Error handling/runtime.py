x= 42
y = 0

'''
try/except/finally is not used to find bugs, 
bugs, you usually have control over them
'''
try:
    print(x/y)
except ZeroDivisionError as e:
    # Optionally, log e somewhere
    print(e)

else :
    print('Something really went wrong')
finally:
    print('This always runs on success or failure')