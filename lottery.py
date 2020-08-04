# CSC 101
# Sharna Hossain
# Chapter 12

# I have created a "main" Python function that takes in
# an input value of one of the following types of lotteries:
# Pick 5, Lotto, Pick 10, and Mega Pick. Each type of
# lottery will execute a function that takes in the user's
# 'play,' and then generates a random number constricted to
# the limitations of each type of lottery. The script will
# then check if the user won the lottery or not.

# Importing the random module to generate random integers
import random

# List of the different lottery types
LOTTERY_TYPES = [
    "Pick 5",
    "Lotto",
    "Pick 10",
    "Mega Pick"
]

# Global variable
lottery_numbers = []
selected_type = ""


def main():

    # Prompting user input
    print("Available lottery types:")
    for x in LOTTERY_TYPES:
        print(f'- {x}')
    while not selected_type in LOTTERY_TYPES:
        selected_type = input(f'Select lottery type:\t')

    # Execute the selected lottery type
    if selected_type == "Pick 5":
        pick_five()
    if selected_type == "Lotto":
        lotto()
    if selected_type == "Pick 10":
        pick_ten()
    if selected_type == "Mega Pick":
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
    for x in lottery_numbers:
        print(x, end=" ")
    print("\nThanks for playing!")


main()
