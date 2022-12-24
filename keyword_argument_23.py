# keyword argument = arguments preceded by an identifier when we pass them to a function, The order of the arguments doesn't matter, unlike positional arguments Python knows the names of the arguments that our function receives.

def student(name,age,add):
    print("Hello "+name+". You are from "+add+" Who is "+str(age)+" years old.")

student(name = "Ragosh",age = 18,add = "Gorkha")