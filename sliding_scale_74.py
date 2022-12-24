from tkinter import *

def submit():
    print("Your happiness level is :"+ str(scale.get())+".")

window = Tk()

happy = Label(text="😊")
happy.pack()
scale = Scale(window, #creating scale in te window
            from_=10, #starting value 
            to=0, #end value
            length=600, #length of the scale
            orient=VERTICAL, #style of the scale to display
            font=("Consolas",20),
            tickinterval=1, #adds numeric indicators for the value
            showvalue=0, #hides current value
            resolution=1, #increment of slider
            troughcolor = "blue", #colour of scale
            )
scale.set(4)
#scale.set(((scale['from']-scale['to'])/2)+scale['to']) --> always sets the scale at the middle
scale.pack()
happy = Label(text="😢")
happy.pack()
button = Button(window,
                text="submit",
                command=submit)
button.pack()


window.mainloop()