# use things with key value pairs

person = {'first': 'Christopher'}
person['last'] = 'Harrison'
print(person)
print(person['first'])

'''
Dictionaries:
Key/Value pairs 
Storage order not guaranteed

Lists:
Zero-based index
Storage order guaranteed

'''

diego = {} # initializing dictionary
diego['first'] = 'Diego'
diego ['last'] = 'Uchendu'

susan = {} # initializing dictionary
susan['first'] = 'Susan'
susan ['last'] = 'Ibach'

# list
people = []
people.append('christopher')
people.append('susan')
people.append({
    'first': 'Bill', 'last':'Gates'
})

print(people)

# list of dictionaries
people = []
people.append(diego)
people.append(susan)
people.append({
    'first': 'Bill', 'last':'Gates'
})
print(people)


# runs in my spyder IDE but gives an error  in my vscode
# both IDEs using python 3.7
output =f'list of Dictonaries {people}'
print(output)
