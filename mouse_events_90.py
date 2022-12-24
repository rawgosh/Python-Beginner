from tkinter import *

def doSomething(event):
    print("Your coordinate is :"+str(event.x)+", "+str(event.y))

window = Tk()

window.bind("<Button-1>",doSomething) #left mouse click
window.bind("<Button-2>",doSomething) #scroll wheel click
window.bind("<Button-3>",doSomething) #right mouse click
window.bind("<ButtonRelease>",doSomething) #when button is released
window.bind("<Enter>",doSomething) #when cursor enters the window
window.bind("<Leave>",doSomething) #when cursor leaves the window
window.bind("<Motion>",doSomething) #when the cursor is in motion



window.mainloop()