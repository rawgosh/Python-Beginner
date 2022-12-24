from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p") #gets local time => hour, min, sec, AM/PM
    time_label.config(text = time_string)
    
    day_string = strftime("%A") #getting day
    day_label.config(text = day_string)
    
    date_string = strftime("%B %d, %Y") #getting full date
    date_label.config(text = date_string)
    
    time_label.after(1000,update) #updates the label after each second or after every 1000 millisecond
    #window.after(1000,update) => we can use window function as well

window = Tk()
window.title("Digital Clock")

time_label = Label(window,font=("Arial",50), fg = "green", bg = "black")
time_label.pack()
day_label = Label(window,font=("Ink Free",30), fg = "cyan", bg = "black")
day_label.pack()
date_label = Label(window,font=("Ink Free",40), fg = "yellow", bg = "black")
date_label.pack()

update()

window.mainloop()