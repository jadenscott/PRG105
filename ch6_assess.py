"""
This program displays each number from a text file, then, adds them all up and displays the total, then, displays how
many numbers there are, then, calculate and display the average.
"""


def main():
    print("This program will total and average numbers in your data file.")

    # gets the name of user's data file
    user_file = input("Enter the name of your data file: ")

    # tries to open the user's file
    try:
        infile = open(user_file, 'r')
        infile.close()

    # prints an error message if the user does not type "sales_error-1"
    except IOError:
        if user_file != "sales_error-1":
            print(f"Unable to access the file: '{user_file}'\n")

    if user_file == "sales_error-1":
        # opens 'sales_error-1.txt' for reading and creates infile variable
        infile = open('sales_error-1.txt', 'r')

        # initializes accumulator
        total = 0.0

        # initializes count variable
        count = 0

        # initializes average variable
        average = 0.0

        for line in infile:
            try:
                # converts to float and strips new line character
                value = float(line.rstrip('\n'))

            # prints error message to account for bad data
            except ValueError as err:
                print(err)

            # prints each value line-by-line
            print(f'{value:,.2f}')

            # calculates total, count and average
            total += value
            count += 1
            average = total / count

        print('')

        # closes file
        infile.close()

        # prints total, number of entries and average
        print(f'Total:{total:20,.2f}')
        print(f'Number of entries:{count:8}')
        print(f'Average:{average:18,.2f}')


if __name__ == '__main__':
    main()
