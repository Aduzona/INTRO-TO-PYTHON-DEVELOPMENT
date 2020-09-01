# Custom string formatting

first_name= 'Diego'
last_name = 'Uchendu'

output = 'Hello, ' + first_name + ' ' + last_name
print(output)

# {} {} specifies accordingly
output =' Hello, {} {}'.format(first_name,last_name)
print(output)

# to specify order, 1= first_name, 0=last_name
output = 'Hello, {1} , {0}'.format(first_name,last_name)
print(output)

# Only available in Python 3 
#output = f"Hello, {first_name}. your last name is  {last_name}. "  #gives me error
#print(output)