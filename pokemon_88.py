from tkinter import *

window = Tk()

canvas = Canvas(window,height=500,width=500)
canvas.create_arc(5,5,495,495,fill = "red", extent = 180, width = 2)
canvas.create_arc(5,5,495,495,fill = "white", start = 180, extent = 180, width = 2)
canvas.create_line(5,250,495,250,width = 10)
canvas.create_oval(180,180,320,320, width = 15) #creating a oval with two fixed point from the centre
canvas.create_oval(185,185,315,315, fill = "white")
canvas.create_oval(205,205,295,295, fill = "white",width = 0.1)

canvas.pack()


window.mainloop()