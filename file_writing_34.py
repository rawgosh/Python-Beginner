#writing files in python
name = "Ragosh Shrestha\n"
with open("study.txt","w") as file: #create a file
    file.write("Ara Ara\n") #writes inside the file
    file.write(name)
    file.write("I am 18 years.")

with open("study.txt","a") as file: #append a file
    file.write("\nDaijobu?")

file = open("study.txt","r") #read a file
print(file.read())
file.close() #close a file