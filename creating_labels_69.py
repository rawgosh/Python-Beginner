from tkinter import *
# label = an area widget that holds text and/or image within a window

window = Tk()
window.geometry("1300x700") #automatically the width of the window increases with the increase in text or images.
photo = PhotoImage(file = "g.png")
label = Label(window,
            text = "Hello World 💻", #text
            font=('consolas',15,'bold'), #font details
            fg = 'black', #foreground color
            bg = 'white', #background color
            relief=SUNKEN, #border type : SUNKEN, RAISED
            bd=10, #border width
            padx=20, #adds space in x-axis 
            pady=20,  #adds space in y-axis
            image=photo, #adding image in the window
            compound='top') #{creating label} """placing the image with respect to the text"""


label.pack() #using the label in the window
#label.place(x=0,y=0) #uses label according to the coordinate



window.config(background="cyan")
window.mainloop()



#6:23:37
