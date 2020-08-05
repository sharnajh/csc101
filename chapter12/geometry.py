# CSC 101
# Sharna Hossain
# Chapter 12 | Program 28
# geometry.py

# This program allows the user to choose various
# geometry calculations from a menu. This program
# imports the circle and rectangle modules.
import circle
import rectangle

# Constants for the menu choices
AREA_CIRCLE_CHOICE = 1
CIRCUMFRENCE_CHOICE = 2
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
            radius = float(input("Enter the circle's radius:\t"))
            print(f'The area is {circle.area(radius)}')

        elif choice == CIRCUMFRENCE_CHOICE:
            radius = float(input("Enter the circle's radius:\t"))
            print(f'The circumfrence is {circle.circumfrence(radius)}')

        elif choice == AREA_RECTANGLE_CHOICE:
            width = float(input("Enter the rectangle's width:\t"))
            length = float(input("Enter the rectangle's length:\t"))
            print(f'The area is {rectangle.area(width,length)}')

        elif choice == PERIMETER_RECTANGLE_CHOICE:
            width = float(input("Enter the rectangle's width:\t"))
            length = float(input("Enter the rectangle's length:\t"))
            print(f'The perimeter is {rectangle.perimeter(width,length)}')

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

# Call the main function.
main()