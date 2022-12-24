#accepting user input

name = input("What is your name?: ") #when we take input from the user it is always in string data type.
age = int(input("How young are you?: "))
height = float(input("How tall are you ?(In cm):"))


age = 100 - age


print("Hello "+name)
print("You are "+str(age)+" years away to reach 100 💀")
print("Just "+str(height)+"cm??? Bro You too short 😢")

