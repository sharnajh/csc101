# CSC 101
# Sharna Hossain
# Program 16 | test_score_average.py

# In my modification of Program 16, I am storing the
# test scores in a dictionary, and looping through them
# in a function to return an average score.

# Get three test scores and assign them to the
# test1, test2, and test3 variables.
test1 = float(input('Enter the first test score:\t'))
test2 = float(input('Enter the second test score:\t'))
test3 = float(input('Enter the third test score:\t'))

# I am storing all of the values received from the input()s
# into a dictionary
test_scores = {
    test1,
    test2,
    test3,
}
# Calculate the average of the three scores
# and assign the result to the average score.
# I have created an average function.
def average(scores):
    total = 0
    # Looping through the scores data with for loop
    for score in scores:
        # Adding the total test scores together
        total += score
        # Dividing the total by the length of dictionary
    return total / len(scores)

# Storing the return of average()
average_test_scores = average(test_scores)

# Display the average
print(f'The average score is {average_test_scores}%')