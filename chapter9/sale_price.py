# CSC 101
# Sharna Hossain
# Program 15 | sale_price.py

# In my modification of Program 15, I have compiled the
# discount algorithm into a function and am using the
# convertToUSD helper function to format the return

# Importing convertToUSD() from helper_functons.py
from helpers.helper_functions import convertToUSD

# This program gets an item's original price and
# calculates its sales price, with a 20% discount.
# Get the item's original price.
original_price = float(input("Enter the item's original price:\t"))

# I created a function to compute the discount.
def calculate_discount(price,discount):
    # Calculate the amount of the discount.
    discount = price * discount
    # Calculate the sales price.
    return price - discount

sale_price = calculate_discount(original_price,.2)

# Display the sale price.
# Using the convertToUSD() helper function
print(f'The sale price is {convertToUSD(sale_price)}')