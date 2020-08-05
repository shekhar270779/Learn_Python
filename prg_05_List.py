# List :
# List stores a sequence of elements
# Elements can be heterogeneous
# List is mutable , i.e its elements can be modified

# Create a List
hobbies = ['Cricket', 'Painting', 'Music']
print('List is', hobbies)
print('Type ', type(hobbies))

# elements are indexed starting with 0
# Access first element
print('First hobby in list', hobbies[0])

# Count no. of hobbies
print('No. of hobbies', len(hobbies))

# We can use negative index to access elements from end of list
print('Last hobby in list', hobbies[-1])

rainbow = ['Violet', 'Indigo', 'Blue', 'Green', 'Yellow', 'Orange', 'Red']
# access a range of elements / Slicing
# first 4 colors of rainbow
print('Four colours of rainbow', rainbow[0:4])

# access alternate colors of rainbow
print('Alternate colors of rainbow', rainbow[::2])

# access colors of rainbow in reverse order
print('Reverse colors of rainbow', rainbow[::-1])

# methods for lists

# append(), appends an element to list
rgb = ['Red', 'Green']
rgb.append('Blue')
print('list rgb:', rgb)

# insert an element at specific location
hobbies.insert(0, 'Basketball')
print('Hobbies after insert:', hobbies)

# extend(), when we have multiple values to add to a list
some_more_hobbies = ['Reading', 'Writing']
hobbies.extend(some_more_hobbies)
print('Extended Hobbies:', hobbies)

# remove an element from List
hobbies.remove('Reading')
print('Removed Reading hobby', hobbies)

# pop() , returns last element of list
last_hobby = hobbies.pop()
print('After pop Hobbies :', hobbies)
print('Popped Hobby:', last_hobby)

# delete an itesm by specifying index
print('After delete:', hobbies)
del hobbies[0]
# Reverse elements of list
rainbow.reverse()
print('Reversed rainbow:', rainbow)

# Sort list
rainbow.sort()
print('Sorted rainbow', rainbow)

rainbow.sort(reverse=True)
print('Descending Sort rainbow', rainbow)

# sorted function()

nums = [31, 18, 20, 51]
sorted_nums = sorted(nums)
print('Sorted Numbers:', sorted_nums)

# min() , max(), sum()
print(f'min={min(nums)}, max={max(nums)}, sum={sum(nums)}')

# find index of element
print('20 no. is at index', nums.index(20))

# check for presence of element in list
is_orange = 'orange' in rainbow
print('Is orange in rainbow colors:', is_orange)

# Loop through elements of a list
# specify code of block using indentation
for color in rainbow:
    print('Rainbow color:', color)

# enumerate()
for i, color in enumerate(rainbow):
    print(f'Index : {i}, color:{color}')

# join elements of a list
colors_string = ','.join(rainbow)
print('Join example:\n', colors_string)

# String to list
new_colors = colors_string.split(',')
print(f'new_colors: {new_colors}')

## Mutable

A = [11, 19, 23]
B = A # shallow copy
B[0] = 22
print(f'A:{A}, B:{B}')

C = A[:] # deep copy
C[0] = 100
print(f'A:{A}, B:{B}, C:{C} ')

# List comprehesion
# new lists are created by applying an operation on each element of an existing list.
nums = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in nums]
print(squares)


