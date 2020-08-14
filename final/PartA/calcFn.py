# CSC 101
# Sharna Hossain
# Final | Part A
# calcFn.py

# Global var for tax
TAX = 0.16

# Calculate gross


def calc_gross(hours, rate, deduction):
    return float((hours * rate) - deduction)

# Calculate net


def calc_net(gross):
    return float(gross + (gross * TAX))


# Empty ist to hold employees
employees = []

# Create employee object


def create_employee(name, hours, rate, deduction):
    # Get gross pay
    gross = calc_gross(hours, rate, deduction)

    # Push object to employees list
    employees.append({
        "name": name.title(),
        "hours": hours,
        "rate": rate,
        "gross": gross
    })


# Create employees
# Name HrsWork RateP Deduction
# John Doe 55 35.78 $250.00
# Jane Doe 48 66.75 $412.00
# Jenny Doe 39  55.12 $525.00
create_employee("john doe", 55, 35.78, 250.00)
create_employee("jane doe", 48, 66.75, 412.00)
create_employee("jenny doe", 39, 55.12, 525.00)

# Menu Option Functions
# Display Info


def calc_payroll():
    # Loops through all of the employees
    for employee in employees:
        name = employee["name"]
        # Calculates the net
        net = calc_net(employee["gross"])
        # Formats the net
        net = format(net, ',.2f')
        print(f"{name}'s net pay is ${net}")

# Display Data


def display_data():
    # Loops through all of the employees
    for employee in employees:
        print(employee["name"])
        # Loops through all of the key val pairs in employee object
        for key, value in employee.items():
            # Checks if data type is a float and formats to currency
            if isinstance(value, float):
                value = f"${format(value, ',.2f')}"
            print(f'{key.title()}:\t{value}')
