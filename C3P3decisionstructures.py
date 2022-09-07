"""This program will obtain information such as which group of people the user belongs to and how many tickets the
user would like to buy and return to him the total cost before and after discounts along with the price per ticket"""

# Initial output written here
print("""PRICE PER TICKET FOR PLAY
1. Student $5.00
2. Veteran $7.00
3. Show Sponsor $2.00
4. Retiree $6.00
5. General Public $10.00\n""")

# Variables are declared here
category = int(input("Please enter the number of the category regarding purchasing tickets to which you belong: "))
ticket_quantity = int(input("Please enter the amount of tickets you would like to purchase: "))
user_price = 0
total_cost = 0

# Price per ticket is assigned
if category == 1:
    user_price = 5.00
if category == 2:
    user_price = 7.00
if category == 3:
    user_price = 2.00
if category == 4:
    user_price = 6.00
if category == 5:
    user_price = 10.00

# Gross cost variable created
gross_cost = user_price * ticket_quantity

# Checks for quantity discounts
if ticket_quantity > 15:
    total_cost = gross_cost * .8
elif ticket_quantity > 8:
    total_cost = gross_cost * .85
elif ticket_quantity > 3:
    total_cost = gross_cost * .9
else:
    total_cost = gross_cost

# Total cost before discount
print(f'\nTotal cost before discount, if any, was applied: ${gross_cost:.2f}')

# Total cost after discount
print(f'Total cost after discount, if any, was applied: ${total_cost:.2f}')

# Cost per ticket after discount
print(f'Price per ticket after discount, if any: ${total_cost / ticket_quantity:.2f}')
