import datetime


# Create a function called print_time
# This function will print the message and current time
def print_time():
    print('task completed')
    
    # in the datetime library, call the datetime object(class)
    # call the now function of that datetime class or object
    print(datetime.datetime.now())
    print()

first_name = 'Susan'
# Call print_time() function to display message and current time
print_time()

for x in range(0,10):
    print(x)

# Call print_time() function to display message and current time
print_time()