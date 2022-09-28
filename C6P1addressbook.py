"""
This program gathers contact information for people.
"""


def main():
    # gets the amount of people to collect contact information from
    num_people = int(input("How many people do you want to add to the file? "))

    # opens a text file to write the contact information to
    contacts_file = open('contacts.txt', 'w')

    # gets contact information for each person
    for count in range(1, num_people + 1):
        # gets each person's name, email address and phone number
        name = input("What is the name of the person? ")
        number = input("What is their phone number? ")
        email = input("What is their email address? ")

        # writes the contact information to contacts_file
        contacts_file.write(f'{name}, {number}, {email}\n')

    # closes contacts_file
    contacts_file.close()


main()
