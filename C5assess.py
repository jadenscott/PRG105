"""
This program will allow the user to get the area of the shape his choice after giving the program the dimensions in
centimeters
"""

PI = 3.14159265358  # global variable for pi is declared


def main():
    menu()  # initially, shape options are printed
    user_num = int(input("Please enter the number of your selection: "))
    validate(user_num)  # to ensure that user_num is an integer between 1 and 5
    while user_num != 5:  # as long as the user does not quit the program, he will be repeatedly asked to select shapes
        if user_num == 1:
            base = int(input("Enter the base of the rectangle in cm: "))
            height = int(input("Enter the height of the rectangle in cm: "))
            rectangle(base, height)
            user_num = int(input("Please enter the number of your selection: "))
            validate(user_num)
        if user_num == 2:
            base = int(input("Enter the base of the triangle in cm: "))
            height = int(input("Enter the height of the triangle in cm: "))
            triangle(base, height)
            user_num = int(input("Please enter the number of your selection: "))
            validate(user_num)
        if user_num == 3:
            length = int(input("Enter the length of one side of the square in cm: "))
            square(length)
            user_num = int(input("Please enter the number of your selection: "))
            validate(user_num)
        if user_num == 4:
            radius = int(input("Enter the radius of the circle in cm: "))
            circle(radius)
            user_num = int(input("Please enter the number of your selection: "))
            validate(user_num)
        if user_num == 5:  # upon quitting, "Goodbye!" will be printed
            print("Goodbye!")


def menu():
    print("This program will find the area of a shape for you.\n1. Rectangle\n2. Triangle\n3. Square\n4. Circle\n"
          "5. Quit")


def validate(num):
    while num != 1 and num != 2 and num != 3 and num != 4 and num != 5:
        print("That is not a valid number")
        num = int(input("Please enter the number of your selection: "))
    return num


def rectangle(num1, num2):  # takes the base and the height and calculates area
    area = num1 * num2
    print(f"The area of the rectangle is {area:.2f} cm squared")
    print('')
    menu()


def triangle(num1, num2):  # takes the base and the height and calculates area
    area = 1/2 * num1 * num2
    print(f"The area of the triangle is {area:.2f} cm squared")
    print('')
    menu()


def square(num):  # takes the length of any side and calculates area
    area = num**2
    print(f"The area of the square is {area:.2f} cm squared")
    print('')
    menu()


def circle(num):  # takes the radius and calculates area
    area = PI * (num**2)
    print(f"The area of the circle is {area:.2f} cm squared")
    print('')
    menu()


main()
