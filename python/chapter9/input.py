# CSC 101
# Sharna Hossain
# Program 13 | input.py

# In my modification of Program 13, I am using the
# generateInput() helper function to create input()s
# that check for the correct data type, store the
# return in a variable and add it to an instance of a
# person class, and then formats the print() with the
# 'sep argument'

# Importing generateInput() from helper_functions
from helper_functions import generateInput, convertToUSD
from Person_class import Person

# Get the user's age and income.
first_name = generateInput("name", "What is your first name?")
last_name = generateInput("name", "What is your last name?")
age = generateInput("number", "What is your age?")
income = float(generateInput("number", "What is your income?"))

# Create new instance of Person class
user = Person(first_name, last_name)

# Adding other data to the user instance
user.age = age
user.income = income

# Display the data
print('Here is the data you entered:')
# I implemented the 'sep' parameter to set a delimeter that
# seperates the multiple values with a ': '
print('Name', user.full_name, sep=": ")
print('Age', user.age, sep=": ")
print('Income', convertToUSD(user.income), sep=": ")
