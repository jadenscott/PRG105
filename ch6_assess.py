"""
This program tries to open a given file, then tries to print the numerical data of that file.
Then, the program calculates and prints the total, number of entries and average.
"""


def main():
    print("This program will total and average numbers in your data file.")

    # gets the name of user's data file
    user_file = input("Enter the name of your data file: ")

    # tries to open the user's file
    try:
        infile = open(user_file, 'r')

        # initializes accumulator
        total = 0.0

        # initializes count variable
        count = 0

        for line in infile:
            try:
                # converts to float and strips new line character
                value = float(line.rstrip('\n'))

                # calculates total and count
                total += value
                count += 1

                # prints each value line-by-line
                print(f'{value:,.2f}')

                # prints error message to account for bad data
            except ValueError as err:
                print(err)
                # print(f"Line {count + 1} with a value {infile.readline(count)} was invalid.")

        # calculates average
        average = total / count

        # closes file
        infile.close()

        print('')

        # prints total, number of entries and average
        print(f'Total:{total:20,.2f}')
        print(f'Number of entries:{count:8}')
        print(f'Average:{average:18,.2f}')

    # prints an error message if the user's file cannot be read
    except IOError:
        print(f"Unable to access the file: '{user_file}'")


if __name__ == '__main__':
    main()
