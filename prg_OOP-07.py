'''
In Python, method names that have leading and trailing double underscores are
reserved for special use like the __init__ method for object constructors,
or __call__ method to make object callable.

These methods are known as dunder methods. dunder here means “Double Under (Underscores)”.
These dunder methods are often referred to as magic methods.
Although there is nothing magical about them.

Why hassle of wrapping them in double underscores?
The choice of wrapping these functions with double-underscores on either side was really just
a way of keeping the language simple. The Python creators didn’t want to steal perfectly good
method names from us, but they also did not want to introduce some new syntax just to declare
certain methods “special”. The dunders achieve the desired objective of making certain methods
special while also making them just the same as other plain methods in every aspect except naming
convention.

Things to Remember for dunders
1. Call them "dunders" — Since there is nothing magical about them.
2. Implement dunders as desired — It’s a core Python feature and should be used as needed.
3. Inventing our own dunders is highly discouraged — It’s best to stay away from using names
that start and end with double underscores in our programs to avoid collisions with our own methods and attributes.


'''

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


p1 = Person('Amit Patel', 32, 'M')
print(p1)

# When the __init__ method is invoked, the object (in this case, p1) is passed as "self".
# Other arguments used in the method call are passed as the rest of the arguments to the function.

# Object Representation: __str__ , __repr__
# When we define a custom class and try to print its instance to the console, the result does not describe
# the object well, since the default “to string” conversion is basic and lacks details.


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"{self.name} is {self.gender} and of age {self.age}"

    def __repr__(self):
        return f"Person({self.name}, {self.age}, {self.gender})"

    # repr is used for unambigious representation of object and should be used for debugging/logging, meant for developers
    # str is for readable representation of object, meant for end users


p1 = Person('Amit Patel', 32, 'M')
print(p1)

print('Calling repr and str methods')
print(f"repr: {repr(p1)}")
print(f"str: {str(p1)}")

'''
Key points for __str__ , __repr__
1. We can control to-string conversion in our own classes using the __str__ and __repr__ "dunder" methods
2. __repr__ compute the "official" string representation of an object (having all information about the object)
3. __str__ is used for "informal" string representation of an object.
4. If we don’t add a __str__ method, Python falls back on the result of the __repr__ when searching for __str__ . 
   Therefore adding __repr__ to our classes is recommended.
'''

# __add__ dunder add example of int and string
print(int.__add__(1, 2))
print(str.__add__("A", "B"))



class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"{self.name},{self.gender} of {self.age} years"

    def __repr__(self):
        return f"Person({self.name}, {self.age}, {self.gender})"

    def __add__(self, other):
        return self.age + other.age

    def __len__(self):
        return len(self.name)

p1 = Person('Amit Patel', 32, 'M')
p2 = Person('Kartik Aryan', 28, 'M')
print(f"Adding {p1} & {p2}: {p1 + p2}")

print(f"Length {p1}: {len(p1)}")