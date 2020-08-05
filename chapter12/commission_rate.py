# CSC 101
# Sharna Hossain
# Chapter 12 | Program 23
# commission_rate.py

# This program calculates a salesperson's pay
# at Make Your Own Music.

# In my modification of commission_rate.py, I have
# modulated the functions and am importing them from
# a seperate file.

import commissions

def main():
    # Get the amount of sales.
    sales = commissions.get_sales()

    # Get the amount of advanced pay.
    advanced_pay = commissions.get_advanced_pay()

    # Determine the commission rate.
    comm_rate = commissions.determine_comm_rate(sales)

    # Calculate the pay.
    pay = sales * comm_rate - advanced_pay

    # Display the amount of pay.
    print(f'The pay is ${format(pay, ",.2f")}')

    # Determine whether the pay is negative.
    if pay < 0:
        print('The Salesperson must reimburse')
        print('the company.')

# Execute main function.
main()