# CSC 101
# Sharna Hossain
# Chapter 11 | Program 13
# property_tax.py

# This program displays property taxes.

# For my alteration of property_tax.py, I am using a
# for loop on a string to loop through each character
# and print a psuedo logging off effect. This is to 
# demonstrate that there are many different data types
# that a loop function can loop through.

TAX_FACTOR = 0.0065     # Represents the tax factor.
LOGGING_OFF_MESSAGE = "LOGGING OFF"

# Get the first lot number.
print('Enter the property lot number')
print('or enter 0 to end.')
lot = int(input('Lot number:\t'))

# Continue processing as long as the user
# does not enter lot number 0.
while lot != 0:
    # Get the property value.
    value = float(input('Enter the property value:\t'))

    # Calculate the property's tax.
    tax = value * TAX_FACTOR

    # Display the tax.
    print('Property tax: $', format(tax, ',.2f'), sep='')

    # Get the next lot number.
    print('Enter the next lot number or')
    print('enter 0 to end.')
    lot = int(input('Lot number:\t'))

for char in LOGGING_OFF_MESSAGE:
    print(char)
print("👋")