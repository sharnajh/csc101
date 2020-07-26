# CSC 101
# Sharna Hossain
# Program 4 | output.py

# In my modification of Program 4, I have created an array
# of books by Shakespeare and will have the program print
# a random value from the array.

# Importing randomNum() from helper_functions.py
from helper_functions import randomNum

# I am storing the different possible Shakespeare books in
# an array with a constant variable, as I do not intend for
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

# I am using Python 3's Literal String Interpolation
# in order to inject Python code inside of the string.
print(f'Your assignment is to read "{random_book}" by tomorrow.')