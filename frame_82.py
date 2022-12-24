#Frame = a rectangular container to group and hold the widgets

from tkinter import *

window = Tk()

frame = Frame(window, bg = "cyan", bd = 4, relief = RAISED) #creating a frame inside a window
frame.pack(side = RIGHT)
#frame.place(x = 20, y = 50) -> displaying according to the coordinates

Button(frame, text = "W", font = ("Sans Sherif",28), width = 3).pack(side = TOP)
Button(frame, text = "A", font = ("Sans Sherif",28), width = 3).pack(side = LEFT)
Button(frame, text = "S", font = ("Sans Sherif",28), width = 3).pack(side = LEFT)
Button(frame, text = "D", font = ("Sans Sherif",28), width = 3).pack(side = LEFT)

window.mainloop()