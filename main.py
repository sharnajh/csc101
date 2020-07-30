# This program determines whether a bank customer
# qualifies for a loan.

MIN_SALARY = 30000.0        # The minimum salary
MIN_YEARS = 2               # The minimum years on the job

# Get the customer's annual salary.
salary = float(input('Enter your annual salary:\t'))

# Get the number of years on the current job.
years_on_job = int(input(f'Enter the number of years employed:\t'))

# Determines whether the customer qualifies
if salary >= MIN_SALARY and years_on_job >= MIN_YEARS:
    print('Your qualify for a loan!')
else:
    print("You don't qualify for a loan.")

