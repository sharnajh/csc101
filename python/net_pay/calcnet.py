# CSC 101
# Sharna Hossain
# module for net_pay.py


def calculate_gross(hours, rate):
    return float(hours * rate)


def calculate_net(gross, tax):
    # Deduct taxes to calculate the net
    gross -= float(gross * tax)
    # Return gross
    return gross


def get_info(tax):
    # Create empty dictionary to store employee info
    employee = {}
    # Get input data
    employee["name"] = input("What is your name?\t\t")
    employee["rate"] = float(input("What is your rate of pay?\t\t"))
    employee["hours"] = float(input("How many hours did you work?\t\t"))
    # Calculate the gross from input data
    employee["gross"] = calculate_gross(employee["hours"], employee["rate"])
    # Calculate the net from input data
    employee["net"] = calculate_net(employee["gross"], tax)
    # Return employee dictionary
    return employee


def display_info(employee):
    print(f"Name:\t{employee['name']}")
    print(f"Hours Worked:\t{employee['hours']}")
    print(f"Rate of Pay:\t${format(employee['rate'], ',.2f')}")
    print(f"Net Pay:\t${format(employee['net'], ',.2f')}")
