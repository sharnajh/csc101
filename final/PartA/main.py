# CSC 101
# Sharna Hossain
# Final | Part A
# __init__.py

# Instructions:
# Write a Python program to calculate the payroll for the following employees.  Payroll tax is 16%.

import calcFn

# Holds menu options
MENU_OPTIONS = {
    "A": "Calculate Payroll",
    "B": "Display Data"
}


def main():
    # Constant local var for the tax
    selection = ""

    print("Welcome to the Employee Portal!")

    # Checks if user input is a menu option
    while not selection in MENU_OPTIONS:
        print("Menu:")

        # Display menu options
        for key, value in MENU_OPTIONS.items():
            print(f'{key}:\t{value}')

        selection = input("What would you like to do today?\t")

    # Executes Function based on menu option
    if selection == "A" or selection == "a":
        calcFn.calc_payroll()
    elif selection == "B" or selection == "b":
        calcFn.display_data()

    print("Thank you for using the Employee Portal!")


main()
