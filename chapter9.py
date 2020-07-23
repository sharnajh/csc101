# CSC101    Sharna Hossain
# Python Version    Python3
# Chapter   9

# Program 1
# output.py
print('Kate Austen')
print('123 Full Circle Drive')
print('Ascheville, NC 28899')


# Program 2
# double_quotes.py
print("Kate Austen")
print("123 Full Circle Drive")
print("Ascheville, NC 28899")


# Program 3
# apostrophe.py
print("Don't fear!")
print("I'm here!")


# Program 4
# display_quote.py
print('Your assignment is to read "Hamlet" by tomorrow.')


# Program 5
# comment1.py
# This program displays a person's
# name and address.
print('Kate Austen') 
print('123 Full Circle Drive')
print('Ascheville, NC 28899')


# Program 6
# comment2.py
print('Kate Austen')                # Display the name.
print('123 Full Circle Drive')      # Display the address.
print('Ascheville, NC 28899')       # Display the city, state, and ZIP.


# Program 7
# variable_demo.py
# This program demonstrates a variable.
room = 503
print('I am staying in room number')
print(room)


# Program 8
# variable_demo2.py
# Create two variables: top_speed and distance.
top_speed = 160
distance = 300

#Display the values referenced by the variables.
print('The top speed is')
print(top_speed)
print('The distance traveled is')
print(distance)


# Program 9
# variable_demo3.py
# This program demonstrates a variable.
room = 503
print('I am staying in room number', room)


# Program 10
# variable_demo4.py
# This program demonstrated veriable reassignment.
# Assign a value to the dollars variable.
dollars = 2.75
print('I have', dollars, 'in my account.')

# Reassign dollars so it references
# a different value.
dollars = 99.95
print('But now I have', dollars, 'in my account!')


# Program 11
# string_veriable.py
# Create variables to reference two strings.
first_name = 'Kathryn'
last_name = 'Marino'

# Display the values referenced by the variables.
print(first_name, last_name)


# Program 12
# string_input.py
# Get the user's first name.
first_name = input('Enter your first name: ')

# Get the user's last name.
last_name = input('Enter your last name: ')

# Print a greeting to the user.
print('Hello', first_name, last_name)


# Program 13
# input.py
# Get the user's name, age, and income.
user_name = input('What is your name? ')
age = int(input('What is your age? '))
income = float(input('What is your income? '))

# Display the data
print('Here is the data you entered:')
# I implemented the sep parameter to set a delimeter that
# seperates the multiple values with a ': ' 
print('Name', user_name, sep=": ")
print('Age', age, sep=": ")
print('Income', ('$' + str(income)), sep=": ")
