# CSC 101
# Sharna Hossain
# Program 17 | time_converter.py

# In my modification of Program 17, I have created a time_converter 
# that returns a dictionary to give
# the related data a comprehensive grouping

def time_converter(seconds):
    return {
        # Get the number of hours.
        "hours": seconds // 3600,
        # Get the number of remaining minutes.
        "minutes": (seconds // 60) % 60,
        # Get the number of remaining seconds.
        "seconds": seconds % 60
    }

# Get a number of seconds from the user.
total_seconds = float(input('Enter a number of seconds:\t'))

# Store the return of the time_converter function in a var
time_dict = time_converter(total_seconds)

# Display the results
print('Here is the time in hours, minutes, and seconds:')
print(
    f'Hours:\t{time_dict["hours"]}\nMinutes:\t{time_dict["minutes"]}\nSeconds:\t{time_dict["seconds"]}')