# CSC 101
# Sharna Hossain
# Chapter 10
# grader.py

# This program gets a numeric test score from the
# user and displays the corresponding letter grade.

# Storing score thresholds into a dictionary
SCORES = {
    "A": 90,
    "B": 80,
    "C": 70,
    "D": 60
}

# Get a test score from the user.
score = int(input('Enter your test score:\t'))

# Determine the grade.
# I am combining if-elif-else structure and loop
# function to check for the score.
# letter represents the key value and threshold
# represents the value.
for letter, threshold in SCORES.items():
    if score >= threshold:
        print(f"Your grade is {letter}.")
        # Break so that the function ends if this
        # is true, so that the computer doesn't
        # have to unnecesarrily loop through the
        # rest of the values.
        break
    # Checks if grade is F.
    elif score < SCORES["D"]:
        print("Your grade is F.")
        break

