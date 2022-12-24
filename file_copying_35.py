#copying files

#copyfile() = copies contents of a file
#copy() = copyfile() + permission mode + destination can be a directory
#copy2() = copy() + copies metadata {file's creation and modification time}

import shutil #access to the function to copy a file

shutil.copyfile("text.txt","copy.txt") # source , destination, we can even keep a path destination


