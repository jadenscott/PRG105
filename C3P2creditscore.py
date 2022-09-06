# This program gives the user a rating of his credit score

# Variables are declared here
credit_score = int(input("What is your credit score? "))

# Credit score will be returned to the user
print(f'With a credit score of {credit_score}')

# Using elif structure, credit_score will be evaluated
if credit_score >= 720:
    print("You have excellent credit.")
elif credit_score >= 690:
    print("You have good credit.")
elif credit_score >= 630:
    print("You have fair credit.")
else:
    print("You have bad credit.")
