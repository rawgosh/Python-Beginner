# module = file containing python code such as functions, classes etc. used to seperate program into parts.

import module_file as mod #imports from the module_file with a nickname 'mod'

mod.que() #accessing the que() function inside the module_file
mod.ans()

print()

#from module_file import * #imports all the module
from module_file import que,ans #another way of importing in short way.
que() #calling a function
ans()

help("modules") #to display all the modules present