# CSC 101
# Sharna Hossain
# Chapter 12 | Program 28
# geometry.py

# This program allows the user to choose various
# geometry calculations from a menu. This program
# imports the circle and rectangle modules.

# For my modification of geometry.py, I am modularizing
# repeated code into functions that can be reused.

import circle
import rectangle

# Constants for the menu choices
AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5

# The main function
def main():
    # The choice variable controls the loop
    # and holds the user's menu choice.
    choice = 0

    while choice != QUIT_CHOICE:
        # displays the menu.
        display_menu()

        # Get the user's choice.
        choice = int(input('Enter your choice:\t'))

        # Perform the selected action.
        if choice == AREA_CIRCLE_CHOICE:
            radius = get_radius()
            print(f'The area is {circle.area(radius)}')

        elif choice == CIRCUMFERENCE_CHOICE:
            radius = get_radius()
            print(f'The circumfrence is {circle.circumference(radius)}')

        elif choice == AREA_RECTANGLE_CHOICE:
            dimensions = get_rectangle_dimensions()
            # Calculating the result with the dimensions dictionary
            res = rectangle.area(dimensions["width"],dimensions["length"])
            print(f'The area is {res}')

        elif choice == PERIMETER_RECTANGLE_CHOICE:
            dimensions = get_rectangle_dimensions()
            # Calculating the result with the dimensions dictionary
            res = rectangle.perimeter(dimensions["width"],dimensions["length"])
            print(f'The perimeter is {res}')

        elif choice == QUIT_CHOICE:
            print('Exiting the program...')

        else:
            print('Error: invalid selection')

# The display_menu function displays a menu.
def display_menu():
    print("MENU")
    print("1) Area of a circle")
    print("2) Circumfrence of a circle")
    print("3) Area of a rectangle")
    print("4) Perimeter of a rectangle")
    print("5) Quit")

# Modularizing code

def get_radius():
    return float(input("Enter the circle's radius:\t"))

def get_rectangle_dimensions():
    # Creating empty dictionary to store dimensions
    dimensions = {}
    # Storing the inputs as values in the dictionary
    dimensions["width"] = float(input("Enter the rectangle's width:\t"))
    dimensions["length"] = float(input("Enter the rectangle's length:\t"))
    return dimensions

# Call the main function.
main()