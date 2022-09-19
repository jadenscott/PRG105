# ColorMixer takes two primary colors and tells us the result from mixing them
# it needs primary colors (red, yellow or blue)


# this function gets a color from the user
# it validates the input and returns the value to the program
def get_color():
    color = input("Enter red, yellow, or blue: ")
    color = color.upper()

    # validate the input: test for BAD data -- if it's BAD, make them re-enter the data
    # if the data is good, there is nothing more to do
    while color != "RED" and color != "YELLOW" and color != "BLUE":
        color = input("Invalid color. Please enter red, yellow, or blue: ")
        color = color.upper()

    # return the good data to the calling program
    return color


# this function finds the resulting color when two colors are combined
# colors MUST be red or yellow or blue (assumes valid data)
def check_colors(one, two):
    # test the first color and then check the other two
    if one == "BLUE":
        if two == "RED":
            result = "PURPLE"
        else:  # the only other choice is yellow
            result = "GREEN"
    elif one == "RED":
        if two == "BLUE":
            result = "PURPLE"
        else:  # the only other choice is yellow
            result = "ORANGE"
    else:  # the only other choice is yellow
        if two == "BLUE":
            result = "GREEN"
        else:  # the only other choice is yellow
            result = "ORANGE"
    return result


# ----- MAIN PROGRAM -----
def main():
    print("This program accepts two primary colors and tells you")
    print("the result when they are combined.")

    # call the getColor() function to get the input AND validate it
    first_color = get_color()  # get the first color
    second_color = get_color()  # get the second color

    # I have validated each color individually, but I need to
    # make sure I have two DIFFERENT primary colors
    while first_color == second_color:
        print("I need two different colors. I already have", first_color)
        second_color = get_color()
    # now call the function that checks for the resulting color
    # the returned value goes into resultColor
    result_color = check_colors(first_color, second_color)
    print(f'{first_color} and {second_color} makes {result_color}')


main()
