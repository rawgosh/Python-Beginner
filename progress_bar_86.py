from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB = 100
    download = 0
    speed = 1
    while (download<GB):
        time.sleep(0.05) #program sleeps before starting
        progressBar['value'] += (speed / GB) * 100 #determining the rate of increase of progress bar
        download += 1 #by what value does the progress bar increases
        percent.set(str(int((download/GB)*100))+"%") #displaying the label in percentage
        text.set(str(download) + "/" + str(GB) + " GB completed") #displaying the completed text
        window.update_idletasks() #updating the window after each iteration

window = Tk()

percent = StringVar() #creating a string variable
text = StringVar()

progressBar = Progressbar(window, orient=HORIZONTAL, length = 300) #creating a progressbar
progressBar.pack(pady = 20)

percentLabel = Label(window, textvariable=percent).pack() #displaying a label;
taskLabel = Label(window, textvariable=text).pack()

Button(window, text = "Download", command = start).pack() #displaying a button 

window.mainloop()

