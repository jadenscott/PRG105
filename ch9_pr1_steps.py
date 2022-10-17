"""
This program tracks the number of daily steps the user takes, then it calculates and displays the total and average
steps taken, minimum steps taken, and maximum steps taken.
"""


def main():
    # days_of_week list is created
    days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    # steps_taken dictionary is initialized
    steps_taken = {}

    # total accumulator is initialized
    total = 0

    # count is initialized
    count = 0

    print('You will be entering the number of steps taken for each day of the week.')

    # adds key-value pairs to steps_taken
    # each day of the week is a key and each corresponding amount of steps_taken is a value
    for day in days_of_week:
        steps_taken[day] = int(input(f'Please enter the number of steps taken on {day}: '))
        count += 1

    print('')

    # adds each amount of steps taken to the total accumulator
    for value in steps_taken.values():
        total += value

    # displays total
    print(f'You walked a total of {total:,} steps during the week.')

    # calculates and displays average
    print(f'You walked an average of {total / count:,.0f} steps per day.')

    # finds maximum amount of steps taken
    max_value = max(steps_taken.values())

    # displays maximum amount of steps taken
    print(f'The maximum amount of steps you took was {max_value:,} on:')

    # finds and displays the day(s) on which the maximum amount of steps was achieved
    for key in steps_taken:
        if steps_taken[key] == max_value:
            print(f'    {key}')

    # finds the minimum amount of steps taken
    min_value = min(steps_taken.values())

    # displays the minimum amount of steps taken
    print(f'The minimum amount of steps you took was {min_value:,} on:')

    # finds and displays the day(s) on which the minimum amount of steps was achieved
    for key in steps_taken:
        if steps_taken[key] == min_value:
            print(f'    {key}')


if __name__ == '__main__':
    main()
