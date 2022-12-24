from tkinter import *

def doSomething(event): #requires the event as a parameter
    print("You clicked: "+ event.keysym) #displaying whic key is pressed in the console
    label.config(text = "You clicked: "+ event.keysym)

window = Tk()

#window.bind(event,function)
window.bind("<Return>",doSomething)
window.bind("<Key>",doSomething) #for all key

label = Label(window, font=("Consolas",50))
label.pack()

window.mainloop()