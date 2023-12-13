# special methods are enclosed usually with double underscore
# hence, they are also called dunder methods

class Employee:
    
    num_of_emps = 0
    raise_amount = 1.08
    
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
    
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
    
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)


emp_1 = Employee('Loyumba','Moirangthem',50000)

print(emp_1)
print(repr(emp_1)) # this is the same as print(emp_1.__repr__())
print(str(emp_1)) # this is the same as print(emp_1.__str__())