# CSC 101
# Sharna Hossain
# Program 15 | sale_price.py

# In my modification of Program 15, I have compiled the
# discount algorithm into a function and am using the
# convertToUSD helper function to format the return
# I am also generating a random discount with the randomNum()
# helper function

# Importing convertToUSD() from helper_functons.py
from helper_functions import convertToUSD, randomNum

# This program gets an item's original price and
# calculates its sales price, with a 20% discount.
# Get the item's original price.
original_price = float(input("Enter the item's original price:\t"))

# I created a function to compute the discount.


def calculate_discount(price, discount):
    # Calculate the amount of the discount.
    discount = price * discount
    # Calculate the sales price.
    return price - discount

# Generating random discount with random() function
discount = randomNum("float", .1, .9)

# Executing calculate_discount function and storing it
sale_price = calculate_discount(original_price, discount)

# Display the formatted discount value as a percentage
print(f'The discount is {"{:.2f}".format(discount * 100)}%')

# Using the convertToUSD() helper function to format sale pirce
print(f'The sale price is {convertToUSD(sale_price)}')
