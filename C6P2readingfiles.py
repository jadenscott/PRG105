"""
This program displays each number from a text file, then, adds them all up and displays the total, then, displays how
many numbers there are, then, calculate and display the average.
"""


def main():
    # opens 'c6p2numbers.txt' for reading and creates numbers_file variable
    numbers_file = open('c6p2numbers.txt', 'r')

    # line variable reads a line from numbers_file
    line = numbers_file.readline()

    # initializes accumulator
    total = 0.0

    # initializes count variable
    count = 0

    # initializes average variable
    average = 0.0

    for line in numbers_file:
        # strips new line character
        line = line.rstrip('\n')

        # converts each number into a float
        value = float(line)

        # prints each value as a float
        print(f'{value:,.2f}')

        # calculates total, count and average
        total += value
        count += 1
        average = total / (count + 1)

    print('')

    # closes file
    numbers_file.close()

    # prints total, number of entries and average
    print(f'Total:{total:20,.2f}')
    print(f'Number of entries:{count + 1:8}')
    print(f'Average:{average:18,.2f}')


if __name__ == '__main__':
    main()
