import os #interacts with the operating system 
from tkinter import *
from tkinter import filedialog, colorchooser, font #imports tkinter packages for different classes
from tkinter .messagebox import * #contains classes for creating different message box
from tkinter .filedialog import *

def change_color():
    color = colorchooser.askcolor(title="Pick a Color")
    print(color)
    text_area.config(fg = color[1])

def change_font(*args): #accepting varying amount of arguments
    text_area.config(font = (font_name.get(), size_box.get()))

def new_file():
    window.title("Untitled") 
    text_area.delete("1.0", END) #deletes everything present inside the text area

def open_file():
    file = askopenfilename(defaultextension=".txt",file = [("All files","*.*"),("Text documents","*.txt")]) #by default text file but we can open any file

    try:
        window.title(os.path.basename(file)) #gives the title as the selected file name
        text_area.delete("1.0", END) #deletes the text from the old window
        
        file = open(file, "r") #opens the file in read format
        text_area.insert("1.0", file.read()) #inserts everything from the selected file to the text area
    
    except Exception: #for any kind of exception
        print("Couldn't read the file")
    
    finally: #this method runs in any case
        file.close()

def save_file():
    file = filedialog.asksaveasfilename(initialfile = "untitled.txt", defaultextension=".txt",filetypes = [("All Files","*.*"),("Text Documents","*.txt")]) #initialfile -> before saving the file, defaultextension -> when a extension is not given, filetypes -> what kind of file does it saves
    
    if file is None: #if nothing is saved
        return
    
    else:
        try:
            window.title(os.path.basename(file)) #changes the window name into the saved name 
            file = open(file, "w") #opens the file in write mode
            
            file.write(text_area.get("1.0",END)) #writes everything in the file from the text_area
            
        except Exception: #If the file cant be saved
            print("Couldn't save the file")
        
        finally:
            file.close()

def cut():
    text_area.event_generate("<<Cut>>") #uses generate event to cut

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

def about():
    showinfo("About this program","It is just a simple project made using Python Programming Language. It was created while practicing about tkinter and its widgets.") #shows a popup info about the program ("Title","Desired text")

def quit():
    window.destroy() #closes the window

window = Tk()
window.title("Text Editor")
file = None

window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry("{}x{}+{}+{}".format(window_width,window_height,x,y)) #centering the window screen

font_name = StringVar(window) #adds to the window
font_name.set("consolas") #default

font_size = StringVar(window)
font_size.set(25)

text_area = Text(window, font=(font_name.get(),font_size.get()))

scroll_bar = Scrollbar(text_area)

window.grid_rowconfigure(0,weight=1) #expands text area
window.grid_columnconfigure(0,weight=1)
text_area.grid(sticky=N+E+S+W) #text_area takes the most of the window

scroll_bar.pack(side = RIGHT, fill=Y) #fills vertical height of Right side completely
text_area.config(yscrollcommand=scroll_bar.set)

frame = Frame(window)
frame.grid()

color_button = Button(frame, text = "Color", command = change_color)
color_button.grid(row = 0, column = 0)

font_box = OptionMenu(frame, font_name, *font.families(), command = change_font)
font_box.grid(row = 0, column = 1)

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command = change_font)
size_box.grid(row = 0, column = 2)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label = "File", menu = file_menu)

file_menu.add_command(label = "New", command = new_file)
file_menu.add_command(label = "Open", command = open_file)
file_menu.add_command(label = "Save", command = save_file)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu = edit_menu)

edit_menu.add_command(label="Copy      (CTRL + C)",command=copy)
edit_menu.add_command(label="Cut         (CTRL + X)",command=cut)
edit_menu.add_command(label="Paste      (CTRL + V)",command=paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)


window.mainloop()