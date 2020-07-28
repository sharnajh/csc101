# CSC 101
# Sharna Hossain
# Person Class

# First, I am creating the Person class.
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
