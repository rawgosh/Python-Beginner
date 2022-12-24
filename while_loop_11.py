#loop = repetition of the code

#while loop = a statement that will execute it's block of code as long as it's condition remains true

#while 1 == 1: #infinite loop
#    print("This PC is hacked!")

name = ""
while len(name) == 0:
    name = input("Enter your name: ")
print("Hello "+name)

name = None
while not name:
    name = input("Enter your name: ")
print("Hii "+name)