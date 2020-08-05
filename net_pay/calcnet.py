# CSC 101
# Sharna Hossain
# module for net_pay.py

# Value of tax
TAX = 0.15

def get_info():
    # Create empty dictionary to store employee info
    employee = {}
    # Get input data
    employee["name"] = input("What is your name?\t\t")
    employee["rate"] = float(input("What is your rate of pay?\t\t"))
    employee["hours"] = float(input("How many hours did you work?\t\t"))
    # Calculate the gross from input data
    employee["gross"] = float(employee["hours"] * employee["rate"])
    # Return employee dictionary
    return employee

def calculate_net(gross):
    # Deduct taxes to calculate the net
    gross -= float(gross * TAX)
    # Return gross
    return gross