"""
This program will have the user enter an integer between 20 and 100, validate the integer, and check if it is divisible
by two, three, and five, respectively.
"""


# main function is defined
def main():
    user_number = int(input("Enter a whole number between 20 and 100: "))
    good_number = validate(user_number)


# validate functions ensures user_number is between 20 and 100
def validate(num):
    while not (num >= 20) or not (num <= 100):
        print("That is not a valid value.")
        num = int(input("Enter a whole number between 20 and 100: "))
    return num


def divisible_by_two(num):
    two = True
    if (num % 2) != 0:
        two = False
    return two


main()



