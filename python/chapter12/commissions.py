# CSC 101
# Sharna Hossain
# Chapter 12 | Program 23 + module
# module for commission_rate.py

# The get_sales function gets a salesperson's
# monthly sales from the user and returns that value.
def get_sales():
    # Get the amount of monthly sales.
    monthly_sales = float(input('Enter the monthly sales:\t'))

    # Return the amount entered.
    return monthly_sales


# The get_advanced_pay function gets the amount of
# advanced pay given to the salesperson and returns
# that amount.
def get_advanced_pay():
    # Get the amount of advanced pay.
    print('Enter the amount of advanced pay, or')
    print('end 0 if no advanced pay was given.')
    advanced = float(input('Advanced pay:\t'))

    # Return the amount entered
    return advanced


# The determine_comm_rate function accepts the
# amount of sales as an argument and returns the
# applicable commission rate.
def determine_comm_rate(sales):
    # Determine the commission rate.
    if sales < 10000.00:
        rate = 0.10
    elif sales >= 10000 and sales <= 14999.99:
        rate = 0.12
    elif sales >= 15000 and sales <= 17999.99:
        rate = 0.14
    elif sales >= 18000 and sales <= 21999.99:
        rate = 0.16
    else:
        rate = 0.18

    # Return the commission rate.
    return rate