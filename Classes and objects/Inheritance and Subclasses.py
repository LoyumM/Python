# Inheritance allows us to inherit atrributes and methods
# from parent classes
# THis is useful because we can create subclasses with the
# functionality of the parent classes and override or add 
# new functionality without affecting the parent classes in 
# any way

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
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
class Developer(Employee):
    # changing the insances here in the subclasses won't have
    # any effect on the parent classes
    raise_amount = 1.1
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # this is going to let Employee init method handle the first three arg
        # Employee.__init__(self, first, last, pay) # this also works
        self.prog_lang = prog_lang
        
class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees
            
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self):
        employee_names = [emp.fullname() for emp in self.employees]
        print("The list of employee(s)", self.fullname(),"manages are: ",", ".join(employee_names))

dev_1 = Developer('Loyumba','Moirangthem',50000, 'Python')
emp_2 = Employee('Test','User',50000)

# print(dev_1.email)
# print(help(Developer))
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
dev_1.apply_raise()
print(f"Salary after two years is {dev_1.pay}")
print(dev_1.prog_lang)
print(emp_2.pay)
emp_2.apply_raise()
print(emp_2.pay)
emp_2.apply_raise()
print(f"Salary after two years is {emp_2.pay}")


mgr_1 = Manager('Lucky','Takhellambam', 90000, [dev_1])
mgr_1.print_emps()
mgr_1.add_emp(emp_2)
mgr_1.print_emps()
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

print(issubclass(Developer, Employee))
print(issubclass(Manager, Developer)) 