"""This program will ask the user to enter the amount of sales for each day of the week, compute the total and average
sales, and return that information to the user"""

# Variables are initialized here
total_sales = 0
sales = 0

# For loop is used to repeat the request for the amount of sales for each day of the week
for day in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]:
    sales = int(input(f'Enter the total sales for {day}: '))
    total_sales = total_sales + sales

# Displays the total weekly sales and the average daily sales
print(f'The total weekly sales were: ${total_sales:,.2f}')
print(f'The average daily sales were: ${total_sales / 7:,.2f}')
