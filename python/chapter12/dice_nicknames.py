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
        for x in range(1, 7):
            # Removes the first element from the array
            # and stores it in this value.
            nickname = DICE_NICKS.pop(0)
            # Create key value pair and add it to the
            # dictionary.
            dice_combos[nickname] = [iteration, x]
    return dice_combos


# Output:
# output = {
#     'Snake Eyes': [1, 1],
#     'Australian yo': [1, 2],
#     'Little Joe from Kokomo': [1, 3],
#     'No field five': [1, 4],
#     'Easy 6': [1, 5],
#     "Six one you're done": [1, 6],
#     'Ace caught a deuce': [2, 1],
#     'Ballerina': [2, 2],
#     'The fever': [2, 3],
#     'Jimmie Hicks': [2, 4],
#     'Bennie Blue': [2, 5],
#     'Easy eight!': [2, 6],
#     'Easy four': [3, 1],
#     'Michael Jordan': [3, 2],
#     'Brooklyn Forest': [3, 3],
#     'Big Red': [3, 4],
#     'Eighter from Decatur': [3, 5],
#     'Nina from Pasadena': [3, 6],
#     'Little Pheobe': [4, 1],
#     'Lumber number': [4, 2],
#     'Skinny McKinney': [4, 3],
#     'Square pair': [4, 4],
#     'Railroad nine': [4, 5],
#     'Big one on the end': [4, 6],
#     'Sixie from Dixie': [5, 1],
#     'Skinny Dugan': [5, 2],
#     'Easy eight!!': [5, 3],
#     'Jesse James': [5, 4],
#     'Puppy paws': [5, 5],
#     'Yo': [5, 6],
#     'The Devil': [6, 1],
#     'Easy eight!!!': [6, 2],
#     'Lou Brown': [6, 3],
#     'Tennessee': [6, 4],
#     'Six five no jive': [6, 5],
#     'Midnight': [6, 6]
# }
