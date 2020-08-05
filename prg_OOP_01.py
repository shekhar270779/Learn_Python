# Python Object Oriented Programming

'''
Object Oriented programming (OOP) is a programming paradigm that is based on the concept of classes and objects.
Reusable pieces of code blueprints are called classes, which are used to create individual instances of objects.

Building blocks of OOP
- class : Classes allow to logically group data and functions
- object : instances of  a class are called as objects
- method
- attribute
'''


class Employee:
    pass

# e1 and e2 below are two instances of class Employee
e1 = Employee()
e2 = Employee()

print(f"Id of object e1 is {id(e1)}")
print(f"Id of object e2 is {id(e2)}")

class Employee:
    def __init__(self, first_name, last_name, gender, sal):
        '''__init__" is a reserved method in python classes. It is known as a constructor in object oriented concepts.
        This method is called when an object is created from the class and it allow the class to initialize the
        attributes of a class. '''
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.sal = sal
        self.email = first_name + '.' + last_name + '@company.com'

    def fullname(self):
        return self.first_name + ' ' + self.last_name

# Creating instances of the class Employee
emp_list = []
emp_list.append(Employee('Annie', 'Kapoor', 'F', 30000))
emp_list.append(Employee('Shyam', 'Bose', 'M', 35000))

for e in emp_list:
    print(e.fullname(), e.gender, e.sal, e.email)

for e in emp_list:
    print(Employee.fullname(e))


class Car:
    def __init__(self, company, model, color, speed_limit):
        self.company = company
        self.model = model
        self.color = color
        self.speed_limit = speed_limit

    def get_speed_limit(self):
        return self.speed_limit

    def get_model(self):
        return self.model

my_first_Car = Car('Hyundai', 'i10', 'red', 150)
print(f"My first car is {my_first_Car.get_model()}, having max speed limit as {my_first_Car.get_speed_limit()}")


