# CSC 101
# Sharna Hossain
# Chapter 12 | Program 7
# cups_to_ounces.py

# This program converts cups to fluid ounces.

def main():
    # display the intro screen.
    intro()
    # Get the number of cups.
    cups_needed = int(input('Enter the number of cups:\t'))
    # Convert the cups to ounces.
    cups_to_ounces(cups_needed)

# The intro function displays an introductory screen.
def intro():
    # Unzipping the lengthy introduction message into
    # shorter strings and storing them in an array.
    intro_string = [
        "This program converts measurements",
        "in cups to fluid ounces. For your",
        "reference the formula is:",
        "1 cup = 8 fluid ounces\n"
    ]
    # Looping over the above array to print each
    # sentence.
    for sentence in intro_string:
        print(sentence)

# The cups_to_ounces function accepts a number of
# cups and displays the equivalent number of ounces.
def cups_to_ounces(cups):
    ounces = cups * 8
    # Using f-string to inject python into string.
    print(f'That converts to {ounces} ounces.')

# Call the main function.
main()