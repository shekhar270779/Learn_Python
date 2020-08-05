'''
Class variables are variables that are shared amongst all instances of a class
Instance variables are unique for each instance, whereas Class variables are same for each instance
'''


class Employee:

    sal_raise_per = 4
    emp_count = 0
    def __init__(self, fname, lname, gender, sal):
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.sal = sal
        self.email = self.fname + ' ' + self.lname + '@company.com'
        Employee.emp_count += 1

    def fullname(self):
        return self.fname + ' ' + self.lname

    def apply_raise(self):
        self.sal = int(self.sal * (1 + self.sal_raise_per /100))





e1 = Employee('Annie', 'Kapoor', 'F', 30000)
e1.apply_raise()
print(f"{e1.fullname()} has salary {e1.sal}")
print(f"Employee got raise as {Employee.sal_raise_per}%")


Employee.sal_raise_per = 5
e2 = Employee('Kiran', 'Bajaj', 'F', 30000)
e2.apply_raise()
print(f"{e2.fullname()} has salary {e2.sal}")
print(f"Employee got raise as {Employee.sal_raise_per}%")

e3 = Employee('Komal', 'Kapoor', 'F', 30000)
e3.sal_raise_per = 10
e3.apply_raise()
print(f"{e3.fullname()} has salary {e3.sal}")
print(f"Employee got raise as {e3.sal_raise_per}%")

e4 = Employee('Shyam', 'Bose', 'M', 30000)
e4.apply_raise()
print(f"{e4.fullname()} has salary {e4.sal}")
print(f"Employee got raise as {e4.sal_raise_per}%")

print(Employee.emp_count)

