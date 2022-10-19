"""
This program reads the contents of a text file and displays the words that have only occurred once.
"""


def main():
    # initialize word_count dictionary
    word_count = {}

    # initialize words list
    words = []

    # infile opens 'tale_of_two_cities.txt' for reading
    infile = open('tale_of_two_cities.txt', 'r')

    # adds each stripped line in infile to words list
    for line in infile:
        words.append(line.strip())

    # adds key-value pairs to word_count
    # adds one to the value every time the word occurs
    # if the word does not occur more than once, its value is one
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # only prints the words that appear once in the file
    for word in word_count:
        if word_count[word] == 1:
            print(word)


if __name__ == '__main__':
    main()

