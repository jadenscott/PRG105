"""
This program attempts to open the user's file containing encoded text and then decodes that text and displays it.
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

    print("This program will decode a coded text file.")

    # gets a file name from the user and stores it as infile
    infile = input("Enter the file name: ")

    try:
        # tries to open infile in reading mode as f
        f = open(infile, 'r')

        # these two lists are initialized
        encoded_list = []
        decoded_list = []

        # strips the \n from each line in f and adds it to encoded_list
        for line in f:
            encoded_list.append(line.strip())

        # closes the file
        f.close()

        # grabs index of encoded_array for each item in encoded_list, grabs the corresponding index of alpha_array and
        # appends the result to decoded_list
        for item in encoded_list:
            decoded_list.append(alpha_array[(encoded_array.index(item))])

        # prints each item in decoded_list in a more readable way
        for item in decoded_list:
            print(item, end='')

    except IOError:
        # if the user's file cannot be found, an error message will be printed
        print(f"Cannot open '{infile}'. Please restart the program.")


if __name__ == '__main__':
    main()
