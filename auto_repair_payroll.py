# CSC 101
# Sharna Hossain
# Chapter 10 | Program 2
# auto_repair_payroll.py

# Named constants to represent the base hours and
# the overtime multiplier
BASE_HOURS = 40         # Base hours per week
OT_MULTIPLIER = 1.5     # Overtime multiplier

# Function that checks if input is valid data type
def generateFloatInput(message):
    value = input(f'{message}\t')
    # If input has any letters in it, will continue
    # to keep asking for input until a valid float
    # is entered.
    while value.isalpha():
        print(f'"{value}" is not a valid float')
        value = input(f'{message}')
    return value

# Get the hours worked and the hourly pay rate.
# Using generateFloatInput() to check valid data types.
hours = float(generateFloatInput('Enter the number of hours worked:'))
pay_rate = float(generateFloatInput('Enter the hourly pay rate:'))

# Calculate and display the gross pay.
if hours > BASE_HOURS:
    # Calculate the gross pay with overtime.
    # First, get the number of overtime hours worked.
    overtime_hours = hours - BASE_HOURS
    # Print how many overtime hours worked.
    print(f'You worked {overtime_hours} hours of OT.')

    # Calculate the amount of overtime pay.
    overtime_pay = overtime_hours * pay_rate * OT_MULTIPLIER

    # Calculate the gross pay.
    gross_pay = BASE_HOURS * pay_rate + overtime_pay
else:
    # Calculate the gorss pay without overtime.
    gross_pay = hours * pay_rate

# Display the gross pay.
# Used the F-string to inject python into string.
gross_pay = format(gross_pay, ",.2f")
print(f'The gross pay is ${gross_pay}')