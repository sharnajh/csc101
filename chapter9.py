# CSC101 - Sharna Hossain
# Python Version: Python3
# Chapter: 9

# I am importing Python3's built-in random module in order
# to use random.randint() and random.uniform() on line 30
import random


# Helper Functions

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
def generateInput(var, type, message):
    # globals() allows for dynamic variable names, which means
    # we can declare a variable's name as the value of another variable,
    # which in this case is the var parameter of this function.
    # I read online that dictionaries would be better for dynamic vars.
    globals()[var] = input(f'{message}\t')      # \t to add spacing
    if type == "name":
        # Checks if input is a valid first name by using isalpha()
        # which checks if the string has alphabet characters only.
        # "while" functions are like if/else but they loop the code
        # until the specified condition is finally met.
        # I removed all of the spaces in the input with replace()
        # because isalpha returns false if there are spaces in the
        # string.
        while not globals()[var].replace(" ", "").isalpha():
            print(f'Whoops! "{globals()[var]}" is not a valid name')
            globals()[var] = input(f'{message}\t')
    elif type == "number":
        # isnumeric() is the same as isalpha() but for number values
        while not globals()[var].isnumeric():
            print(f'Whoops! "{globals()[var]}" is not a valid number')
            globals()[var] = input(f'{message}\t')
    else:
        print(f'{type} is not a valid type')


# Programs

# Program 1
# output.py
# I am storing the data in a object to DRY my code
# DRY means 'Don't Repeat Yourself' and it is an
# important principle in software development that
# I learned from the book "The Pragmatic Programmer"
# by Andy Hut & Dave Thomas.
# First I created the class
class Person:
    # __init__ is the function that when executed
    # will create a new instance of the class with
    # the parameters as the data
    def __init__(self, first_name, last_name, address1="", address2=""):
        # Using Python's built-in title() function to format
        # the input values so that the first letter of every word
        # in the string is capitalized and the rest of the chars
        # are lowercase.
        # Strip() removed all whitespace.
        self.first_name = first_name.strip().title()
        self.last_name = last_name.strip().title()
        self.full_name = f'{self.first_name} {self.last_name}'
        self.address1 = address1
        self.address2 = address2


# Then I created an object instance of Person Class with Kate's data
kate = Person("Kate",
              "Austen",
              "123 Full Circle Drive",
              "Ascheville, NC 28899")

# Now I can reference the data in the 'kate' object by it's key name.
# This reduces the chance of typos and structures our data comprehensively.
# I implemented commands '\n' in the string to break the string
# into seperate lines when printed.
kate_info = f'{kate.full_name}\n{kate.address1}\n{kate.address2}'
print(kate_info)


# Program 2
# double_quotes.py
kate_info = f"{kate.full_name}\n{kate.address1}\n{kate.address2}"
print(kate_info)


# Program 3
# apostrophe.py
print("Don't fear!\nI'm here!")


# Program 4
# display_quote.py
# Created an array of different books by Shakespeare.
# Used constant variable for books because I don't want
# the data to mutate at any point.
BOOKS = ["Hamlet",
         "Romeo & Juliet",
         "Macbeth",
         "A Midsummer Night's Dream",
         "Othello"]
# Using the randomNum() function to generate a random
# value from 0 to the max length of the BOOKS array minus
# 1 because the index starts from 0, and then using that
# value as the index to retrieve a random value from the
# BOOKS array.
books_length = (len(BOOKS) - 1)     # len(arr) gets length of array
random_index = randomNum("int", 0, books_length)
random_book = BOOKS[random_index]
# I broke up the pieces into their own variables for legibility
# It would have looked like this otherise:
# >> BOOKS[randomNum("int",0,(len(BOOKS) - 1))]
print(f'Your assignment is to read "{random_book}" by tomorrow.')


# Program 5
# comment1.py
# This program displays a person's
# name and address.
print(kate_info)


# Program 6
# comment2.py
print(kate.full_name)          # Display the name.
print(kate.address1)           # Display the address.
print(kate.address2)           # Display the city, state, and ZIP.


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
# Example of passing a function as a parameter
top_speed = randomNum("int", 100, randomNum("int", 101, 900))
distance = randomNum("int", 100, randomNum("int", 101, 900))

# Display the values referenced by the variables.
print(f'The top speed is {top_speed}\nThe distance traveled is {distance}')


# Program 9
# variable_demo3.py
# This program demonstrates a variable.
# I used a float as a parameter for randomNum()
# to test whether there will be an error by mixing
# types. There was, so I adjusted the randomNum()
# function to convert the parameters to the right
# types before executing rest of the function.
room = randomNum("int", 1.5, 900)
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
# I used (+=) shorthand operand because it is the
# equivalaned of (dollars = dollars + randomNum(x,y,z))
dollars += randomNum("float", 2.50, 300)
print(f'But now I have {convertToUSD(dollars)} in my account!')


# Program 11
# string_veriable.py
# Create variables to reference two strings.
first_name = 'Kahryn'
last_name = 'Marino'

# Create new Person object with Kahryn's data
kahryn = Person(first_name, last_name)

# Display the values referenced by the variables.
# I am referencing them by their object key value pair instead:
print(f'{kahryn.first_name} {kahryn.last_name}')


# Program 12
# string_input.py
# Get the user's first name.
user_first_name = None
generateInput("user_first_name", "name", "Enter your first name:")

# Get the user's last name.
user_last_name = None
generateInput("user_last_name", "name", "Enter your last name:")

# Create new Person object with user's data
user = Person(user_first_name, user_last_name)

# Print a greeting to the user.
# Added the 'end' paramater to the print parameter
# to add an exclaimation mark (!) at the end of the
# output and then break into a new line for following
# prints.
print('Hello', user.first_name, user.last_name, end="!\n")


# Program 13
# input.py
# Get the user's age and income.
generateInput("age", "number", "What is your age?")
user.age = int(globals()["age"])

generateInput("income", "number", "What is your income?")
user.income = float(globals()["income"])

# Display the data
print('Here is the data you entered:')
# I implemented the 'sep' parameter to set a delimeter that
# seperates the multiple values with a ': '
print('Name', user.full_name, sep=": ")
print('Age', user.age, sep=": ")
print('Income', convertToUSD(user.income), sep=": ")


# Program 14
# simple_math.py
# Assign a value to the salary variable.
salary = 2300.0

# Assign a value to the bonus variable.
bonus = 1200.0

# Calculate the total pay by adding salary and bonus.
# Assign the result to pay.
pay = salary + bonus

# Display
print(f'Your pay is {convertToUSD(pay)}')


# Program 15
# sale_price.py
# This program gets an item's original price and
# calculates its sales price, with a 20% discount.
# Get the item's original price.
original_price = float(input("Enter the item's original price:\t"))

# Calculate the amount of the discount.
discount = original_price * .2

# Calculate the sales price.
sale_price = original_price - discount

# Display the sale price.
print(f'The sale price is {convertToUSD(sale_price)}')


# Program 16
# test_score_average.py
# Get three test scores and assign them to the
# test1, test2, and test3 variables.
test1 = float(input('Enter the first test score:\t'))
test2 = float(input('Enter the second test score:\t'))
test3 = float(input('Enter the third test score:\t'))

# Calculate the average of the three scores
# and assign the result to the average score.
average = ((test1 + test2 + test3) / 3.0)

# Display the average
print(f'The average score is {average}%')


# Program 17
# time_converter.py
# I created a time_convert function in order to wrap up
# all of the steps, and it returns a dictionary to give
# the related data a comprehensive grouping
def time_converter(seconds):
    return {
        # Get the number of hours.
        "hours": seconds // 3600,
        # Get the number of remaining minutes.
        "minutes": (seconds // 60) % 60,
        # Get the number of remaining seconds.
        "seconds": seconds % 60
    }

# Get a number of seconds from the user.
total_seconds = float(input('Enter a number of seconds:\t'))

# Execute the function with the total_seconds parameter
time_dict = time_converter(total_seconds)

# Display the results
print('Here is the time in hours, minutes, and seconds:')
print(
    f'Hours:\t{time_dict["hours"]}\n\
    Minutes:\t{time_dict["minutes"]}\n\
    Seconds:\t{time_dict["seconds"]}')


# Program 18
# future_value.py
# Compressing all the steps into a function
def calculate_amount():
    # Get the desired future value.
    future_value = float(input('Enter the desired future value:\t'))
    # Get the annual interest rate.
    rate = float(input('Enter the annual interest rate:\t'))
    # Get the number of years that the money will appreciate
    years = int(input('Enter the number of years the money will grow:\t'))
    # Calculate the amount that needed to deposit and return
    present_value = future_value / (1.0 + rate)**years
    # Display the amount needed to deposit
    return print(f'You will need to deposit this amount: {present_value}')

# Executing function
calculate_amount()


# Program 19
# no_formatting.py
# This demonstrates how a floating-point number is displayed
# with no formatting.
# Creating function to compute the monthly payments determined
# by how much is due
def get_monthly_payment(amount):
    return convertToUSD(amount/12)

amount_due = randomNum('float', 1000, 5000)
monthly_payment = get_monthly_payment(amount_due)
print(f'The monthly payment is {monthly_payment}')


# Program 20
# formatting.py
# This program demonstrates how a floating-point number can be
# formatted.
amount_due = randomNum('float', 1000, 5000)
monthly_payment = get_monthly_payment(amount_due)
print(f'The monthly payment is {monthly_payment}')


# Program 21
# dollar_display.py
# This program demonstrates how a floating-point number can be
# displayed as currency.
amount_due = randomNum('float', 1000, 5000)
monthly_payment = get_monthly_payment(amount_due)
print(f'The monthly payment is {monthly_payment}')


# Program 22
# columns.py
# This program displays the following
# floating-point numbers in a column
# with their decimal points aligned.
# Writing out multiple values and printing each
# one-by-one is an anti-pattern in coding, so I
# am automating it with a dictionary and for loops.
# First, I declared a dictionary called numbers.
numbers = {}

# I used a for loop to generate 6 random numbers
# with variables num(x) as key value-pairs in the
# numbers dictionary.
# Using range() to get t a range of values from 0
# to 6, which is the same as 1-6.
for x in range(0, 6):
    numbers[f'num{x}'] = randomNum('float', 1, 800)

# Display each number in a field of 7 spaces
# with 2 decimal spaces.
# I used another for loop to print all of the va
for i in numbers:
    print(numbers[i])
