import sys

print(sys.version_info)

msg = 'Hello there'
print(len(msg))

# access individual elements of a string, we need to use index
# index starts with 0 in python

print(msg[0])

# access a range of characters
# first index is starting index, other index is stopping point
# second index is exclusive
print(msg[0:5])

msg = 'I am liking Python'
print(msg[0::2])

print(msg[::-1])
# nohtyP gnikil ma I

######## String functions ####
msg = 'Hello Python'

# Convert string into lower case
print(msg.lower())

# Convert string into upper case
print(msg.upper())

# Count the frequency of character in a string
print(msg.count('o'))

# find first index of character in string
print(msg.find('o'))

# if character is not found it returns -1
print(msg.find('z'))

# replace
new_msg = msg.replace('Python', 'Universe')
print(new_msg)

# Concatenate strings using + sign
greeting = 'Hello!!'
wish_bday = 'Happy B\'day!!'

msg = greeting + wish_bday
print(msg)

# Formatted string using {} placeholders
wish_anniversary = 'Happy Anniversary'
another_msg = '{}, {}'.format(greeting, wish_anniversary)
print(another_msg)

# f-strings , works with Python 3.6 and above
# String formatting becomes easier as we can pass
# variables names in place holders directly
wishes = f'{msg} {another_msg}'
print(wishes)
