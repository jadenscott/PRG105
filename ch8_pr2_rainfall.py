"""
This program validates the data from 'rainfall-totals.txt', calculates the total and average, and displays them.
"""


def main():
    # total accumulator is initialized
    total = 0

    # count is initialized
    count = 0

    # opens 'rainfall-totals.txt' for reading
    infile = open('rainfall-totals.txt', 'r')

    # list for contents of infile is initialized
    contents = []

    # strips \n for each line in infile and appends it to contents list
    for line in infile:
        contents.append(line.strip())

    # closes the file
    infile.close()

    # data list splits each item of contents by the space
    data = [item.split(' ') for item in contents]

    for item in data:
        try:
            # converts numerical data into floating-point values
            amount = float(item[1])

            # adds each amount to the total
            total += amount

            # count is increased by one
            count += 1

        except ValueError:
            # prints an error message if the number cannot be converted to a float
            print(f'The amount of rainfall for {item[0]} was invalid.')

    # prints total and average after calculating it
    print(f'Total: {total:.1f} inches')
    print(f'Average: {total / count:.1f} inches')


if __name__ == '__main__':
    main()
