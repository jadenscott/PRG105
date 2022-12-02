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

        # Select all data in the Category field in the Coffee table
        cur.execute('SELECT Category FROM Coffee')

        # Add data all from Category field to a list
        category_list = cur.fetchall()

        # Make a list that stores each unique category
        unique_categories = []
        for item in category_list:
            if item[0] not in unique_categories:
                unique_categories.append(item[0])

        # Displays a header for the report
        print(f'Category         Product            Supplier\n'
              f'========= ===================== ===============')

        # Sorts unique categories alphabetically
        unique_categories.sort()

        for category in unique_categories:
            # Prints the category once
            print(category)

            # Selects and fetches all records in each category
            cur.execute('SELECT * FROM Coffee WHERE Category == ? ORDER BY Product', (category,))
            product_list = cur.fetchall()

            # Displays each record in a formatted manner
            for product in product_list:
                print(f'          {product[1]:20}  {product[3]}')

        # Commits changes and closes database connection
        conn.commit()
        conn.close()

    # Catches any SQl errors
    except sqlite3.Error as err:
        print(f'%SQL error encountered: {err}')


if __name__ == '__main__':
    main()
