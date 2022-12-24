#grid() = geometry manager that organizes widgets in a table-like structure in a parent, arranges like in excel, we cannot use .pack()

from tkinter import *

def submit():
    print("Submitted")

window = Tk()

Label(window, text = "Enter your details", font = ("Consolas",30)).grid(row = 0 , column=0, columnspan=2)

#firstnameLabel = Label(window, text = "First Name").pack()
#firstnameEntry = Entry(window,).pack()


firstnameLabel = Label(window, text = "First Name ",width=10, bg = "cyan").grid(row = 1, column = 0) #width for all column gets adjusted
firstnameEntry = Entry(window,).grid(row = 1, column = 1)

lastnameLabel = Label(window, text = "Last Name ",bg = "pink").grid(row = 2, column = 0)
lastnameEntry = Entry(window,).grid(row = 2, column = 1)

emailLabel = Label(window, text = "Email ",bg = "orange").grid(row = 3, column = 0)
emailEntry = Entry(window,).grid(row = 3, column = 1)

Button(window, text="Submit", command = submit).grid(row = 4, column = 0,columnspan=2) #expanding the column of the button grid

window.mainloop()