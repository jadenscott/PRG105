"""
This program displays a menu and gives the user a description of the item he chooses.
"""

# menu is displayed first
print("Select one of the menu options below to find out more\n"
      "A. Burger\nB. Chicken sandwich\nC. BBQ pork sandwich\nD. Cheesesteak\nE. Hot dog")

# variables are declared next
user_choice = input("Please enter the letter of your choice: ")

# while loop is used to account for bad data
while user_choice != "A" and user_choice != "B" and user_choice != "C" and user_choice != "D" and user_choice != "E":
    user_choice = input("Invalid character. Please select from A-E: ")


def burger():  # function for choice A is defined
    print("American cheese, lettuce, tomato, grilled onions, pickle, mayo and ketchup.\nServed with fries.")


def chicken():  # function for choice B is defined
    print("Fried or grilled. Spicy available for both. Comes with pickle and mayonnaise.\n"
          "Served with tater tots.")


def pork():  # function for choice C is defined
    print("Homemade barbecue sauce, crispy onions.\nServed with mac and cheese or a cup of chili.")


def cheesesteak():  # function for choice D is defined
    print("Vermont Cheddar cheese on top of sliced rib eye steak.\nServed with fries.")


def hotdog():  # function for choice E is defined
    print("A classic Chicago-style hot dog.\nServed with fries.")


# independent if-statements to process user input
if user_choice == "A":
    burger()

if user_choice == "B":
    chicken()

if user_choice == "C":
    pork()

if user_choice == "D":
    cheesesteak()

if user_choice == "E":
    hotdog()
