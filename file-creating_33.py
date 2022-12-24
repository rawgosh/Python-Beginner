#creating a file

with open("text.txt","w") as file: #it will close the file automatically
    file.write("Hello guys!\n")
    file.write("I am from the file.")

with open("text.txt") as file: #by default it is in read mode
    print(file.read()) #reads from the file

try:
    with open("test.tx") as file:
        print(file.read())
except FileNotFoundError:
    print("That file is missing")