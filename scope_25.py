#scope = The region that a variable is recognized. A variable is only available from inside the region it is created. Global and Local are two version of variable.

subject_name = "Computer science" #global variable (available both inside and outside the function.)

def student():
    while True: #loops forever until the break statement is satisfied
        student_name = input("Enter your name :") #local variable (only available inside of the function.)
        if student_name != "":
            break
    print("Hello "+student_name)
    print("You are a "+subject_name+" student.")

student()
