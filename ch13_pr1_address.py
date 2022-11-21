"""
This program uses a GUI to display a name and address when a button is clicked.
"""
import tkinter


class MyGUI:
    def __init__(self):
        # creates main window and sets title
        self.main_window = tkinter.Tk()
        self.main_window.title('Name and Address Problem')

        # creates StringVar objects to display name and address
        self.name_value = tkinter.StringVar()
        self.street_value = tkinter.StringVar()
        self.csz_value = tkinter.StringVar()

        # creates a top and bottom frame
        self.info_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # creates the label widgets associated with the StringVar objects
        self.name_label = tkinter.Label(self.info_frame, textvariable=self.name_value)
        self.street_label = tkinter.Label(self.info_frame, textvariable=self.street_value)
        self.csz_label = tkinter.Label(self.info_frame, textvariable=self.csz_value)

        # pack the labels
        self.name_label.pack()
        self.street_label.pack()
        self.csz_label.pack()

        # creates button widgets
        self.show_info_button = tkinter.Button(self.button_frame, text='Show Info', command=self.show_info)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)

        # pack the buttons
        self.show_info_button.pack(side='left')
        self.quit_button.pack(side='right')

        # pack the frames
        self.info_frame.pack()
        self.button_frame.pack()

        # enters tkinter main loop
        tkinter.mainloop()

    # callback function definition for show_info_button
    def show_info(self):
        self.name_value.set('Jaden Winterpacht')
        self.street_value.set('8900 Northwest Hwy #14')
        self.csz_value.set('Crystal Lake, IL 60012')


# instantiates MyGUI class
if __name__ == '__main__':
    my_gui = MyGUI()

