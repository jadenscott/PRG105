"""
This program uses a GUI that has the user enter an amount of gallons and an amount of miles in order to calculate
miles per gallon.
"""
import tkinter
import tkinter.messagebox


class MPGCalculatorGUI:
    def __init__(self):

        # creates main window and sets title
        self.main_window = tkinter.Tk()
        self.main_window.title('MPG Calculator')

        # creates top, middle and bottom frames to group widgets
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # creates labels
        self.gallons_label = tkinter.Label(self.top_frame, text="Enter your car's tank size in gallons:")
        self.miles_label = tkinter.Label(self.middle_frame, text="Enter how many miles you've traveled:")

        # creates entry widgets
        self.gallons_entry = tkinter.Entry(self.top_frame, width=10)
        self.miles_entry = tkinter.Entry(self.middle_frame, width=10)

        # pack labels and entry widgets
        self.gallons_label.pack(side='left')
        self.gallons_entry.pack(side='left')
        self.miles_label.pack(side='left')
        self.miles_entry.pack(side='left')

        # creates button widgets for the bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame, text='Calculate', command=self.calculate)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        # pack the buttons
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack the frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        # enter the tkinter main loop
        tkinter.mainloop()

    # callback function for convert button is defined
    def calculate(self):
        # gets user input (gallons)
        gallons = float(self.gallons_entry.get())

        # gets user input (miles)
        miles = float(self.miles_entry.get())

        # calculates miles per gallon
        mpg = miles / gallons

        # displays miles per gallon in an info dialog box
        tkinter.messagebox.showinfo('Results', str(mpg) + ' miles per gallon')


# creates an instance of MPGCalculatorGUI
if __name__ == '__main__':
    mpg_calc = MPGCalculatorGUI()



