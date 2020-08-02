# CSC 101
# Sharna Hossain
# Chapter 11 | Program 2
# temperature.py

# This program assists a technician in the process
# of checking a substance's temperature

# For my alteration of temperature.py, I am storing
# the lengthy error message into a list, breaking them
# up by how I want each to be seperated in their own
# line, and then inside of the while loop I use a for
# loop to loop through the error_instructions list and
# print each item.
# This helps with modularity in the event that I want
# to show this error message elsewhere in my code.

# Named constant to represent the maximum
# temperature.
MAX_TEMP = 102.5

# Get the substance's temperature.
temperature = float(input("Enter the substance's Celsius temperature:\t"))

# Storing error instructions into a list
error_instructions = [
    'The temperature is too high.',
    'Turn the thermostat down and wait',
    '5 minutes. Then take the temperature',
    'again and enter it.'
]

# As long as necessary, instruct the user to
# adjust the thermostat.
while temperature > MAX_TEMP:
    # Looping through error instructions to print each chronologically
    for line in error_instructions:
        print(line)
        
    temperature = float(input("Enter the new Celsius temperature:\t"))

# Remind the user to check the temperature again
# in 15 minutes.
print('The temperature is acceptable.')
print('Check it again in 15 minutes.')