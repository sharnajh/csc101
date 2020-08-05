# CSC 101
# Sharna Hossain
# Chapter 12 | Program 19
# dice.py

# This program simulates the rolling of dice.
# Depending on the values of each simulated dice
# roll, my modified version of dice.py will return
# a special nickname for that roll. Nicknames are
# based off of this chart:
# https://vitalvegas.com/colorful-nicknames-dice-combinations-craps/

import random

# Contants for the minimum and maximum random numbers
MIN = 1
MAX = 6

def main():
    # Stores the nickname and value pairs in
    # a local var
    dice_combos = set_dice_combo_pairs()
    # Create a variable to control the loop.
    again = 'y'
    # Simulate rolling the dice.
    while again == 'y' or again == 'Y':
        # Created empty array to push dice values into
        dice_pair = []
        # Generating two rolls and pushing them into the
        # dice_pair array
        for x in range(2):
            dice_pair.append(random.randint(MIN,MAX))
        
        # Looping through the dice_combos dictionary to
        # determine the combo name for the combo the cpu
        # has randomized.
        for nickname,pair in dice_combos.items():
            if dice_pair == pair or dice_pair == reversed(pair):
                combo_name = nickname
        print('Rolling the dice...')
        print('Their values are: ')
        print(f'{dice_pair[0]} and {dice_pair[1]}')
        print(f'{combo_name}!')

        # Do another roll of the dice?
        again = input('Roll them again? (y = yes):\t')

# I have created an array of all the nicknames in their ascending order.
# Because manually typing in their dice combinations as well would be very
# time consuming, I devised a function that will automate that in the lines
# below.
DICE_NICKS = [
    "Snake Eyes",
    "Australian yo",
    "Little Joe from Kokomo",
    "No field five",
    "Easy 6",
    "Six one you're done",
    "Ace caught a deuce",
    "Ballerina",
    "The fever",
    "Jimmie Hicks",
    "Bennie Blue",
    "Easy eight",
    "Easy four",
    "Michael Jordan",
    "Brooklyn Forest",
    "Big Red",
    "Eighter from Decatur",
    "Nina from Pasadena",
    "Little Pheobe",
    "Lumber number",
    "Skinny McKinney",
    "Square pair",
    "Railroad nine",
    "Big one on the end",
    "Sixie from Dixie",
    "Skinny Dugan",
    "Easy eight",
    "Jesse James",
    "Puppy paws",
    "Yo",
    "The Devil",
    "Easy eight",
    "Lou Brown",
    "Tennessee",
    "Six five no jive",
    "Midnight"
]

# Automates the dice combo pairs and stores
# them in a dictionary with the appropriate
# nickname as the key.
def set_dice_combo_pairs():
    dice_combos = {}
    # Keeps track of how many times the function has
    # looped and doubles as a dice value for each pair.
    iteration = 0
    while iteration < 6:
        # Add to the accumulator
        iteration += 1
        # So that x = 1-6 through the whole loop.
        for x in range(1,7):
            # Removes the first element from the array
            # and stores it in this value.
            nickname = DICE_NICKS.pop(0)
            # Create key value pair and add it to the
            # dictionary.
            dice_combos[nickname] = [iteration,x]
    return dice_combos

# Call the main function.
main()