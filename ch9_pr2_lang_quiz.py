"""
This program is a simple foreign language quiz that tests if the user can translate the numbers 1-10 from German to
English.
"""


def main():
    # translations dictionary is created
    # each key is a number spelled in German and each corresponding value is the number spelled in English
    translations = {'ein': 'one', 'zwei': 'two', 'drei': 'three', 'vier': 'four', 'funf': 'five', 'sechs': 'six',
                    'sieben': 'seven', 'acht': 'eight', 'neun': 'nine', 'zehn': 'ten'}

    # score accumulator is initialized
    score = 0

    print('Spell out the number in English that corresponds to the number spelled in German.')

    for key in translations:
        # answer stores the string the user types
        answer = input(f'What is the equivalent of {key}: ')

        # if answer is the same as the value in translations, one is added to the user's score
        if answer == translations[key]:
            score += 1
            print('Correct')

        # prints the correct answer if the user gets the question wrong
        else:
            print(f'Incorrect. The correct answer is {translations[key]}')

    # displays final score out of ten
    print(f'Your final score is {score}/10')

    # determines and prints user's letter grade based on his score
    if score == 10:
        print('A+')
    elif score == 9:
        print('A')
    elif score == 8:
        print('B')
    elif score == 7:
        print('C')
    elif score == 6:
        print('D')
    else:
        print('F')


if __name__ == '__main__':
    main()
