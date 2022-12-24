#file detection
from genericpath import isdir #importing 'isdir' function
import os #function for creating or removing a directory,fetching its content, changing and identifying the current directory etc.

path = "C:\\Users\\Hp\\Desktop\\learning"

if os.path.exists(path): #checks whether the passed path exists or not
    print("That location exists.")
    if os.path.isfile(path): #checks whether it is a file or not
        print("That's a file")
    elif os.path.isdir(path): #checks if it is a directory/folder
        print("That's a directory!")
else: #if nothing is satisfied this block runs
    print("That location is unknown")
