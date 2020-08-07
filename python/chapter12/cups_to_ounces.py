# CSC 101
# Sharna Hossain
# Chapter 12 | Program 7
# cups_to_ounces.py

# This program converts cups to fluid ounces.

# In my modification of cupes_to_ounces.py, I will
# be adding the numerous conversions of cups to other
# measurements, such as pints and litres, using
# Python dictionary.

def main():
    # display the intro screen.
    intro()
    # Get the number of cups.
    cups_needed = int(input('Enter the number of cups:\t'))
    # Convert the cups to ounces.
    convert_cups(cups_needed)

# Dictionary that contains different measurement types and
# the respective multiplicand that converts cups to that type
CUP_CONVERSIONS = {
    "ounce": 8,
    "pint": (1/2),
    "gallon": (1/16),
    "mililiter": 237,
    "quart": (1/4),
    "teaspoon": 48,
    "tablespoon": 16,
    "liter": (1/4.227)
}

# The intro function displays an introductory screen.
def intro():
    # Unzipping the lengthy introduction message into
    # shorter strings and storing them in an array.
    intro_string = [
        "This program converts measurements",
        "in cups to other measurements. For",
        "your reference, the formulas are:"
    ]
    # Looping through CUP_CONVERSIONS to print
    # formulas.
    for measurement, multiplicand in CUP_CONVERSIONS.items():
        # Pluralize measurement or not
        if multiplicand > 1:
            measurement += "s"
        intro_string.append(f'1 cup = {multiplicand} {measurement}')
    # Looping over the above array to print each sentence.
    for sentence in intro_string:
        print(sentence)

# The cups_to_ounces function accepts a number of
# cups and displays the equivalent number in several
# different measurements, as described in the 
# CUP_CONVERSIONS dictionary.
def convert_cups(cups):
    print(f'{cups} cups converts to:')
    for measurement, multiplicand in CUP_CONVERSIONS.items():
        # Converts the cups
        res = cups * multiplicand
        # Pluralize measurement or not
        if res > 1:
            measurement += "s"
        print(f'{res} {measurement}')

# Call the main function.
main()