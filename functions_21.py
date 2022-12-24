#functions = a block of code which is executed only when it is called.

def student(name,age): #function defining
    print("Good morning "+name)
    print("You are "+str(age)+" years old")


my_name = input("Enter your name :")
student(my_name,18) #function calling