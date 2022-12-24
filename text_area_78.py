#text widget = functions like a text area, you can enter multiple line of text
from tkinter import *

def submit():
    string = text.get("1.0",END) #it recieves the text from the very first index to the End of the file.
    print(string)
window  = Tk()

text = Text(window, #creating a text area
            bg = "light yellow",
            font = ("Ink Free",18),
            width = 20,
            height = 20,
            padx = 10,
            pady = 10,
            fg = "violet")
text.pack() #displaying the text area

button = Button(window, text = "Submit", command = submit)
button.pack()

window.mainloop()