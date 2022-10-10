def main():
    # description of program
    print("This program accepts a phrase and returns the acronym.")

    # gets said phrase from the user
    phrase = input("Please enter a phrase to convert: ")

    # splits phrase into a list
    phrase_list = phrase.split(' ')

    # prints the first character as a capital letter of each word in phrase_list
    for item in phrase_list:
        print(item[0].upper(), end='')


if __name__ == '__main__':
    main()
