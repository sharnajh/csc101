# CSC 101
# Sharna Hossain
# Program 12 | string_input.py

# In my modification of Program 12, I created a generateInput()
# helper function that returns an input function that checks
# if the value entered is a valid type of either number or name,
# and then storing the values in an instance of the Person class.
# I will also be generating a greeting depending on the time, using
# Python3's built-in datetime module.

# Importing the datetime module
import datetime 

# Using the datetime module, I am getting the current date and time
# according to the computer's clock and storing only the hour in
# military time.
current_hour = datetime.datetime.now().hour

# I am going to calculate whether it is morning, afternoon, evening,
# or night by using the current_hour and logic operators, and returning
# the appropriate salutation.
def getGreeting(hour):
    if hour >= 1 and hour <= 5:
        return "You're sure up early"
    if hour >= 5 and hour <= 11:
        return "Good morning"
    if hour >= 12 and hour <= 17:
        return "Good afternoon"
    if hour >= 18 and hour <= 21:
        return "Good evening"
    if (hour >= 22 and hour <= 24) or hour == 0:
        return "You're sure up late"

greeting = getGreeting(current_hour)

# Importing the generateInput() helper function from
# helper_functions.py and Person class from Person_class.py
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
print(greeting, user.first_name, user.last_name, end="!\n")

