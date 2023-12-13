# regular methods always takes the instances as the first argument,
# to take the class as the first argument we can use a decorator
# a method that has a logical relation to the class but is not 
# related to any class variable is called a static method

import datetime

class Employee:
    
    num_of_emps = 0
    raise_amount = 1.1
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        Employee.num_of_emps += 1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Loyumba','Moirangthem',30000)
emp_2 = Employee('Test','User',50000)

print(Employee.raise_amount)
print(emp_1.raise_amount)

Employee.set_raise_amount(1.08)

print(Employee.raise_amount)
print(emp_1.raise_amount)

emp_str_1 = 'John-Doe-60000'

emp_3 = Employee.from_string(emp_str_1)

print(emp_3.__dict__)

my_date = datetime.date(2023, 9, 23)
print(Employee.is_workday(my_date))