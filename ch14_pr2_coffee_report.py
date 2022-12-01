"""
This program generates a report displaying the data from the Coffee SQL table created in 'ch14_pr1_coffee.py'.
"""
import sqlite3


def main():
    try:
        # Connect to the database
        conn = sqlite3.connect('coffee.db')

        # Create cursor
        cur = conn.cursor()

        print(f'Category         Product            Supplier\n'
              f'========= ===================== ===============')

        """
        COFFEE CATEGORY
        """
        # Selects the Category field, fetches the Coffee category and prints it
        cur.execute('''SELECT Category FROM Coffee'
                    '   WHERE Category == "Coffee"''')
        category = cur.fetchone()
        print(f'{category[0]}')

        # Selects and fetches all records in the coffee category
        # Orders products alphabetically
        cur.execute('''SELECT * FROM Coffee
                        WHERE Category == "Coffee"
                        ORDER BY Product''')
        coffee = cur.fetchall()

        # Prints out each product and supplier in a formatted manner
        for record in coffee:
            print(f'          {record[1]:22}{record[3]}')

        """
        CONDIMENTS CATEGORY
        """
        cur.execute('''SELECT Category FROM Coffee'
                    '   WHERE Category == "Condiments"''')
        category = cur.fetchone()
        print(f'{category[0]}')

        cur.execute('''SELECT * FROM Coffee
                        WHERE Category == "Condiments"
                        ORDER BY Product''')
        condiments = cur.fetchall()

        for record in condiments:
            print(f'          {record[1]:22}{record[3]}')

        """
        DAIRY CATEGORY
        """
        cur.execute('''SELECT Category FROM Coffee'
                    '   WHERE Category == "Dairy"''')
        category = cur.fetchone()
        print(f'{category[0]}')

        cur.execute('''SELECT * FROM Coffee
                        WHERE Category == "Dairy"
                        ORDER BY Product''')
        dairy = cur.fetchall()

        for record in dairy:
            print(f'          {record[1]:22}{record[3]}')

        """
        PAPER CATEGORY
        """
        cur.execute('''SELECT Category FROM Coffee'
                    '   WHERE Category == "Paper"''')
        category = cur.fetchone()
        print(f'{category[0]}')

        cur.execute('''SELECT * FROM Coffee
                        WHERE Category == "Paper"
                        ORDER BY Product''')
        paper = cur.fetchall()

        for record in paper:
            print(f'          {record[1]:22}{record[3]}')

        """
        TEA CATEGORY
        """
        cur.execute('''SELECT Category FROM Coffee'
                    '   WHERE Category == "Tea"''')
        category = cur.fetchone()
        print(f'{category[0]}')

        cur.execute('''SELECT * FROM Coffee
                        WHERE Category == "Tea"
                        ORDER BY Product''')
        tea = cur.fetchall()

        for record in tea:
            print(f'          {record[1]:22}{record[3]}')

        # Commits changes and closes database connection
        conn.commit()
        conn.close()

    # Catches any SQl errors
    except sqlite3.Error as err:
        print(f'%SQL error encountered: {err}')


if __name__ == '__main__':
    main()
