# CSC 101
# Sharna Hossain
# Chapter 10 | Program 2
# auto_repair_payroll.py

# Named constant to represent the tax
TAX = 0.35

# Create class for employees that take in values for name
# and their rate of pay according to their position
class Employee:
    # __init__ is the function that when executed
    # will create a new instance of the class with
    # the parameters as the data
    def __init__(self, name, position, hours_worked):
        # Format name so it is capitalized
        self.name = name.title()
        self.pay_rate = position
        self.hours_worked = hours_worked


# Create dictionary for employees
employees = {}

# Using a for loop to generate 5 employee objects with data
# received from input funtions
for x in (range(1, 6)):
    # get employee name
    employee_name = input(f"What is employee {x}'s name?\t")
    # get employee pay rate
    employee_pay_rate = float(input(f"What is employee {x}'s pay rate?\t"))
    # get employee hours worked
    employee_hours_worked = float(
        input(f"How many hours did employee {x} work?\t"))
    # create new instane of Employee class with the received data
    employees[employee_name] = Employee(
        employee_name, employee_pay_rate, employee_hours_worked)

# Display the tax rate
print(f'The tax rate is {TAX*100}%')

# looping through employees dictionary to calculate the gross and netpay of each employee and display data
for x in employees.values():
    # calculate gross pay
    x.gross_pay = x.hours_worked * x.pay_rate
    # calculate net pay
    x.net_pay = x.gross_pay - (x.gross_pay * TAX)
    # printing all of the details of each employee
    print(f'{x.name} has a pay rate of ${x.pay_rate}. After working {x.hours_worked} hours, they made a gross of ${format(x.gross_pay,",.2f")} and a net of ${format(x.net_pay,",.2f")}\n')
