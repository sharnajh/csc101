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

# Modulated code that generates the nickname - combos pairs
# in dice_nicknames.py and importing it into dice.py
import dice_nicknames

# Contants for the minimum and maximum random numbers
MIN = 1
MAX = 6

def main():
    # Stores the nickname and value pairs in
    # a local var
    dice_combos = dice_nicknames.combo_pairs()
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
            if dice_pair == pair:
                combo_name = nickname

        # Displaying dice roll
        print('Rolling the dice...')
        print('Their values are: ')
        print(f'{dice_pair[0]} and {dice_pair[1]}')
        print(f'"{combo_name}!"')

        # Do another roll of the dice?
        again = input('Roll them again? (y = yes):\t')

# Call the main function.
main()