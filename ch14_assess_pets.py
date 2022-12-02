"""
This program uses an SQL database with two related tables in order to generate a report of pet owners and their
respective pets
"""
import sqlite3


def main():
    try:
        # Establish a connection to the database and get a cursor
        conn = sqlite3.connect('pets.db')
        cur = conn.cursor()

        # Create Owners table and insert data from the respective comma-delimited data file
        cur.execute('''CREATE TABLE IF NOT EXISTS Owners (OwnerID INTEGER PRIMARY KEY NOT NULL, 
                                                          OwnerName TEXT, 
                                                          OwnerPhone TEXT)''')
        owners_file = open('Owners.txt', 'r')
        for line in owners_file:
            in_tuple1 = tuple(line.strip().split(','))
            cur.execute('''INSERT INTO Owners (OwnerName, OwnerPhone) VALUES (?, ?)''', in_tuple1)

        # Create Pets table and insert data from the respective comma-delimited data file
        cur.execute('''CREATE TABLE IF NOT EXISTS Pets (PetID INTEGER PRIMARY KEY NOT NULL, 
                                                        PetName TEXT, 
                                                        PetType TEXT, 
                                                        PetBreed TEXT, 
                                                        OwnerID INTEGER, 
                                                        FOREIGN KEY (OwnerID) REFERENCES Owners(OwnerID))''')
        pets_file = open('Pets.txt', 'r')
        for line in pets_file:
            in_tuple2 = tuple(line.strip().split(','))
            cur.execute('''INSERT INTO Pets (PetName, PetType, PetBreed, OwnerID) VALUES (?, ?, ?, ?)''', in_tuple2)

        # Nested for loops select, fetch and display each owner's information followed by their pets' information
        cur.execute('SELECT OwnerID, OwnerName, OwnerPhone FROM Owners')
        owners = cur.fetchall()
        for ownerID, name, phone in owners:
            print(f'{name}   {phone}')
            cur.execute('SELECT PetName, PetType, PetBreed FROM Pets '
                        'WHERE OwnerID == ?', (ownerID,))
            pets = cur.fetchall()
            for pet_name, pet_type, breed in pets:
                print(f'       {pet_name} is a {breed} {pet_type}.')

        # Commits changes and closes database connection
        conn.commit()
        conn.close()

    # Catches any file IO or sqlite3 errors and prints default error
    except IOError as err:
        print(f'%File IO error encountered: {err}')
    except sqlite3.Error as err:
        print(f'%SQL error encountered: {err}')


if __name__ == '__main__':
    main()
