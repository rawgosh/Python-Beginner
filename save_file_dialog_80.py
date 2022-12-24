from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="F:\\RAWGOSH\\Python from brocode",
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


window = Tk()

text = Text(window)
text.pack()
button = Button(window, text = "Save", command = saveFile)
button.pack()


window.mainloop()