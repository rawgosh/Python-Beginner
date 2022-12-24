#create new window in python

from tkinter import *


def create_window():
    #new_window = Toplevel() #Toplevel() -> new window 'on top' of other windows, linked to a 'bottom' window.
    new_window = Tk()
    new_window.title("Python GUI")
    
    old_window.destroy() #closes the old window

old_window = Tk() #Tk() -> new independent window

Button(old_window, text = "CREATE A NEW WINDOW", command = create_window).pack() #creating button directly without using variable

old_window.mainloop()
