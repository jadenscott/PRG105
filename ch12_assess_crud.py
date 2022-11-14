"""
This program is a CRUD (create, read, update, delete) program that uses multiple functions to achieve this. This
program also makes use of pickling and dictionaries in order to carry out its purpose which is to associate names with
email addresses, essentially.
"""
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


def main():
    try:
        # pickle dictionary
        infile = open('customer_file.dat', 'rb')
        customer_file = pickle.load(infile)
        infile.close()

    except IOError:
        # initialize dictionary
        customer_file = {}

    # initialize choice
    choice = 0

    # calls appropriate function passing customer_file as an argument
    while choice != QUIT:
        choice = menu()
        if choice == LOOK_UP:
            read(customer_file)
        elif choice == ADD:
            create(customer_file)
        elif choice == CHANGE:
            update(customer_file)
        elif choice == DELETE:
            delete(customer_file)
        else:
            print('Shutting down...')


def menu():
    # initialize choice
    choice = 0

    # keeps displaying menu if choice is not valid
    while choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5:
        print("Enter your selection:\n\t1. Look up an email by name\n\t2. Add a new entry\n\t"
              "3. Change a person's email\n\t4. Delete an entry\n\t5. Quit")

        # try to convert choice to integer
        try:
            choice = int(input('? '))
            return choice
        except ValueError:
            print('Enter an integer.')


def read(customer_file):
    # get name from user
    customer_name = input('\nEnter a name: ')

    # if the name is found, the corresponding email is printed
    if customer_name in customer_file:
        print(f'{customer_file[customer_name]}\n')
    else:
        print('No data found. Try adding a new entry.\n')


def create(customer_file):
    customer_name = input('\nEnter a name: ')

    # get email address from user
    customer_email = input(f'Enter an email address for {customer_name}: ')

    # adds a key-value pair to the dictionary customer_file
    customer_file[customer_name] = customer_email

    # pickles data
    save(customer_file)

    print(f'{customer_name} has been added with email {customer_email}\n')


def update(customer_file):
    customer_name = input('\nEnter a name: ')

    # nested if statements to replace a customer's email address
    if customer_name in customer_file:
        answer = input(f'Current email for {customer_name} is {customer_file[customer_name]}. Do you want to change '
                       f'it? (y/n) ')
        if answer == 'y':
            customer_email = input(f'Enter the new email address for {customer_name}: ')
            customer_file[customer_name] = customer_email
            save(customer_file)

            print(f'The email for {customer_name} is now {customer_email}\n')
        else:
            print('No changes were made.\n')
    else:
        print('No data found. Try adding a new entry.\n')


def delete(customer_file):
    customer_name = input('\nEnter a name: ')

    # nested if statements to delete a customer's entry
    if customer_name in customer_file:
        answer = input(f'Current email for {customer_name} is {customer_file[customer_name]}. Are you sure you want to'
                       f' delete it? (y/n) ')
        if answer == 'y':
            del customer_file[customer_name]
            save(customer_file)
            print(f'{customer_name} has been removed\n')
        else:
            print('No changes were made.\n')
    else:
        print('No data found. Try adding a new entry.\n')


def save(customer_file):
    try:
        infile = open('customer_file.dat', 'wb')
        pickle.dump(customer_file, infile)
        infile.close()
    except IOError:
        print('Error: unable to save file')


if __name__ == '__main__':
    print('Welcome to your email list manager!\n')
    main()
