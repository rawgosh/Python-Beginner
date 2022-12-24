from tkinter import *

def move_up(event):
    canvas.move(mycar,0,-10) #moves the image inside the canvas up
def move_down(event):
    canvas.move(mycar,0,+10) #moves the image inside the canvas down
def move_left(event):
    canvas.move(mycar,-10,0) #moves the image inside the canvas left
def move_right(event):
    canvas.move(mycar,10,0) #moves the image inside the canvas right
window = Tk()

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)
window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)

canvas = Canvas(window, height=500, width=500)
canvas.pack()

car = PhotoImage(file = "car.png")
car = car.subsample(10,10)

mycar = canvas.create_image(0,0,image = car,anchor=NW) #anchor sets the position

window.mainloop()