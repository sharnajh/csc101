# CSC 101
# Sharna Hossain
# Chapter 12 | Program 19 + module
# Module for dice.py

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
    "Easy eight!",
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
    "Easy eight!!",
    "Jesse James",
    "Puppy paws",
    "Yo",
    "The Devil",
    "Easy eight!!!",
    "Lou Brown",
    "Tennessee",
    "Six five no jive",
    "Midnight"
]

# Automates the dice combo pairs and stores
# them in a dictionary with the appropriate
# nickname as the key.
def combo_pairs():
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