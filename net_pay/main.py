# CSC 101
# Sharna Hossain

# Calculate net pay of an employee
# Get name, hours worked, and rate of pay

# Import module with functions
import calcnet

# Main function
def main():
    # Get employee info and store into local var
    employee = calcnet.get_info()
    # Calculate net pay and store in dictionary
    employee["net"] = calcnet.calculate_net(employee["gross"])
    # Print the information
    calcnet.display_info(employee)
    
main()