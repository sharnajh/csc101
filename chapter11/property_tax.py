# CSC 101
# Sharna Hossain
# Chapter 11 | Program 13
# property_tax.py

# This program displays property taxes.

# For my alteration of property_tax.py, I am use a
# for loop with the range function to produce a 
# logging off screen effect at the end of the program.

TAX_FACTOR = 0.0065     # Represents the tax factor.

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

# Runs when lot == 0
print("Logging off")
# Empty accumulator
message = ""
# Enacting a loop function that iterates 5 times
for x in range(5):
    # Each iteration adds a "." to the message var
    message += "."
    print(message)
print("Logged off! Bye bye!")