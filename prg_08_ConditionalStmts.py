
## Conditional Statements

# if-else
num = 27

if num % 2 == 0:
    print(f'{num} is Even')
else:
    print(f'{num} is odd')

# if-elif-else
num = 9
if num >= 30:
    print('>= 30')
elif num >= 20:
    print('>= 20')
elif num >= 10:
    print('>= 10')
else:
    print('less than 10')

### Boolean operations
# and, or, not

x = 10
y = 12
z = 13

if (x % 2 == 0) and (y % 2 == 0):
    print('Both x and y are even')

if (x % 2 == 0) or (z % 2 == 0):
    print('Atleast one is even')

if not (z % 2 == 0):
    print(f'{z} is not even')

## None
if None:
    print('None evaluates to true')
else:
    print('None evaluates to False')

## Non Zero
if -1:
    print('Non-zero evaluates to true')
else:
    print('Non-zero evaluates to False')


## Zero
if 0:
    print('Zero evaluates to true')
else:
    print('Zero evaluates to False')

# Empty String
if '':
    print('Empty string evaluates to true')
else:
    print('Empty string evaluates to False')

L = [] # Empty list

# Empty objects
if L:
    print('Empty object evaluates to true')
else:
    print('Empty object evaluates to False')

https://www.youtube.com/watch?v=6iF8Xb7Z3wQ