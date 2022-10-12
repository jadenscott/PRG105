"""
Given two text files, one a list of customer information and the other a list of overdue accounts, this program
displays the information of the customers whose accounts are overdue.
"""


def main():
    try:
        # opens the text files in reading mode
        accounts_file = open('accounts.txt', 'r')
        over_90_file = open('over90.txt', 'r')

        # initializes the two lists, one for each file
        accounts_list = []
        over_90_list = []

        # for loops add each line of the files to their respective lists
        for line in accounts_file:
            accounts_list.append(line.strip())
        for line in over_90_file:
            over_90_list.append(line.strip())

        # closes the files
        accounts_file.close()
        over_90_file.close()

        # nested for loops test if items in over_90_list match anything in accounts_list
        for item in accounts_list:
            for string in over_90_list:
                if string in item:
                    print(item)

    # prints error message if file(s) cannot be opened
    except IOError as err:
        print(err)


if __name__ == '__main__':
    main()
