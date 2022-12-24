#creating a menu bar in python
from tkinter import *
from tkinter import filedialog

#from file_dialog_79 import openFile #importing from different file.
#from save_file_dialog_80 import saveFile

def openFile():
    filepath = filedialog.askopenfilename(initialdir="F:\\RAWGOSH\\Python from brocode", #configuring the initial directory
                                        title = "Open File", #changing the title of displaying window
                                        filetypes= (("text files","*.txt"), #type of file to select
                                        ("all files","*.*"))) #asks user the file path
    """print(filepath)""" #displays the file path
    
    with open(filepath,'rt') as file: # or file = open(filepath, 'r') -> both are same
        print(file.read())
    file.close()

def saveFile():
    file = filedialog.asksaveasfile(initialdir="F:\\RAWGOSH\\Python from brocode",
                                    title = "Save File",
                                    defaultextension=".txt", #creating a default extension for saving file
                                    filetypes=[ ("Text files",".txt"),
                                                ("HTML files",".html"),
                                                ("All files",".*")]) #list of other types of file

    if file is None: #to overcome the exception while mistakenly closing before saving
        return
    filetext = str(text.get(1.0,END))
    """filetext = input("Enter something to save :)")""" #to get input from the console
    file.write(filetext)
    file.close()

def copy():
    print("COPIED")

def cut():
    print("CUT")

def paste():
    print("PASTED")

def undo():
    pass

def redo():
    pass

window = Tk()

openImage = PhotoImage(file = "open.png", height=20, width=20) #to keep photo as a label for the menu
saveImage = PhotoImage(file = "save.png")
exitImage = PhotoImage(file = "exit.png")

window.title("File Dialog")
text = Text(window)
text.pack()
menubar = Menu(window)
window.config(menu=menubar) #proportionating the size of window

fileMenu = Menu(menubar,tearoff=0,font=("Conslas",12))
menubar.add_cascade(label="File",menu=fileMenu) #creating a menu named "File"
fileMenu.add_command(label="Open",command = openFile,image=openImage, compound='left') #creating labels for "File", adding image to the left of the label
fileMenu.add_command(label="Save", command = saveFile)
fileMenu.add_separator() #adding a seperator line between two labels
fileMenu.add_command(label="Exit", command = quit) #quit function is a shortcut to quit the file/program


editMenu = Menu(menubar,tearoff=0,font=("Conslas",12))
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Paste",command=paste)
editMenu.add_separator()
editMenu.add_command(label="Undo",command=undo)
editMenu.add_command(label="Redo",command=redo)




window.mainloop()
