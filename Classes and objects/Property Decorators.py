class Employee:
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    #using the property decorator allow us to define it like a method but use it like an instance
    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last  = name.split(' ')
        self.first = first
        self.last = last
        
    @fullname.deleter
    def fullname(self):
        print('Name deleted!')
        self.first = None
        self.last = None

emp_1 = Employee('Loyumba','Moirangthem')
print(emp_1.first)
print(emp_1.email)
# print(emp_1.fullname()) # without property
print(emp_1.fullname) # with property

# now using the setter decorator we can update the fullname as
emp_1.fullname = 'Lucky Takhellambam'
print(emp_1.email)


# the deleter decorator as the name suggest is for deleting instances

del emp_1.fullname