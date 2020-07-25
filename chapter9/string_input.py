# CSC 101
# Sharna Hossain
# Program 12 | string_input.py

# In my modification of Program 12, I created a generateInput()
# helper function that returns an input function that checks
# if the value entered is a valid type of either number or name,
# and then storing the values in an instance of the Person class.

# Importing the generateInput() helper function from
# helper_functions.py

from helper_functions import generateInput
from Person_class import Person

# I am using the generateInput() helper function to 
# receive the inputs, check if they're the right data types,
# and store them in variables.
# Get the user's first name.
user_first_name = generateInput("name", "Enter your first name:")

# Get the user's last name.
user_last_name = generateInput("name", "Enter your last name:")

# Create new Person object with user's data
user = Person(user_first_name, user_last_name)

# Print a greeting to the user.
# Added the 'end' paramater to the print parameter
# to add an exclaimation mark (!) at the end of the
# output and then break into a new line for following
# prints.
print('Hello', user.first_name, user.last_name, end="!\n")

