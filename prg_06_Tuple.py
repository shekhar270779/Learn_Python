## Tuple
# A Tuple is an immutable sequence of elements.
# Tuples are sequences, just like lists.

## Create a tuple
symbols = ('R', 'G', 'B', 'O', 'W')

# Check type
print('symbols is a ', type(symbols))

# Print elements of tuple
print('Elements of symbols:', symbols)

# Access range of elements # Slicing
print(symbols[0:3])

# Tuple unpacking
x, y, z = (4, 5, 6)
print(f'After unpack x:{x}, y:{y}, z:{z}')

# Swap values
a = 1
b = 2

a , b = b , a
print(f'After Swapping: a:{a}, b:{b}')

# Zip() Parallel iteration through Zip()

adjectives = ('tall', 'hot', 'light', 'large')
nouns = ('giraffe', 'fire', 'feather', 'life','flash')

for adj, noun in zip(adjectives, nouns):
    print(f'As {adj} as {noun}')


# map(fun, iterable) : applies function to every element of iterable
nums = (1, 2, 3, 4)
import math
sqrt_nums = tuple(map(math.sqrt, nums))
print('sqrt_nums', sqrt_nums)

# range
multiples_of_five = tuple(range(5, 20, 5))
print(f'multiples of five: {multiples_of_five}')

# slice() : with help of slice() we can create a slice of an object
things = ('apple', 'banana', 'carrot', 'dish', 'egg', 'fish', 'grapes')
slice_indexes = slice(0, 5)
some_things = things[slice_indexes]
print(f'some_things: {some_things}')






