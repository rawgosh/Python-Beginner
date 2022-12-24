from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="F:\\RAWGOSH\\Python from brocode", #configuring the initial directory
                                        title = "Open File", #changing the title of displaying window
                                        filetypes= (("text files","*.txt"), #type of file to select
                                        ("all files","*.*"))) #asks user the file path
    """print(filepath)""" #displays the file path
    
    with open(filepath,'rt') as file: # or file = open(filepath, 'r') -> both are same
        print(file.read())
    file.close()


window = Tk()
button = Button(window, text = "Click", command = openFile)
button.pack()
window.mainloop()

#creating a window to access the file path with just a button click
