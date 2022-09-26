"""
This program will have the user enter an integer between 20 and 100, validate the integer, and check if it is divisible
by two, three, and five, respectively.
"""


# main function gets user input and calls other functions
def main():
    user_number = int(input("Enter a whole number between 20 and 100: "))
    good_number = validate(user_number)  # validated number is stored as a variable
    divisible_by_two(good_number)
    divisible_by_three(good_number)
    divisible_by_five(good_number)


# validate function ensures user_number is between 20 and 100 and then returns it to the main function
def validate(num):
    while not (num >= 20) or not (num <= 100):
        print("That is not a valid value.")
        num = int(input("Enter a whole number between 20 and 100: "))
    return num


# the three functions below determine if good_number is divisible or not by two, three, and five
def divisible_by_two(num):
    if (num % 2) == 0:
        print(f"{num} is divisible by two.")
    else:
        print(f"{num} is not divisible by two.")


def divisible_by_three(num):
    if (num % 3) == 0:
        print(f"{num} is divisible by three.")
    else:
        print(f"{num} is not divisible by three.")


def divisible_by_five(num):
    if (num % 5) == 0:
        print(f"{num} is divisible by five.")
    else:
        print(f"{num} is not divisible by five.")


main()  # finally, the main function is called
