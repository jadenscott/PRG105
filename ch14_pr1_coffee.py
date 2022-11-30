"""
This program creates an SQL table to store coffeehouse supplies data from a CSV file.
"""
import sqlite3


def main():
    try:
        # Connect to the database
        conn = sqlite3.connect('coffee.db')

        # Create cursor
        cur = conn.cursor()

        # Create a table named Coffee
        cur.execute('''CREATE TABLE Coffee (ProductID INTEGER PRIMARY KEY NOT NULL,
                                            Product TEXT,
                                            Category TEXT,
                                            Supplier TEXT)''')

        # Open the CSV file for reading
        infile = open('coffeehouse_supplies.csv', 'r')

        # Initialize count variable
        count = 0

        for line in infile:
            # Strips new line and splits values by comma, then stores data in a tuple
            in_tuple = tuple(line.strip().split(','))

            # Inserts each tuple containing Product, Category and Supplier into SQL table
            cur.execute('''INSERT INTO Coffee (Product, Category, Supplier)
                            VALUES (?, ?, ?)''', in_tuple)

            # Increments count each time a record is added to the table
            count += 1

        # Commits changes and closes database connection
        conn.commit()
        conn.close()
        
        print(f'{count} records added.')

    # Catches any errors opening the CSV file
    except IOError as err:
        print(f'%File IO error encountered: {err}')

    # Catches any SQl errors
    except sqlite3.Error as err:
        print(f'%SQL error encountered: {err}')


if __name__ == '__main__':
    main()
