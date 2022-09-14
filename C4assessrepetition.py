"""This program will take the user's current age, age at which he would like to retire, annual income, percent of income
saved, and amount of total savings and return to him a chart with his projected income, savings contributions, and total
savings over the next fifteen years"""

# Variables are declared here
current_age = int(input("What is your current age, in years?: "))
retire_age = int(input("At which age would you like to retire?: "))
annual_income = int(input("What is your current annual income, in dollars?: "))
percent_income = int(input("What percent of your income do you save?: "))
total_savings = int(input("What is your total amount saved, in dollars?: "))

difference = (retire_age - current_age) + 1

savings_contr = annual_income * (percent_income / 100)

# Small disclosure and table headings are printed
print("This projection assumes a 3% annual raise and a 6% annual return on investment.")
print(f'{"Year":10}{"Income":10}{"Savings Contribution":10}\t{"Total Savings":10}')

# Year 1 data is printed
print(f'1\t\t{annual_income:,.2f}\t\t{savings_contr:,.2f}\t\t\t{total_savings + savings_contr + (total_savings * .06):10,.2f}')

# For loop accounts for an annual 3% raise, adjusted savings contribution, and a 6% return on investment for total savings
for year in range(2, difference):
    annual_income += annual_income * .03
    savings_contr = annual_income * (percent_income / 100)
    total_savings += savings_contr + (total_savings * .06)
    print(f'{year}\t\t{annual_income:,.2f}\t\t{savings_contr:,.2f}\t\t\t{total_savings:,.2f}')
