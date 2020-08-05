'''
Static Methods:
Static methods don't pass either instance or class as parameter to method.
They behave like normal functions.
Static method knows nothing about the class and just deals with the parameters.
'''

class Employee:

    def __init__(self, fname, lname, sal):
        self.fname = fname
        self.lname = lname
        self.sal = sal

    def fullname(self):
        return self.fname + ' ' + self.lname

    @staticmethod
    def is_weekend(worked_dt):
        if worked_dt.weekday() in (5, 6): # Sat/sun have weekday represented as 5, 6 respectively:
            return True
        else:
            return False


import datetime
e5 = Employee('Kim', 'John', 30000)

today = datetime.date.today()
yesterday = today + datetime.timedelta(days=-1)
day_before_yesterday = yesterday + datetime.timedelta(days=-1)

worked_on = list((today, yesterday, day_before_yesterday))

for day in worked_on:
    print(f"{e5.fullname()} worked on : {day}, is it a weekend? {Employee.is_weekend(day)}")

