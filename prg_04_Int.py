# Types of Numbers
# Python has 4 types of numbers:
# Booleans
# Integers
# Floating point
# Complex (imaginary numbers)

## Boolean : Booleans have two values: True, False.

a = True
b = False
print(a, b)

# Numerically, they’re evaluated as integers with value 1, 0
print(5 + True)
print(5 * False)

# Integer
x = 5
y = -5
# python has built in function type() to find type of variable
print(type(x))
print('Integers: x, y:', x, y)

# Float
pi = 3.14
print(type(pi))

# floor division using  //
print('Floor division', 5//3)# returns quotient

# modulo i.e  remainder using %
print('Reminder', 5 % 3)

# Exponent or powers using **
print('Exponent', 3**2)


# Increment
x = 10
x += 1 # this is equal to x = x + 1
print('After increment x is ', x)

# Similarly we ca use other opertors

x -= 1
print('Decrement x by 1 ', x)

x *= 5
print('Multiply x by 5 ', x)


# Mathematical functions

# abs() to print absolute value
print('absolute value',  abs(-9))

# round() to n decimal places
print('Round value of 3.1475 up to 2 decimal', round(3.1475, 2))

import math
print('log 100 to base 10', math.log10(100))
print('log 16 to base 2', math.log2(16))

# Arithmetic comparison operators, These return boolean value True or False
# > , < , >=, <=, == , !=
x = 10
y = 11

print('Is x equals to 10?', x == 10)
print('Is x > y?', x > y)
print('Is y != 11', y!= 11)

# Deal numbers which are stored as strings

x = '100'
y = '100'
print('type of x ', type(x))
print('type of y ', type(y))
print(x + y)

# Cast strings to numbers
x = int(x)
y = int(y)
print('type of x ', type(x))
print('type of y ', type(y))
print(x + y)

# Check type
x = 10
print(isinstance(x, int))

x = '10'
print(isinstance(x, str))

x = 10.0
print(isinstance(x, float))





