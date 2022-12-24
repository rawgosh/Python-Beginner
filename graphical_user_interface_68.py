from tkinter import * # tkinter is a GUI module, and '*' imports everything from the module

# widgets = GUI elements: buttons, labels, images
# windows = serves as a container to hold or contain the widgets

window = Tk() #instantiate an instance of a window
window.geometry("1300x788") #width and height
window.title("Ragosh Shrestha's Window") #title for the window
icon = PhotoImage(file = 'logo-social.png') #modifying the image into compatiable icon
window.iconphoto(True,icon) #using the icon in the window
window.config(background="#3F2554") #changing the background color



window.mainloop() #place window on computer screen, listen for events







