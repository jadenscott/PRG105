"""
This program will allow the user to get the area of the shape his choice after giving the program the dimensions in
centimeters
"""

PI = 3.14159265358  # global variable for pi is declared


def main():
    # choice is initialized
    user_num = 0
    while user_num != 5:
        print("This program will find the area of a shape for you.\n1. Rectangle\n2. Triangle\n3. Square\n4. Circle\n"
            "5. Quit")  # menu choices are printed
        user_num = int(input("Please enter the number of your selection: "))  # get user's choice
        user_num = validate(user_num)  # to ensure that user_num is an integer between 1 and 5

        # if-elif statements to process user input
        if user_num == 1:
            base = int(input("Enter the base of the rectangle in cm: "))  # get base in cm
            height = int(input("Enter the height of the rectangle in cm: "))  # get height in cm
            area = rectangle(base, height)
            print(f"The area of the rectangle is {area:.2f} cm squared")  # print area of rectangle
        elif user_num == 2:
            base = int(input("Enter the base of the triangle in cm: "))  # get base in cm
            height = int(input("Enter the height of the triangle in cm: "))  # get height in cm
            area = triangle(base, height)
            print(f"The area of the triangle is {area:.2f} cm squared")  # print area of triangle
        elif user_num == 3:
            length = int(input("Enter the length of one side of the square in cm: "))  # get length of one side in cm
            area = square(length)
            print(f"The area of the square is {area:.2f} cm squared")  # print area of square
        elif user_num == 4:
            radius = int(input("Enter the radius of the circle in cm: "))  # get radius of circle in cm
            area = circle(radius)
            print(f"The area of the circle is {area:.2f} cm squared")  # print area of circle
        elif user_num == 5:  # upon quitting, "Goodbye!" will be printed
            print("Goodbye!")


def validate(num):
    while num != 1 and num != 2 and num != 3 and num != 4 and num != 5:
        print("That is not a valid number")
        num = int(input("Please enter the number of your selection: "))
    return num


def rectangle(base, height):  # calculates and returns area of a rectangle
    area = base * height
    return area


def triangle(base, height):  # calculates and returns area of a triangle
    area = (1/2) * base * height
    return area


def square(length):  # calculates and returns area of a square
    area = length**2
    return area


def circle(radius):  # calculates and returns area of a circle
    area = PI * (radius**2)
    return area


if __name__ == '__main__':
    main()
