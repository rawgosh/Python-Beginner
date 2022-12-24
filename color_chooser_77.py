from tkinter import *
from tkinter import colorchooser #submodule

def click():
    color = colorchooser.askcolor() #asking user to pick a color
    print(color)
    colorHex = color[1] #assigning the hex value of the color
    print(colorHex)
    window.config(bg = colorHex) #changes background according to the picked color
    #window.config(bg = colorchooser.askcolor()[1])

window = Tk()
window.geometry("500x500")


button = Button(window,text = "pick", command = click)
button.pack()




window.mainloop()