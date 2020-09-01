import json

# Create a dictionary object
person_dict = {'first': 'Christopher', 'last':'Harrison'}
# Add additional key pairs to dictionary as needed
person_dict['City']='Seattle'

# create a staff dictionary
# assign a person to a staff position of program manager
staff_dict={}
staff_dict['Program Manager']=person_dict



person_dict2 = {'first': 'Diego', 'last': 'Uchendu'}
# Add additional key pairs to dictionary as needed
person_dict2['City']= 'Magdeburg'
staff_dict['Operations Manager']=person_dict2



# Convert dictionary to JSON object
staff_json = json.dumps(staff_dict)

# Print JSON object
print(staff_json)