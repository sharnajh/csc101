# CSC 101
# Sharna Hossain
# Chapter 11 | Program 16
# retail_with_validation.py

# This program calculates retail prices.

# In my alteration of retail_with_validation.py, I will 
# set a maximum number of items that the user can add
# and I will be storing all of the return values in their
# own list.

MARK_UP = 2.5       # The markup percentage.
another = 'y'       # Variable to control the loop.
MAXIMUM_ITEMS = 5   # Control how many items the user can enter.

# List that will store all of the user inputs.
prices = []

# Process one or more items.
# Checks if the length of prices list hasn't exceeded MAXIMUM_ITEMS.
while (another == 'y' or another == 'Y') and (len(prices) < MAXIMUM_ITEMS):
    # Get the item's wholesale cost.
    wholesale = float(input("Enter the item's wholesale cost:\t"))

    # Validate the wholesale cost.
    while wholesale < 0:
        print("ERROR: the cost cannot be negative!")
        wholesale = float(input("Enter the correct wholesale cost:\t"))

    # Calculate the retail price.
    retail = wholesale * MARK_UP
    
    # Display the retail price.
    print(f"Retail price: ${format(retail, ',.2f')}")

    # Store the retail price in a list
    prices.append(retail)

    # Do this again only if the length of the prices list hasn't
    # exceeded the MAXIMUM_ITEMS var
    if len(prices) < MAXIMUM_ITEMS:
        another = input('Do you have another item? (Enter y for yes):\t')

# Ending the program
print("Thanks for using the terminal!")