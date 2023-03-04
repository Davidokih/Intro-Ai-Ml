class Employee():
    employee_namw = "Ben"
    department = "sales"
    starting_year = 2020
    salary = 5000

myObject = Employee()
print(myObject.employee_namw)
print(myObject.department)
print(myObject.starting_year)
print(myObject.salary)

# Working with the class constructor method known as the _init_
# The self paramiter in the _init_ method allow us to access all attributes in a class

class Employee1():
    def __init__(self, employee_name, department, starting_year, salary):
        self.employee_name = employee_name
        self.department = department
        self.starting_year = starting_year
        self.salary = salary

employee1 = Employee1("John","sales",2022,5000)

print(employee1.employee_name)
print(employee1.department)
print(employee1.starting_year)
print(employee1.salary)