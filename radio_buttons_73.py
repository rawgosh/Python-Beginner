# radio buttons -> similar to checkbox, but you can only select one from a group

from tkinter import *

food = ["Burger","Pizza","Coffee"] #creating a list 


def order():
    if(x.get()==0):
        print("OHHH! You like Burger.")
    elif(x.get()==1):
        print("OHHH! You like Pizza.")
    elif(x.get()==2):
        print("OHHH! You like Coffee.")
    else:
        print("Do you even like any thing?")
window = Tk()

burgerPhoto = PhotoImage(file="burger.png")
pizzaPhoto = PhotoImage(file="pizza.png")
coffeePhoto = PhotoImage(file="coffee.png")
foodPhoto = [burgerPhoto,pizzaPhoto,coffeePhoto] #list of the images

x = IntVar() #holds an integer object

for index in range(len(food)): #loops from index of the list to the end of the list

    radio = Radiobutton(window,
                        text=food[index], #adds text to the radiobuttons from the list
                        variable=x, #groups radiobutton together if the share the same variable 
                        value = index, #assigns each radiouttons a different value
                        font = ("Impact",30),
                        fg="black",
                        padx = 25,
                        image=foodPhoto[index],#uses images in the radiobuttons according to the index
                        compound="left",
                        indicatoron=0, #eliminate circle indicators, creates a push button
                        width=200, #sets the width of the radiobuttons
                        command=order, #set command of radiobutton to function
                        )
    radio.pack(anchor=W) #displays on west




window.mainloop()


