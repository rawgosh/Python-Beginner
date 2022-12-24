# assigning a function to a variable

def learn():
    print("Studying to fullest")

print(learn) #displays the memory address of the function


study = learn #assigning function 
study()


display = print
display("I haven't written print to display this")