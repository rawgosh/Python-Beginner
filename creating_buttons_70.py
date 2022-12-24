from tkinter import *

count = 0 #to count how many times the user has clicked the button
def click():
    global count #globalizing the variable
    count += 1 #counting on each click
    print("You clicked ",count," times.")
    print("Why are you clicking?")

window = Tk()
photo = PhotoImage(file="g.png")
window.title("Buttons")
window.geometry("720x720")


button = Button(window,
                text="TEXT EDITOR",
                command=click, #commanding the button
                font=("Comic Sans",30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00", #color of active fg
                activebackground="black", #color of active bg
                state=ACTIVE, #status of the button
                image=photo,
                compound="bottom") #{creating the button}
button.pack() #displaying the button





window.mainloop()