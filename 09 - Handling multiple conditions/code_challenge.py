# Ask a user their name
name =input('What is your name? ')

# If their first name starts with A or B 
# tell them they go to room AB
first_letter = name[0:1]
if first_letter.upper() in ('A','B'):
    room = 'AB'
# IF their first name starts with C
# tell them to go to room CD
elif first_letter.upper() == 'C':
    room ='CD'
    
else:
    # If their first name starts with another letter, ask for their last name
    # IF their last name starts with Z, tell them to go to room Z
    last_name = input('what is your last name? ')
    last_name_first_letter = last_name[0:1]
    
    # if their last name starts with any other letter, tell them to go to room OTHER
    if last_name_first_letter == 'Z':
        room = 'Z'
    else:
        room = 'OTHER'
print('Please go to room '+ room)

# When you are done
# Anna should be in room AB
# Bob should be in room AB
# Charlie should be in room C
# Khalid Haque should be in room OTHER
# Xin Zhao should be in room Z