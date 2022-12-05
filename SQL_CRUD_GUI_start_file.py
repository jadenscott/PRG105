"""
    This program combines the CRUD GUI with SQL as a data source.

    The Customer TABLE structure allows multiple entries with the same name, but customer_id is always unique.
            Therefore, the Update and Delete modules use ID to select a unique record.
    The Customer TABLE is created for you in the main() function at the bottom of this file.

    There are some features of Tkinter used in this program that are not in your book.
            In the CrudGUI module, some options are added for accessibility (in the main CrudGUI):
                -- setting the font size for the default font using tkfont
                -- changing the radio buttons to bar button style using:  <radiobutton>.configure(indicatoron=0)
            The re-sized font will be automatically applied to labels and buttons,
                but to use the re-sized font for an Entry widget, you need to use the parameter: font="TkDefaultFont"

            The following features are used in the AddGUI, ChangeGUI and DeleteGUI modules:
                Options to insert or clear text in an entry box (NOTE widget state must be NORMAL to use insert/delete):
                    -- <entry_box>.insert(<text>)
                    -- <entry_box>.delete(<text>)
                Options to enable or disable buttons:
                    -- to instantiate a button in the DISABLED state, use the parameter:  state=tkinter.DISABLED
                    -- after button exists:   <button>['state'] = tkinter.ACTIVE or <button>['state'] = tkinter.DISABLED
                    -- for an entry box:  <widget>['state'] = tkinter.NORMAL or <widget>['state'] = tkinter.DISABLED
                 Option to set focus (move the cursor to selected field) -- widget state must first be set to NORMAL:
                    -- <entry_box>.focus_set()

    TODO finish this program by completing each of the TODO instructions
    TODO Hint: When you have completed a TODO, mark it as *done* (in the TODO comments)
    TODO
    TODO Hint: The main() function at the bottom of the code will show you the TABLE structure
    TODO
    TODO Hint: You may want to complete the find_customer_by_name() and find_customer_by_id() functions
    TODO        first since they are used in multiple places in the code. Their function definitions
    TODO        are found near the bottom of the code.
"""
import tkinter
import tkinter.font as tkfont
import sqlite3


# main (root) GUI menu
class CrudGUI:
    def __init__(self, master):
        # the primary window (master) was initialized in the main() program
        #  -- save the master parameter in an instance variable to make it available throughout the class
        self.master = master
        self.master.title('Welcome Menu')

        # #######################################################################################################
        # these statements tell Tkinter what font size to use for the default font
        default_font = tkfont.nametofont("TkDefaultFont")
        # use a larger size value for better visibility
        default_font.configure(size=13)
        # #######################################################################################################

        # create two frames -- one for the menu, one for the buttons
        self.top_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)

        # the menu uses Radiobuttons so that only one option is selected at any time -- start by selecting option 1
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # create the radio buttons
        self.look = tkinter.Radiobutton(self.top_frame, text='Look up customer',
                                        variable=self.radio_var, value=1)
        self.add = tkinter.Radiobutton(self.top_frame, text='Add customer',
                                       variable=self.radio_var, value=2)
        self.change = tkinter.Radiobutton(self.top_frame, text='Update customer',
                                          variable=self.radio_var, value=3)
        self.delete = tkinter.Radiobutton(self.top_frame, text='Delete customer',
                                          variable=self.radio_var, value=4)

        # #######################################################################################################
        # for visibility at a larger scale, you can uncomment the lines below to
        #  -- turn off the radiobutton indicator (icon) resulting in a push-button look
        #  -- (Tkinter also provides the option to provide your own images for the icons)
        # self.look.configure(indicatoron=0)
        # self.add.configure(indicatoron=0)
        # self.change.configure(indicatoron=0)
        # self.delete.configure(indicatoron=0)
        # #######################################################################################################

        # pack the radio buttons
        self.look.pack(anchor='w', padx=20)
        self.add.pack(anchor='w', padx=20)
        self.change.pack(anchor='w', padx=20)
        self.delete.pack(anchor='w', padx=20)

        # create ok and quit buttons
        self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.open_menu, width=10)
        self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.master.destroy, width=10)

        # pack the buttons
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

    # this method is called to process the menu choice when the OK button is pressed
    # you will need to modify this method to process the other menu options based on the radio button selection
    #  -- each menu item should be instantiated as an appropriate class similar to the example provided
    # ##################################################################################################### #
    # NOTE: As you work to complete the program, you can comment out incomplete sections for testing.       #
    #       It may be helpful to temporarily comment out some of the options in the following chained-if.   #
    # ##################################################################################################### #
    def open_menu(self):
        if self.radio_var.get() == 1:
            _ = LookGUI(self.master)
        # elif self.radio_var.get() == 2:
            # _ = AddGUI(self.master)
        # elif self.radio_var.get() == 3:
        #     _ = ChangeGUI(self.master)
        # elif self.radio_var.get() == 4:
        #     _ = DeleteGUI(self.master)
        else:
            print("Program Error -- menu choice out of range.")


# This class processes the first menu choice -- to look for a name
# The database allows for multiple records of the same or similar names
# So, the database search allows for a partial match and will list all matches found
class LookGUI:
    def __init__(self, master):
        # tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
        # when the Toplevel window is closed, it returns focus to the master window
        self.look = tkinter.Toplevel(master)
        self.look.title('Search for customer by name')

        # create Frames for this Toplevel window
        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # widgets for top frame - label and entry box for name
        self.search_label = tkinter.Label(self.top_frame, text='Enter customer name to look for: ')
        # Entry boxes use their own font settings, so tell it to use the TkDefaultFont we set for the primary window
        self.search_entry = tkinter.Entry(self.top_frame, width=20, font="TkDefaultFont")

        # pack top frame
        self.search_label.pack(side='left')
        self.search_entry.pack(side='left')

        # middle frame - label for results
        self.info_string = tkinter.StringVar()
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.info_string, height=MAX_LIST_SIZE+1,
                                          width=60)

        # pack Middle frame
        self.result_label.pack(side='left')

        # buttons for bottom frame
        # TODO add three buttons to the bottom frame:
        # TODO      a button titled "Search First Name" that calls self.search_first
        # TODO      a button titled "Search Last Name" that calls self.search_last
        # TODO      a button titled "Main Menu" that closes the window and returns to the main menu
        self.search_first_button = tkinter.Button(self.bottom_frame, text='Search First Name',
                                                  command=self.search_first)
        self.search_last_button = tkinter.Button(self.bottom_frame, text='Search Last Name',
                                                 command=self.search_last)
        self.main_menu_button = tkinter.Button(self.bottom_frame, text='Main Menu',
                                               command=self.look.destroy)

        # pack bottom frame
        # TODO pack the buttons you just created
        self.search_first_button.pack(side='left')
        self.search_last_button.pack(side='left')
        self.main_menu_button.pack(side='left')

        # pack frames into the Toplevel window
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    # this method is called by the Search_first button
    def search_first(self):
        # TODO 1. get the data from the search_entry box
        # TODO 2. pass the name to find_customer_by_name() to search for the name in the database
        # TODO      set the Boolean parameter for find_customer_by_name() as indicated in the function description
        # TODO 3. call return_data_as_string() with the results of find_customer_by_name() and
        # TODO      display the result(s) in the result_label widget
        # TODO Hint: You will need to complete the functions find_customer_by_name() and return_data_as_string() below
        name = self.search_entry.get()
        results = return_data_as_string(find_customer_by_name(name, True))
        self.info_string.set(results)
        print(results)

    # this method is called by the Search_last button
    def search_last(self):
        # TODO 1. get the data from the search_entry box
        # TODO 2. pass the name to find_customer_by_name() to search for the name in the database
        # TODO      set the Boolean parameter for find_customer_by_name() as indicated in the function description
        # TODO 3. call return_data_as_string() with the results of find_customer_by_name() and
        # TODO      display the result(s) in the result_label widget
        # TODO Hint: You will need to complete the functions find_customer_by_name() and return_data_as_string() below
        name = self.search_entry.get()
        results = return_data_as_string(find_customer_by_name(name, False))
        self.info_string.set(results)

"""
# This class processes the second menu choice -- to add one or more records to the database
# Note: The Customer_ID field is automatically generated by SQL, so it is not included in the Add window
class AddGUI:
    def __init__(self, master):
        # tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
        self.add = tkinter.Toplevel(master)
        self.add.title('Add a customer')

        # create Frames for this Toplevel window
        self.first_name_frame = tkinter.Frame(self.add)
        self.last_name_frame = tkinter.Frame(self.add)
        self.phone_frame = tkinter.Frame(self.add)
        self.email_frame = tkinter.Frame(self.add)
        self.result_frame = tkinter.Frame(self.add)
        self.button_frame = tkinter.Frame(self.add)

        # widgets for top frame - label and entry box for name
        # TODO add labels and entry boxes for each of the following data fields:
        #        first name, last name, phone, email
        # TODO place each label and entry box into the corresponding frame (defined above)
        # TODO set appropriate widths for the entry boxes

        # pack data widgets into their frames
        # TODO pack each of the labels and entry boxes you just created

        # middle frame - label for results
        # TODO create a StringVar() called self.message
        # TODO create a Label in self.result_frame with width of 45 that will display the contents of self.message

        # pack results into frame
        # TODO pack the Label you just created

        # buttons for button frame
        # TODO add two buttons into the button_frame
        # TODO     the Add button should call self.add_customer
        # TODO     the Main Menu button should close the window and return to the master window


        # pack button frame
        # TODO pack the buttons you just added


        # pack frames
        self.first_name_frame.pack()
        self.last_name_frame.pack()
        self.phone_frame.pack()
        self.email_frame.pack()
        self.result_frame.pack()
        self.button_frame.pack()

    # This method is called when the Add button is pressed
    # It will check to make sure all fields have data in them, and if so,
    #     it will INSERT the data as a new record in the database
    #     and it will reset the form for the next record (erase data and set focus)
    def add_customer(self):
        # TODO get data from the entry widgets for first name, last name, phone and email; strip off white space

        # check to make sure data is available to add, if so, add to database
        # TODO use an if statement to verify that none of the fields are empty
        # if...
            customer_db = None
            try:
                # TODO use the try-except statement to connect to the database and INSERT the data
                # TODO remember to commit your changes
            except sqlite3.Error as err:
                # TODO if there is an SQLite error, set an error message into self.message

            finally:
                # if the insert succeeded, notify user, clear data fields for another potential add
                if customer_db is not None:
                    # TODO 1. set self.message to say "Customer added."
                    # TODO 2. clear the entry fields for first name, last name, phone and email
                    # TODO         to clear an entry field use: <field>.delete(0, tkinter.END)
                    # TODO 3. close the database connection

            # TODO aligned to the try block, set the focus to the first name entry widget
            # TODO     to set focus, use <field>.focus_set()

        else:
            # TODO set self.message to indicate data was not added due to incomplete data



# This class processes the third menu choice -- to update one or more records in the database (one at a time)
# Note: Only the Customer_ID is unique in the database, so the user must select the record by their ID
# Tkinter features are used to enable and disable widgets to focus the user on the steps required for processing
class ChangeGUI:
    def __init__(self, master):
        # tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
        self.change = tkinter.Toplevel(master)
        self.change.title('Change customer data')

        # create Frames for this Toplevel window
        self.id_frame = tkinter.Frame(self.change)
        self.find_button_frame = tkinter.Frame(self.change)
        self.find_frame = tkinter.Frame(self.change)
        self.name_frame = tkinter.Frame(self.change)
        self.email_frame = tkinter.Frame(self.change)
        self.phone_frame = tkinter.Frame(self.change)
        self.result_frame = tkinter.Frame(self.change)
        self.button_frame = tkinter.Frame(self.change)

        # locate the customer ID first
        self.id_label = tkinter.Label(self.id_frame, text="Enter customer ID: ")
        self.id_entry = tkinter.Entry(self.id_frame, width=10, font="TkDefaultFont")
        self.find_button = tkinter.Button(self.find_button_frame, text='Search by ID', command=self.find_customer)

        # widgets for top frame - label and entry box for name
        self.first_name_label = tkinter.Label(self.name_frame, text="Customer first name: ")
        self.first_name_entry = tkinter.Entry(self.name_frame, width=15, font="TkDefaultFont")
        self.last_name_label = tkinter.Label(self.name_frame, text="Customer last name: ")
        self.last_name_entry = tkinter.Entry(self.name_frame, width=15, font="TkDefaultFont")
        self.phone_label = tkinter.Label(self.phone_frame, text="Customer phone: ")
        self.phone_entry = tkinter.Entry(self.phone_frame, width=25, font="TkDefaultFont")
        self.email_label = tkinter.Label(self.email_frame, text="Customer email: ")
        self.email_entry = tkinter.Entry(self.email_frame, width=25, font="TkDefaultFont")
        # TODO the first name, last name, phone and email entry widgets above should initially have a DISABLED state
        # TODO 1. add a statement for each of these four entry widgets to change the state to DISABLED
        # TODO      Example:  self.first_name_entry['state'] = tkinter.DISABLED

        # pack data widgets into their frames
        self.id_label.pack(side='left')
        self.id_entry.pack(side='left')
        self.find_button.pack()
        self.first_name_label.pack(side='left')
        self.first_name_entry.pack(side='left')
        self.last_name_label.pack(side='left')
        self.last_name_entry.pack(side='left')
        self.phone_label.pack(side='left')
        self.phone_entry.pack(side='left')
        self.email_label.pack(side='left')
        self.email_entry.pack(side='left')

        # middle frame - label for results
        self.message = tkinter.StringVar()
        self.status_label = tkinter.Label(self.result_frame, textvariable=self.message, width=45)

        # pack results into frame
        self.status_label.pack(side='left')

        # buttons for button frame
        # TODO 1. add three buttons to the button_frame for Update, Cancel and Main Menu
        # TODO     Update should call self.change_customer
        # TODO     Cancel should call self.cancel_update
        # TODO     Main Menu should close the window and return to the master window
        # TODO The Add and Cancel buttons should initially be in a DISABLED state
        # TODO 2. add an argument to each of the Update and Cancel buttons to disable them
        # TODO     Example: state=tkinter.DISABLED

        # pack buttons into frame
        # TODO pack the buttons

        # pack frames
        self.id_frame.pack()
        self.find_button_frame.pack()
        self.name_frame.pack()
        self.phone_frame.pack()
        self.email_frame.pack()
        self.result_frame.pack()
        self.button_frame.pack()

    # this method is called when the Update button is pressed
    # Update button should not be ACTIVE unless a valid ID has been located
    def change_customer(self):
        # TODO get data from each of the entry widgets into variables, strip off white space

        # use data to locate and update matching database record
        customer_db = None
        try:
            # TODO connect to the database and UPDATE the Customer table with the data entered
            # TODO Use a WHERE clause to locate the record to update using the CustomerID

        except sqlite3.Error as err:
            self.message.set(f"Database error: {err}")
        finally:
            # if the update succeeded, notify user, clear data fields
            if customer_db is not None:
                self.message.set("Customer modified.")
                customer_db.close()
        # swap status of entry boxes and buttons
        self.swap_status()

    # This method is called when the Cancel button is pressed
    def cancel_update(self):
        # confirm with user that nothing changes
        self.message.set("No changes made.")
        # even though no data has changed, we need to reset entry boxes and reset button states
        self.swap_status()

    # swap active portions of the form to prepare for the next (potential) update
    def swap_status(self):
        # clear and disable name and email entry fields; disable Update & Cancel buttons
        # clear ID entry but make it active
        # TODO ---------------------------------------------------------------------------------
        # TODO NOTE: The order of the following steps must be followed
        # TODO       because you cannot modify the contents of an entry widget that is disabled
        # TODO ---------------------------------------------------------------------------------
        # TODO the first name, last name, phone and email entry widgets should be cleared and disabled
        # TODO the customer ID widget should be cleared and enabled for the next update
        # TODO 1. clear the first name, last name, phone and email entry widgets
        # TODO       Example:  <widget>.delete(0, tkinter.END)
        # TODO 2. disable the first name, last name, phone and email entry widgets
        # TODO       Example: <widget>['state'] = tkinter.DISABLED
        # TODO 3. disable the Update and Cancel buttons using the same syntax
        # TODO 4. activate the Search By ID button by setting the state to: tkinter.ACTIVE
        # TODO 5. enable the id_entry widget by setting the state to: tkinter.NORMAL
        # TODO 6. clear the data from the id_entry widget
        # TODO 7. set focus to the id_entry widget using: <widget>.focus_set()

    # This method is called when the Search by ID button is pressed
    def find_customer(self):
        # get the data from the entry box
        id_number = self.id_entry.get().strip()
        # look for the name in the dictionary
        result = find_customer_by_id(id_number)
        # there should be at most one record matching the ID (or none)
        if len(result) == 1:
            # TODO enable the first name, last name, phone and email entry widgets
            # TODO then, using the data from the tuple record in the list named result
            # TODO      populate the corresponding entry widgets
            # TODO NOTE: Each entry widget must be enabled before data is inserted
            # TODO 1. enable each widget using: <widget>['state'] = tkinter.NORMAL
            # TODO 2. insert data into each widget using: <widget>.insert(0, <variable name>)
            # swap button states to allow for Update or Cancel,
            # but disallow searching for a new ID while a record is active
            # TODO 1. Enable the Update and Cancel buttons using: <widget>['state'] = tkinter.ACTIVE
            # TODO 2. Disable the customer ID entry field and Search by ID button using:
            # TODO      <widget>['state'] = tkinter.DISABLED
            # TODO 3. set self.message to an empty string
            # TODO 4. set focus to the first name entry widget using: <widget>.focus_set()
        else:
            # if no record was found, delete the ID value and reset focus to get a new ID
            # TODO 1. set self.message to indicate that the Customer ID was not found
            # TODO 2. clear the data from the customer id entry widget
            # TODO 3. set focus to the customer id entry widget


# This class processes the third menu choice -- to delete one or more records in the database (one at a time)
# Note: Only the Customer_ID is unique in the database, so the user must select the record by their ID
# Tkinter features are used to enable and disable buttons to focus the user on the steps required for processing
class DeleteGUI:
    def __init__(self, master):
        # tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
        self.delete = tkinter.Toplevel(master)
        self.delete.title('Delete customer')

        # create Frames for this Toplevel window
        self.id_frame = tkinter.Frame(self.delete)
        self.find_button_frame = tkinter.Frame(self.delete)
        self.find_frame = tkinter.Frame(self.delete)
        self.result_frame = tkinter.Frame(self.delete)
        self.button_frame = tkinter.Frame(self.delete)

        # locate the customer ID first - similar to the UpdateGUI widgets
        # TODO add a Label, Entry widget and Button for customer ID into self.id_frame
        # TODO the Search by ID button should call self.find_customer

        # pack data widgets into their frames
        # TODO pack the widgets you just created

        # middle frame - label for results
        # TODO create self.message as a StringVar()
        # TODO create a Label in self.result_frame with width 45 to display the contents of self.message

        # pack results into frame
        # TODO pack the label

        # buttons for button frame
        # TODO create three buttons in self.button_frame
        # TODO the Delete button should call self.remove and have state=DISABLED
        # TODO the Cancel button should call self.cancel_removal and have state=DISABLED
        # TODO the Main Menu button should close the window and return to the master window

        # pack button frame
        # TODO pack the buttons

        # pack frames
        self.id_frame.pack()
        self.find_button_frame.pack()
        self.result_frame.pack()
        self.button_frame.pack()

    # This method is called when the Delete button is pressed
    # Delete button should not be ACTIVE unless a valid ID has been located and displayed
    def remove(self):
        # get the customer_ID that has been selected, then remove the corresponding record from the database
        # TODO get the value from the Customer ID entry widget and strip off whitespace
        # TODO      (You will use the value in your WHERE clause below)
        customer_db = None
        try:
            # TODO connect to the database and DELETE FROM the Customer table
            # TODO Use a WHERE clause to locate the correct record to DELETE using the CustomerID
        except sqlite3.Error as err:
            self.message.set(f"Database error: {err}")
        finally:
            # notify user if delete was successful
            if customer_db is not None:
                self.message.set("Customer removed.")
                customer_db.close()
        # reset entry boxes and button states
        self.swap_status()

    # This method is called when the Cancel button is pressed
    def cancel_removal(self):
        # confirm with user that nothing changes
        self.message.set("No changes made.")
        # reset entry boxes and button states
        self.swap_status()

    # reset entry boxes and button states to put the focus back on selecting a new ID for potential removal
    def swap_status(self):
        # TODO ---------------------------------------------------------------------------------
        # TODO NOTE: The order of the following steps must be followed
        # TODO       because you cannot modify the contents of an entry widget that is disabled
        # TODO ---------------------------------------------------------------------------------
        # TODO 1. disable the Delete and Cancel buttons
        # TODO 2. activate the Search By ID button by setting the state to: tkinter.ACTIVE
        # TODO 3. enable the Customer ID entry widget by setting the state to: tkinter.NORMAL
        # TODO 4. clear the data from the Customer ID entry widget
        # TODO 5. set focus to the Customer ID entry widget

    # This method is called when the Search by ID button is pressed
    def find_customer(self):
        # get the data from the entry box
        # TODO get the value from the Customer ID entry widget and store it in a variable called id_number
        # look for the name in the dictionary
        result = find_customer_by_id(id_number)
        # there should be at most one record matching the ID (or None)
        # TODO create an if statement that tests to make sure there is only one record in the list result
            # if one record is found, display all data (including ID) so that user can confirm
            # TODO get the individual values out of the record (tuple)
            # TODO    and display them in a string using the message widget
            # enable button choices to Delete or Cancel
            # TODO change the Delete and Cancel buttons to have a state of tkinter.ACTIVE
            # -- disable id section until this record is processed, but do not erase ID until processed
            # TODO change the states of the Customer ID entry widget and Search by ID button to tkinter.DISABLED
        else:
            # if no matching ID is found, reset for another try
            # TODO clear the data from the Customer ID entry widget
            self.message.set("Customer ID not found.")
"""

# The find_customer_by_name method returns all records that match the name
# The parameter first_name is a Boolean.
#       If first_name is True, search for name in the field FirstName.
#       If first_name is False, search for name in the field LastName
def find_customer_by_name(name, first_name):
    customer_db = None
    results = []
    pattern_to_match = f"%{name.lower()}%"
    try:
        # TODO:
        #  1. establish a connection to the database
        #  2. SELECT all fields from Customers that match the name to FirstName or LastName depending on first_name
        #  3. fetch the resulting data into the list named results
        conn = sqlite3.connect('customers.db')
        cur = conn.cursor()
        if first_name is True:
            cur.execute('SELECT * from Customers WHERE FirstName == ?', (pattern_to_match,))
        else:
            cur.execute('SELECT * from Customers WHERE LastName == ?', (pattern_to_match,))
        results = cur.fetchall()

    except sqlite3.Error as err:
        print('Database Error', err)
    finally:
        if customer_db is not None:
            customer_db.close()
    # Return the list of matching records
    return results


# The find_customer_by_name function returns a list of tuples containing all records that match the name
# If none are found or there is an error, an empty list is returned
def find_customer_by_id(customer_id):
    customer_db = None
    results = []
    try:
        # TODO:
        #  1. establish a connection to the database
        #  2. SELECT all fields from the Customers database that match the given customer_id
        #  3. fetch all resulting data into the list named results
        conn = sqlite3.connect('customers.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM Customers WHERE CustomerID == ?', (customer_id,))
        results = cur.fetchall()

    except sqlite3.Error as err:
        print('Database Error', err)
    finally:
        if customer_db is not None:
            customer_db.close()
    # Return the list of matching records
    return results


# Returns a string displaying all customer data in the given list of tuples from the db
def return_data_as_string(customer_list):
    customer_string = ""
    if len(customer_list) > MAX_LIST_SIZE:
        return "Too many customers matched.\nPlease narrow your search."
    else:
        try:
            for customer_id, first_name, last_name, phone, email in customer_list:
                customer_string += f"{customer_id}  {first_name} {last_name}  {phone}  {email}\n"
        except ValueError:
            print("%Program Error. Customer list in unexpected format.")
        return customer_string


# main program fires up the TK interface and instantiates the root GUI
def main():
    # first make sure we are able to access the customer database
    try:
        my_db = sqlite3.connect('customers.db')
        my_cursor = my_db.cursor()
        # define the table structure and create the table, but only if it doesn't already exist
        table_structure = """CREATE TABLE IF NOT EXISTS Customers 
                            (CustomerID INTEGER PRIMARY KEY NOT NULL, 
                             FirstName TEXT, LastName TEXT, Phone TEXT, Email TEXT)"""
        my_cursor.execute(table_structure)
        my_db.commit()
        my_db.close()

        # since we have been able to access the database (and optionally create the table)
        # we can proceed to run the GUI, so create a window and initialize the Tk library
        root = tkinter.Tk()
        # call the GUI and send it the root window
        # use _ as variable name because the variable will not be needed after instantiating GUI
        # the GUI itself will handle the remaining program logic
        _ = CrudGUI(root)
        # because the root window was initialized here, we control the mainloop from main instead of the class
        root.mainloop()
    except sqlite3.Error:
        print("%Error. Unable to access SQL database: customers.db")


MAX_LIST_SIZE = 7       # constant defining the max number of records to display in the LookGUI search
if __name__ == '__main__':
    main()
