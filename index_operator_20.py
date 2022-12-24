#index operator [] = gives access to a sequence's element (str,list,tuples)

name = "ragosh shrestha"

if(name[0].islower()): #checks whether the strings 0 index is lower case or not
    name = name.capitalize()

print(name)

first_name = name[0:6].upper() #slicing
last_name = name[7:].lower()
print(first_name)
print(last_name)