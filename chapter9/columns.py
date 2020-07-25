# CSC 101
# Sharna Hossain
# Program 22 | columns.py

# This program displays the following
# floating-point numbers in a column
# with their decimal points aligned.
# Writing out multiple values and printing each
# one-by-one is an anti-pattern in coding, so I
# am automating it with a dictionary and for loops.

from helper_functions import randomNum

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
# I used another for loop to print all of the var
for i in numbers:
    print(numbers[i])
