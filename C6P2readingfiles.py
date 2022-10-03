"""
This program displays each number from a text file, then, adds them all up and displays the total, then, displays how
many numbers there are, then, calculate and display the average.
"""


def main():
    # opens 'c6p2numbers.txt' for reading and creates numbers_file variable
    in_file = open('sales_totals.txt', 'r')

    # initializes accumulator
    total = 0.0

    # initializes count variable
    count = 0

    # initializes average variable
    average = 0.0

    for line in in_file:
        # converts to float and strips new line character
        value = float(line.rstrip('\n'))

        # prints each value line-by-line
        print(f'{value:,.2f}')

        # calculates total, count and average
        total += value
        count += 1
        average = total / count

    print('')

    # closes file
    in_file.close()

    # prints total, number of entries and average
    print(f'Total:{total:20,.2f}')
    print(f'Number of entries:{count:8}')
    print(f'Average:{average:18,.2f}')


if __name__ == '__main__':
    main()
