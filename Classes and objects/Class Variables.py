class Employee:
    
    num_of_emps = 0
    raise_amount = 1.1
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        # we use Employee instead of self, just so it can be overwritten if needed be
        Employee.num_of_emps += 1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
# this would return 0
print(Employee.num_of_emps)

emp_1 = Employee('Loyumba','Moirangthem',30000)
emp_2 = Employee('Test','User',50000)

print(Employee.raise_amount)
# The following are accessing the Employee attributes
print(emp_1.raise_amount)
print(emp_2.raise_amount)


# here we can see that there is no raise amount
print(emp_1.__dict__)

# the raise amount is being accessed from here
print(Employee.__dict__)


# the raise amount can be change for the entire class as:
Employee.raise_amount = 1.13

# but doing this will only change for one employee
emp_1.raise_amount = 1.15
# once this is done, emp_1 will have raise_amount
print(emp_1.__dict__)

# but it won't be in emp_2
print(emp_2.__dict__)

# this would return 2
print(Employee.num_of_emps)