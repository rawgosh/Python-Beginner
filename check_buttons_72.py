from tkinter import *

def display():
    if(x.get()==1): #getting value of x from the checkbox
        print("You agree")
    else:
        print("Why didn't you agree?")

window = Tk()
photo = PhotoImage(file="g.png",height=100,width=100)
x = IntVar() #integer variable

check_button=Checkbutton(window,
                        text = "I agree!",
                        variable = x, #associating the check box with the variable
                        onvalue = 1, #value when the checkbox is checked
                        offvalue = 0, #we can even use boolean value or string value
                        command = display,
                        font=("Arial",20),
                        fg="green",
                        bg = "black",
                        activebackground="black",
                        activeforeground="green",
                        padx = 20, #padding
                        pady = 30,
                        image = photo,
                        compound="right")
check_button.pack()

window.mainloop()


