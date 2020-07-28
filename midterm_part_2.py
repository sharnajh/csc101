# CSC 101
# Sharna Hossain
# Midterm Part 2

# Storing the following data in constant variables to protect it
# from accidentally mutating, amongst many other benefits
TAX = 0.08875
BUSINESS_NAME = "Jahan Convenience Store"

# First, I will create a class data structure for an item.
class Item():
    # __init__ is the function that when executed
    # will create a new instance of the class with
    # the parameters as the data
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        # calculating subtotal of item
        self.subtotal = float(price * quantity)


# Then, I will create an empty dictionary called shopping_cart to store the
# item objects created from the data that will be received from the user input
shopping_cart = {}

# In the following lines of code, I will greet the customer.
print(f'Thank you for shopping with {BUSINESS_NAME.title()}!')
# Formatted tax value as a percentage.
print(f'Please note that the sales tax is {TAX*100}%.\n')

# Then, I will use a for loop to ask the user to input the data for
# each item. After receiving the data for each item, I will use that
# data to create a new instance of the Item class, and then store it
# into the shopping_cart dictionary.
for i in range(1, 6):
    # Using title to capitalize every word in string
    print(f'\nEnter details for item {i} below')
    name = input("Name:\t").title()
    # Using the f string to interject python into the string
    price = float(input(f'Price:\t'))
    quantity = int(input(f'Quantity:\t'))
    shopping_cart[i] = Item(name,price,quantity)

# Now that we have collected all of the data and stored them nicely
# inside of a dictionary, I will now calculate the grand total by
# looping through the subtotal values of each item stored in the
# dictionary and adding them into a total variable
total = 0
for item in shopping_cart.values():
    total += item.subtotal

# Now I am going to calculate tax to the total and store it into a
# grand_total variable
tax_value = total * TAX
grand_total = total + tax_value

# Because I have a lot of data that I want to be formatted
# in a precise format, I will create a helper function that
# I can use repeatedly and save time from rewriting
# format() over and over again!
# This helper function takes a int/float dollar amount
# as a parameter and converts it to a string, and formats it
# into USD format (ex: $100.00) using the format function.
def convertToUSD(amount):
    # I am using Python 3's Literal String Interpolation
    # in order to inject Python code inside of the string.
    return f'${str("{:,.2f}".format(amount))}'

# I now have collected and calculated all of the data necessary
# for the customer's receipt! It's time to begin.
# Storing line break in a constant variable to resuse.
LINE_BREAK = "===================================="
print(f'\n\t{BUSINESS_NAME}')
print(LINE_BREAK)

# Now, I will loop through the shopping_cart dictionary to
# print the data for each item, as well as it's subtotal.
for item in shopping_cart.values():
    print(f'x{item.quantity} \t{item.name} \t{convertToUSD(item.subtotal)}')

# Now I will print the total, tax, and grandtotal.
print(LINE_BREAK)
print(f'Subtotal:\t\t{convertToUSD(total)}')
print(f'Tax({TAX*100}%):\t\t{convertToUSD(tax_value)}')
print(f'Grand Total:\t\t{convertToUSD(grand_total)}')