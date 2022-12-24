#entry widget -> text box that accepts a single line of user input.

from tkinter import *

def submit(): #defining a function for the command
    username = entry.get() #gets the current value of the entry box or a variable
    print("Hello "+username)
    entry.config(state=DISABLED) #disables the entry box for further use

def delete():
    entry.delete(0,END) #deletes from the index of the character to the end of the character.
    print ("Deleted")

def backspace():
    entry.delete(len(entry.get())-1,END) #getting length of the string from the entry box and deleting the last character only


window = Tk()
window.title("ENTRY BOX")

entry = Entry(window, #where we want the entrybox
            font=("consolas",20),
            fg="cyan",
            bg="Black",
            show="*")
#entry.insert(0,"password") #acts like a place holder
entry.pack(side=LEFT) #selects the side for the entry box


submit_button = Button(window,text="Submit",command=submit)
submit_button.pack(side=RIGHT) #select the side for the button

delete_button = Button(window,text="Delete",command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window,text="Backspace",command=backspace)
backspace_button.pack(side=RIGHT)


window.mainloop()

