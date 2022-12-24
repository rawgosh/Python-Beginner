#listbox -> A listing of selectable text items within its own container


from msilib.schema import ListBox
from tkinter import *

def order():
    
    game = [] #creating an empty list 
    for index in listbox.curselection(): #loops for each items selected
        game.insert(index,listbox.get(index)) #inserts in the empty list
    
    """print("Do you even play " +listbox.get(listbox.curselection())+"?")""" #it gets the current selection from the listbox [listbox.get() -> fetches the data] [listbox.curselection() -> provides the selected value.]
    print("Your games :")
    for index in game:
        print(index) #prints the items present in the index
    
def add():
    listbox.insert(listbox.size(),entryBox.get())#inserts a new data in the listbox which is typed in the entry box
    listbox.config(height=listbox.size())

def delete():
    
    for index in reversed(listbox.curselection()): #it is reversed because the indexes are changing so it works from last index to 0
        listbox.delete(index)
    
    """listbox.delete(listbox.curselection())""" #deletes the recently selected data from the listbox
    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window,
                bg = 'Cyan',
                fg = 'green',
                font=("Consolas",20),
                width = 10,
                selectmode = MULTIPLE, #selects multiple items from the listbox
                )

listbox.pack()

listbox.insert(1,"Valorant") #inserting value to the listbox according to the index
listbox.insert(2,"Fortnite")
listbox.insert(3,"Apex")
listbox.insert(4,"Overwatch")
listbox.insert(5,"GTA")
listbox.insert(6,"Rocket")


listbox.config(height=listbox.size()) # it is used when we want to change something.

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window,
                    text = "Order",
                    command= order)
submitButton.pack()
addButton = Button(window,
                    text = "Add",
                    command= add)
addButton.pack()

deleteButton = Button(window,
                    text="Delete",
                    command = delete)
deleteButton.pack()


window.mainloop()