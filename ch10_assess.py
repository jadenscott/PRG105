"""
This program uses a Movie class to design Movie objects which are used to display a table of Marvel movies with a
column for titles, a column for release year, and a column for the year in which the story takes place
"""


class Movie:

    def __init__(self, title, release_year, story_year):
        self.__title = title
        self.__release_year = release_year
        self.__story_year = story_year

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_release_year(self, release_year):
        self.__release_year = release_year

    def get_release_year(self):
        return self.__release_year

    def set_story_year(self, story_year):
        self.__story_year = story_year

    def get_story_year(self):
        return self.__story_year


def main():

    # initializes list to store raw data in
    list_one = []

    # opens the .csv file for reading
    infile = open('MarvelMovies.csv', 'r')

    # appends each line of the input file to list_one
    for line in infile:
        list_one.append(line.strip())

    # closes the file
    infile.close()

    # splits each item in list_one at the commas
    list_two = [item.split(',') for item in list_one]

    # initializes lists
    objects_list = []
    title_list = []

    # creates Movie objects using list_two
    # adds only the titles from list_two to title_list
    for item in list_two:
        objects_list.append(Movie(item[0], item[1], item[2]))
        title_list.append(item[0])

    print('            Title                 Release  Storyline')

    # sorts the titles alphabetically, prints them and the corresponding years in a table
    for title in sorted(title_list):
        for item in objects_list:
            if title == item.get_title():
                print(f'{item.get_title():36}{item.get_release_year():9}{item.get_story_year()}')


if __name__ == '__main__':
    main()
