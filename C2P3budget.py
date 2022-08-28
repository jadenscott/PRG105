# This program will help the user create a budget

# Variables are created here
# These variables get integers from the user
income = int(input("Enter your monthly net income: "))
housing_expense = int(input("Enter your monthly housing expense: "))
food_expense = int(input("Enter your monthly food expense: "))
transportation_expense = int(input("Enter your monthly transportation expense: "))
phone_expense = int(input("Enter your monthly phone expense: "))
utilities_expense = int(input("Enter your monthly utilities expense: "))
clothing_expense = int(input("Enter your monthly clothing expense: "))

# Additional variables account for each proportion of monthly income
housing_percentage = housing_expense / income
food_percentage = food_expense / income
transportation_percentage = transportation_expense / income
phone_percentage = phone_expense / income
utilities_percentage = utilities_expense / income
clothing_percentage = clothing_expense / income

# This variable calculates the user's leftover income
income_left = income - (housing_expense + food_expense + transportation_expense + phone_expense + utilities_expense + clothing_expense)

# Each expense is divided by income and displayed as a percentage
print(f'\nHousing accounts for {housing_percentage:.2%} of your monthly income')
print(f'Food accounts for {food_percentage:.2%} of your monthly income')
print(f'Transportation accounts for {transportation_percentage:.2%} of your monthly income')
print(f'Phone bills account for {phone_percentage:.2%} of your monthly income')
print(f'Utilities account for {utilities_percentage:.2%} of your monthly income')
print(f'Clothing accounts for {clothing_percentage:.2%} of your monthly income')

# Final print statement tells the user how much of his income is left
print(f'\nYou have ${income_left:,.2f} left after paying for monthly expenses')
