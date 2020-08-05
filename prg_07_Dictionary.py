
# Dictionary : Dictionary allows to create a data structure in form of key:value pair
# Dictionary is an unordered collection of elements
# key is a unique identifier


synonyms = {'transaction': 'An act of carrying out some form of business between two persons',
            'negotiation': 'An act of bargaining',
            'consortium': 'A corporation made up of a number of different companies that operate in diversified fields.'
            }

print(type(synonyms))
print(synonyms)

employee = {'name': 'Ram', 'age': 27, 'location':'Delhi'}
print(employee)

# access elements by keys
print(employee['name'])
print(employee['age'])

print(f"{employee['name']} is {employee['age']} years and lives in {employee['location']}")

# get()
print(employee.get('name'))
print(employee.get('salary'))
print(employee.get('salary', 'Not defined'))

# add a new key
employee['salary'] = 10000
print(employee.get('salary', 'Not defined'))

# update value of key
employee['salary'] = 15000
print(employee.get('salary', 'Not defined'))

# more than one updates
employee.update({'age': 35, 'gender':'Male'})
print(employee)

# delete a key
del employee['gender']
print(employee)

# pop
loc = employee.pop('location')
print(employee)
print('location:', loc)

# find no. of keys
print('employee has no. of keys =',  len(employee))

# to list all keys
print(employee.keys())

# to list all values
print(employee.values())

# to list keys and values
for k,v in employee.items():
    print(f'{k} = {v}')

# loop through keys
for k in employee:
    print(employee[k])