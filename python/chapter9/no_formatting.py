# CSC 101
# Sharna Hossain
# Program 19 | no_formatting.py

# In my modification of Program 19, I have created a function
# that computes the monthly payment from a randomly generated
# amount_due value and formats the return
# with the convertToUSD helper function

# Import convertToUSD() from helper_functions
from helper_functions import convertToUSD, randomNum

# This demonstrates how a floating-point number is displayed
# with no formatting.


def get_monthly_payment(amount):
    # Format
    return convertToUSD(amount/12)


# Generate random value with randomNum() helper function
amount_due = randomNum('float', 1000, 5000)
monthly_payment = get_monthly_payment(amount_due)
print(f'The monthly payment is {monthly_payment}')
