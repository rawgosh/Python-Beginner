#deleting files

import os

import shutil #to delete a directory that contains file

path = "copy.txt"
e_folder = "new"
folder = "hey"

try:
    os.remove(path) #deletes the file within the destination path
    os.rmdir(e_folder) #deletes an empty directory
    shutil.rmtree(folder) #deletes a directory containing files
except FileNotFoundError:
    print("There is no such files")
except PermissionError:
    print("No permission to delete ")
except OSError:
    print("Function error to delete")
else:
    print(path+ " and "+folder+" was deleted.")