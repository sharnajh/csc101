# CSC101    Sharna Hossain
# Python Version    Python3
# Chapter   9

# I am importing Python3's random module in order
# to use random.randint() and random.uniform()
# on line 22
import random


# Helper Functions

# This helper function takes a int/float dollar amount
# as a parameter and converts it to a string, and formats it
# into USD format (ex: $100.00) using the format function.
def convertToUSD(amount):
    # I am using Python 3's Literal String Interpolation
    # in order to inject Python code inside of the string.
    return f'${str("{:,.2f}".format(amount))}'


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
        return random.randint(min, max)
    # Checking if desired result is a float
    elif type == "float":
        # Returns a random float using the random module
        return random.uniform(min, max)


# Programs
# Program 1
# output.py
# I am storing the data in a variable to DRY my code
# DRY means 'Don't Repeat Yourself' and it is an
# important principle in software development that
# I learned from the book "The Pragmatic Programmer"
# by Andy Hut & Dave Thomas.
# I implemented commands '\n' in the string to break the string
# into seperate lines when printed.
user_info = 'Kate Austen\n123 Full Circle Drive\nAscheville, NC 28899'
print(user_info)


# Program 2
# double_quotes.py
user_info = "Kate Austen\n123 Full Circle Drive\nAscheville, NC 28899"
print(user_info)


# Program 3
# apostrophe.py
print("Don't fear!\nI'm here!")


# Program 4
# display_quote.py
print('Your assignment is to read "Hamlet" by tomorrow.')


# Program 5
# comment1.py
# This program displays a person's
# name and address.
print(user_info)


# Program 6
# comment2.py
print('Kate Austen')                # Display the name.
print('123 Full Circle Drive')      # Display the address.
print('Ascheville, NC 28899')       # Display the city, state, and ZIP.


# Program 7
# variable_demo.py
# This program demonstrates a variable.
# Executing the randomNum helper function
# in order to generate random numbers
room = randomNum("int", 1, 900)
print(f'I am staying in room number {room}')


# Program 8
# variable_demo2.py
# Create two variables: top_speed and distance.
top_speed = randomNum("int", 100, 900)
distance = randomNum("int", 100, 900)

# Display the values referenced by the variables.
print(f'The top speed is {top_speed}\nThe distance traveled is {distance}')


# Program 9
# variable_demo3.py
# This program demonstrates a variable.
room = randomNum("int", 1, 900)
print(f'I am staying in room number {room}')


# Program 10
# variable_demo4.py
# This program demonstrates veriable reassignment.
# Assign a value to the dollars variable.
dollars = randomNum("float", 2.50, 300)
# Executing the helper function I created convertToUSD()
# inside of the string interpolation to print the value.
print(f'I have {convertToUSD(dollars)} in my account.')

# Reassign dollars so it references
# a different value.
dollars = randomNum("float", 300, 900)
print(f'But now I have {convertToUSD(dollars)} in my account!')


# Program 11
# string_veriable.py
# Create variables to reference two strings.
first_name = 'Kahryn'
last_name = 'Marino'

# Display the values referenced by the variables.
print(f'{first_name} {last_name}')


# Program 12
# string_input.py
# Get the user's first name.
# Added a '\t' command to the string passed to
# the input parameter to create a standard
# spacing for the questions.
first_name = input('Enter your first name:\t')

# Get the user's last name.
last_name = input('Enter your last name:\t')

# Print a greeting to the user.
# Added the 'end' paramater to the print parameter
# to add an exclaimation mark (!) at the end of the
# output and then break into a new line for following
# prints.
print('Hello', first_name, last_name, end="!\n")


# Program 13
# input.py
# Get the user's name, age, and income.
user_name = input('What is your name?\t')
age = int(input('What is your age?\t'))
income = float(input('What is your income?\t'))

# Display the data
print('Here is the data you entered:')
# I implemented the 'sep' parameter to set a delimeter that
# seperates the multiple values with a ': '
print('Name', user_name, sep=": ")
print('Age', age, sep=": ")
print('Income', convertToUSD(income), sep=": ")
