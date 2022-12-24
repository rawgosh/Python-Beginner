from tkinter import *

def drag(event):
    widget = event.widget #gets widget of the event we are using, here it takes the label as a widget
    widget.startX = event.x
    widget.startY = event.y


def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x #label.winfo_x() -> gets the top left coordinate of our label relative to the window that we are in
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)

window = Tk()
window.geometry("600x600")
label = Label(window, bg = "cyan", height=10,width=20)
label.place(x=0,y=0)
label2 = Label(window, bg = "red", height=10,width=20)
label2.place(x=200,y=200)

label.bind("<Button-1>",drag)
label.bind("<B1-Motion>",drag_motion) #when left button is pressed and hold and moved

label2.bind("<Button-1>",drag)
label2.bind("<B1-Motion>",drag_motion)

window.mainloop()