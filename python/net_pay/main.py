# CSC 101
# Sharna Hossain

# Calculate net pay of an employee
# Get name, hours worked, and rate of pay

# Import module with functions
import calcnet


# Main function


def main():
    # Value of tax
    TAX = 0.15
    # Get employee info and store into local var
    employee = calcnet.get_info(TAX)
    # Print the information
    calcnet.display_info(employee)


main()
