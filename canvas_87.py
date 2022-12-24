#canvas = widget that is used to draw graphs, plots, images in a window

from tkinter import *

window = Tk()

canvas = Canvas(window, height = 500, width = 500) #creating a canvas
canvas.create_line(0,0,500,500, fill = 'red', width = 20) #(x1,y1,x2,y2)
canvas.create_line(0,500,500,0, fill = 'red', width = 20) #creating a straight line
canvas.create_rectangle(50,50,450,450, fill = "cyan") #creating a square or rectangle
canvas.create_polygon(250,50,50,450,450,450, fill = 'purple', outline = 'black' ,width = 5) #taking three points of polygon, outline -> border
canvas.create_arc(50,50,450,450,fill = "red",style = ARC, start = 270, extent = 180) #starts from 270 degree and extent to 180 degree

canvas.pack()

window.mainloop()