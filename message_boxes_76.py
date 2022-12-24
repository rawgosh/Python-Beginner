from tkinter import *
from tkinter import messagebox #imports messagebox library


def click():
    messagebox.showinfo(title = "info", message = "These are useful commands.", icon = "error") #displays an info message box
    
    #while(True): -> infinite loop
    messagebox.showwarning(title = "warn", message = "These requires patience.") #displays a warning mesage box
    
    messagebox.showerror(title = "error", message = "ERROR 404!") #displays an error message box
    
    if messagebox.askokcancel(title = "ask ok cancel", message = "Do you need it?"): #asks ok or cancel and gives ans in boolean
        print("Congrats")
    else:
        print("See yaaa!")
    
    if messagebox.askretrycancel(title = "ask retry cancel", message = "Do you need to retry it?"): #asks retry or cancel and gives ans in boolean
        print("Quest acomplished")
    else:
        print("See yaaa!")
    
    if messagebox.askyesno(title = "Yes / No", message = "Are you happy?"): #asks yes or no and gives ans in boolean
        print("Keep it up!")
    else:
        print("Why bro?")
    
    ans = messagebox.askquestion(title = "ask question", message = "Is python better?") #asks question and gives ans as Yes or No.
    if (ans == "yes"):
        print("Yess Python built diff.")
    else:
        print("Check your mind.")
    
    ans = messagebox.askyesnocancel(title = "yes/no/cancel", message = "Wanna play?") #asks yes or no or cancel and gives ans in boolean
    if (ans == True):
        print("What you want to play?")
    elif(ans == False):
        print("Why are you here?")
    else:
        print("Answer me quick.")

window = Tk()
window.title("hello")
button = Button(window,command = click, text = "CLICK ME!")

button.pack()


window.mainloop()