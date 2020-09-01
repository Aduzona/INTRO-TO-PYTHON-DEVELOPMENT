# used for logging errors, saving to databases to know when that error was written
# or when things happen
#To get current date and time we need to use the datetime library
# get me the date time function from the date time library
from datetime import datetime

current_date = datetime.now()
# The now function returns current date and time as a datetime object

# You must convert the dateime object to a string
# before you can concatenate it to another string
print('Today is:' + str(current_date))
