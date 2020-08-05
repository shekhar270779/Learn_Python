
# String Formatting

name = 'John'
age = str(25)

sentence_1 = 'My name is ' + name + '. I am ' + age + ' years old'
print(sentence_1)

sentence_2 = 'Hey I am {} and I am {} years old'.format(name, age)
print(sentence_2)

sentence_3 = 'I am {1} years old and I am {0}, yes {0}'.format(name, age)
print(sentence_3)

sentence_4 = f'I am {name} and I am {age} years old'
print(sentence_4)

sentence5 = f'I am {name.upper()}'
print(sentence5)

pi = 3.14159
print(f'value of pi upto 2 decimal places : {pi:.2f}')

largenum = 987654321.123456789
print(f' largenum is {largenum:,.2f}')

