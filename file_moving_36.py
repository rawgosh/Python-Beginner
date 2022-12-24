#moving files

from genericpath import exists
import os

source = "copy.txt"
destination = "F:\\RAWGOSH\\copy.txt"

try:
    if os.path.exists(destination):
        print("The is already the file with same name")
    else:
        os.replace(source,destination) #moves the file located in the source to the destination path
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found.")

#it cannot move file from one disk drive to another disk drive.
#we can even move a folder/directory within a same disk drive.