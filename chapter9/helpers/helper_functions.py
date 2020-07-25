# CSC 101
# Sharna Hossain
# Helper Functions

# I have created several helper functions in order
# to import and use them across all of my programs.
# This is an effort to DRY my code.
# DRY means "Don't Repeat Yourself", and it is a 
# programming principle that I learned from the book
# "The Pragamatic Programmer" by Andy Hunt.
# By doing this, I have saved coding time that would
# have been wasted rewriting the same function in 
# several files.

# I am importing Python3's built-in random module in order
# to use random.randint() and random.uniform()
import random

# This helper function takes a int/float dollar amount
# as a parameter and converts it to a string, and formats it
# into USD format (ex: $100.00) using the format function.
def convertToUSD(amount):
    # I am using Python 3's Literal String Interpolation
    # in order to inject Python code inside of the string.
    return f'${str("{:,.2f}".format(amount))}'
    # An alternative method is to use Python3's locale
    # module to use the locale.currency() function that
    # formats money amount to the local computer's region.
    # >> import locale
    # >> # Checks the locale environment's region
    # >> locale.setlocale(locale.LC_ALL,'')
    # >> # Call locale.currency(amount) function to format amount
    # >> # 'grouping=True' parameter formats the amount with commas
    # >> locale.currency(amount_var, grouping=True )


# This helper function takes a type, minimum_value, and
# a maximum_value as the parameters and returns
# a random integer or float (depending on the type param)
# from that range.
def randomNum(type, min, max):
    # I am using if/elif logic statements to check what
    # the value of the type parameter is in order to determine
    # which part of the code should be executed to get the
    # desired result.
    # Checking if desired result is an integer
    if type == "int":
        # Returns a random integer using the random module
        return random.randint(int(min), int(max))
    # Checking if desired result is a float
    elif type == "float":
        # Returns a random float using the random module
        return random.uniform(float(min), float(max))
    else:
        # 'else' error catches in case 'type' isn't valid input
        # Using the multi-line break symbol '\' for brevity
        print(f'{type} is not a valid type.')
        # return 0 as a default
        return 0


# Decided to create a function to generate inputs because it would be
# repetitive to hardcode this standard functionality every time.
def generateInput(type, message):
    value = input(f'{message}\t')      # \t to add spacing
    if type == "name":
        # Checks if input is a valid first name by using isalpha()
        # which checks if the string has alphabet characters only.
        # "while" functions are like if/else but they loop the code
        # until the specified condition is finally met.
        # I removed all of the spaces in the input with replace()
        # because isalpha returns false if there are spaces in the
        # string.
        while not value.replace(" ", "").isalpha():
            print(f'Whoops! "{value}" is not a valid name')
            value = input(f'{message}\t')
        return value
    elif type == "number":
        # isnumeric() is the same as isalpha() but for number values
        while not value.isnumeric():
            print(f'Whoops! "{value}" is not a valid number')
            value = input(f'{message}\t')
        return value
    else:
        print(f'{type} is not a valid type')