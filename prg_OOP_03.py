'''
Class Methods:
    A class method is a method that is bound to a class rather than its object.
    It doesn't require creation of a class instance
    The class method is always attached to a class with the first argument as the class itself
'''

class Employee:
    sal_hike_per = 4

    def __init__(self, fname, lname, sal):
        self.fname = fname
        self.lname = lname
        self.sal = sal

    def apply_sal_hike(self):
        self.sal = int(self.sal * (1 + Employee.sal_hike_per/100))

    def fullname(self):
        return self.fname + ' ' + self.lname

    @classmethod
    def set_sal_hike_per(cls, per):
        cls.sal_hike_per = per

    @classmethod
    def from_string(cls, emp_str):
        '''
        emp_str is in form of 'emailid, sal'
        '''
        email, sal = emp_str.split(',')
        empname, companyname = email.split('@')
        fname, lname = empname.split('.')
        return cls(fname.capitalize(), lname.capitalize(), int(sal))

e1 = Employee('Sara', 'Jones', 30000)
e1.apply_sal_hike()
print(f"{e1.fullname()} has salary after hike : {e1.sal}")

e2 = Employee('Tom', 'Hankes', 30000)
Employee.set_sal_hike_per(5)
e2.apply_sal_hike()
print(f"{e2.fullname()} has salary after hike : {e2.sal}")

e3_str = 'jimmy.shergill@company.com, 30000'
e3 = Employee.from_string(e3_str)
e3.apply_sal_hike()
print(f"{e3.fullname()} has salary after hike: {e3.sal}")

# To specify multiple, independent "constructors" using class methods
class vehicle:
    def __init__(self, wheels=2):
        self.wheels = wheels
    @classmethod
    def auto(cls):
        return cls(wheels=3)

    @classmethod
    def car(cls):
        return cls(wheels=4)

    @classmethod
    def truck(cls):
        return cls(wheels=6)

v1 = vehicle()
print(f"v1 has wheels {v1.wheels}")

v2 = vehicle.auto()
print(f"v2 has wheels {v2.wheels}")

v3 = vehicle.car()
print(f"v3 has wheels {v3.wheels}")

v4 = vehicle.truck()
print(f"v4 has wheels {v4.wheels}")