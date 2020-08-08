# CSC 101
# Sharna Hossain
# Program 18 | future_value.py

# In my modification of Program 18, I have grouped all of the
# steps to compute the future value into a function.

# I compressed all of the steps into a function
def calculate_amount():
    # Get the desired future value.
    future_value = float(input('Enter the desired future value:\t'))
    # Get the annual interest rate.
    rate = float(input('Enter the annual interest rate:\t'))
    # Get the number of years that the money will appreciate
    years = int(input('Enter the number of years the money will grow:\t'))
    # Calculate the amount that needed to deposit and return
    present_value = future_value / (1.0 + rate)**years
    # Display the amount needed to deposit
    return print(f'You will need to deposit this amount: {present_value}')


# Executing function
calculate_amount()
