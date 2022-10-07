"""
This program encodes a given string, prints it to the console in the form of a list and writes it to a text file
"""


def main():
    # lowercase and uppercase letters, space, period, comma, exclamation mark
    alpha_array = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J',
                   'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T',
                   'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z', ' ', '.', ',', '!']

    # parallel array used to encode text
    encoded_array = ['(', 's', 'q', 'E', '.', 'P', 'Q', 'j', '/', 'L', 'W', 'a', '>', 'y', 'v', '*', 'e', '^', 't',
                       '#', '=', 'U', '&', 'C', ']', 'O', '+', 'J', 'k', ')', 'l', 'F', '{', 'T', 'n', 'w', ',', 'm',
                       'R', '}', '|', 'v', '[', ';', 'b', ':', 'c', '%', 'Y', '<', 'p', 'G', '@', 'X', 'K', '?']

    # what the user would like to encode
    phrase = input("Enter a phrase to encode: ")

    # each character in phrase is an item in user_list
    user_list = list(phrase)

    # encoded list is initialized
    encoded_user_list = []

    # open 'encoded_strings.txt.' for writing
    encoded_file = open('encoded_strings.txt', 'w')

    # grabs index for each item in user_list, finds the corresponding character in encrypted_array, appends it to
    # encrypted_list and writes it to encoded_file
    for item in user_list:
        encoded_user_list.append(encoded_array[(alpha_array.index(item))])
        encoded_file.write(f'{encoded_array[(alpha_array.index(item))]}\n')

    # closes encoded_file
    encoded_file.close()

    print(encoded_user_list)


if __name__ == '__main__':
    main()


