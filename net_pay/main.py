# CSC 101
# Sharna Hossain

# Calculate net pay of an employee
# Get name, hours worked, and rate of pay

import calcnet

def main():
    # Get employee info and store into local var
    employee = calcnet.get_info()
    # Calculate net pay
    employee["net"] = calcnet.calculate_net(employee["gross"])

    # Print the information
    print(f"Name:\t{employee['name']}")
    print(f"Hours Worked:\t{employee['hours']}")
    print(f"Rate of Pay:\t${format(employee['rate'], ',.2f')}")
    print(f"Net Pay:\t${format(employee['net'], ',.2f')}")
    
main()