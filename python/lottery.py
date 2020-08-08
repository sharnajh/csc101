# CSC 101
# Sharna Hossain
# Chapter 12

# I have created a lottery script that takes in
# an input value of one of the following types of lotteries:
# Pick 5, Lotto, Pick 10, and Mega Pick. Each type of
# lottery will execute a function that generates a random
# number constricted to the limitations of each type of lottery.

# The code makes use of several principles learned in Chapter 12,
# such as modularizing code into functions, global/local vars,
# void functions, and the random module.

# Importing the random module to generate random integers
import random

# Global variables
lottery_numbers = []
# List of the different lottery types
LOTTERY_TYPES = [
    "Pick 5",
    "Lotto",
    "Pick 10",
    "Mega Pick"
]


def main():
    # Get input and store into local var
    selected_type = get_input()

    # Start generating lottery numbers
    print(f"You are playing '{selected_type}'!")
    # Execute the selected lottery type
    if selected_type == "Pick 5":
        pick_five()
    elif selected_type == "Lotto":
        lotto()
    elif selected_type == "Pick 10":
        pick_ten()
    elif selected_type == "Mega Pick":
        mega_pick()

    # Printing the generated lottery number
    print_lotto_numbers()

# Defining the functions for ea/ lottery type


def pick_five():
    # Based on Pennsylvania's Lottery Pick 5
    for count in range(5):
        lottery_numbers.append(random.randint(1, 9))


def lotto():
    # Based on NY Lottery
    for count in range(6):
        lottery_numbers.append(random.randint(1, 100))


def pick_ten():
    # Based on Pennsylvania's Lottery Pick 10
    for count in range(10):
        lottery_numbers.append(random.randint(1, 100))


def mega_pick():
    # Based on the 'Mega Millions' lottery
    for count in range(5):
        # White balls
        lottery_numbers.append(random.randint(1, 70))
    # Gold ball
    lottery_numbers.append(random.randint(1, 25))

# Printing lottery number


def print_lotto_numbers():
    print("Lottery numbers:\t", end="")
    # Formats list of lottery numbers.
    for x in lottery_numbers:
        print(x, end=" ")
    # Ends script
    print("\nThanks for playing!")

# Get the input


def get_input():
    print("Available lottery types:")
    # Print each available lottery type
    for x in LOTTERY_TYPES:
        print(f'- {x}')
    # Assign new value to global var
    selected_type = input(f'Select lottery type:\t')
    # Error handling
    while not selected_type in LOTTERY_TYPES:
        print("ERROR: Invalid lotto type.")
        selected_type = input(f'Reselect lottery type:\t')
    # Return value and end function
    return selected_type


# Executing main function
main()
