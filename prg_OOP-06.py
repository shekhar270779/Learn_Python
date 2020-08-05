'''Inheritance Example
'''

class Employee:
    def __init__(self, empid, name):
        self.empid = empid
        self.name = name


class SalariedEmployee(Employee):
    def __init__(self, empid, name, monthly_salary):
        super().__init__(empid, name)
        self.monthly_salary = monthly_salary
    def calculate_yearly_payroll(self):
        return self.monthly_salary * 12


class HourlyEmployee(Employee):
    def __init__(self, empid, name, hours_worked, hour_rate):
        super().__init__(empid, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate
    def calculate_yearly_payroll(self):
        return 365* self.hours_worked *  self.hour_rate


class CommissionEmployee(SalariedEmployee):
    def __init__(self, empid, name, monthly_salary, monthly_commission):
        super().__init__(empid, name, monthly_salary)
        self.monthly_commission = monthly_commission
    def calculate_yearly_payroll(self):
        yearly_fixed = super().calculate_yearly_payroll()
        yearly_commission = 12 * self.monthly_commission
        return yearly_fixed + yearly_commission


class PayrollSystem:
    def calculate_yearly_payroll(self, employees):
        for emp in employees:
            print(f'Yearly payroll for {emp.empid}-{emp.name} : {emp.calculate_yearly_payroll()}')

e1 = SalariedEmployee(1, 'Vicky KAushal', 50000)
e2 = HourlyEmployee(2, 'Ayushman Khurana', 8, 700)
e3 = CommissionEmployee(3, 'Jay Bora', 25000, 500)

hr_payroll_system = PayrollSystem()
hr_payroll_system.calculate_yearly_payroll([e1, e2, e3])


