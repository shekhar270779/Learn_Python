'''
Class Inheritance: Inheritance allows a class to inherit attributes and methods from parent class.
This is useful as we can create subclass which inherits all functionality of parent class, also if required
we can override, or add new functionality to sub class without affecting parent class
'''

class Employee:

    sal_hike_per = 4

    def __init__(self, fname, lname, sal):
        self.fname = fname
        self.lname = lname
        self.sal = sal

    def fullname(self):
        return self.fname + ' ' + self.lname

    @classmethod
    def set_sal_hike_per(cls, per):
        cls.sal_hike_per = per

    def apply_sal_hike(self):
        self.sal = int(self.sal * (1 + self.sal_hike_per/100))


# Create Sub Class engineer which inherits Employee
class Engineer(Employee):
    pass

e1 = Engineer('Tom', 'Walter', 30000)
print(e1.fullname())
e1.apply_sal_hike()
print(e1.sal)

class Manager(Employee):
    sal_hike_per = 10 # overriding class variable

e2 = Manager("Kim", "Jones", 30000)
e2.apply_sal_hike()
print(f"{e2.fullname()} after salary hike has salary {e2.sal}")


class Developer(Employee):
    def __init__(self, fname, lname, sal, main_skill):
        super().__init__(fname, lname, sal)
        self.main_skill = main_skill


e3 = Developer("Ash", "Watson", 30000, "Python")
print(f"{e3.fullname()} has key skill as {e3.main_skill}")


class Lead(Employee):
    def __init__(self, fname, lname, sal, employees=None):
        super().__init__(fname, lname, sal)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        print(f"Team of {self.fullname()}")
        for emp in self.employees:
            print('--->' + emp.fullname())


e4 = Lead("Ashley", "King", 30000, [e1])
print(f"{e4.fullname()}  ")
e4.print_employees()

print(f"Adding employees to team of {e4.fullname()}")
e4.add_employee(e2)
e4.add_employee(e1)
e4.print_employees()

print(f"Removing {e1.fullname()} from team of {e4.fullname()}")
e4.remove_employee(e1)
e4.print_employees()

