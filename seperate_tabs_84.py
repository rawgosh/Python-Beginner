from tkinter import *
from tkinter import ttk #imports widgets that are normally not accessible 

window = Tk()

notebook = ttk.Notebook(window) #widget that manages a collection of windows/displays

tab1 = Frame(notebook) #new frame for tab 1
tab2 = Frame(notebook) #new frame for tab 2

notebook.add(tab1, text = "Tab 1")
notebook.add(tab2, text = "Tab 2")
notebook.pack(expand = True, fill = "both") #expand to fill any space , #fill -> space on x and y axis

Label(tab1, text = "This is tab 1", width = 90, height = 30).pack() #adding a label for tab1 frame
Label(tab2, text = "This is tab 2", width = 90, height = 30).pack()

window.mainloop()