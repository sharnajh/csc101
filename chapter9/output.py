# CSC 101
# Sharna Hossain
# Chapter 9
# Program 1 | output.py

# In my modification of Program 1, I am using Class/Object
# data structures to create a 'Person' Class with an instance
# with 'Kate Austen's' data from the textbook.

# I am importing the Person class from Person_class.py
from Person_class import Person

# Then I created an object instance of Person Class with Kate's data
kate = Person("Kate",
              "Austen",
              "123 Full Circle Drive",
              "Ascheville, NC 28899")

# Now I can reference the data in the 'kate' object by it's key name.
# This reduces the chance of typos and structures our data comprehensively.
# I am using Python 3's Literal String Interpolation
# in order to inject Python code inside of the string.
# I also implemented commands '\n' in the string to break the string
# into seperate lines when printed.
kate_info = f'{kate.full_name}\n{kate.address1}\n{kate.address2}'

print(kate_info)