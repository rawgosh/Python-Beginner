#higher order functions = functions that either, accepts a function as an argument or, returns a function

def office(text):
    return text.upper()

def hall(text):
    return text.lower()

def school(func): #school() is a higher order function #func is just a parameter 
    text = func("student") #assigning function to a variable
    print(text)

school(office) #uses office function


print()
print()


def divisor(x): #x will be 2 unless we reasign its value
    def dividend(y):
        return y/x
    return dividend

divide = divisor(2) #passes the divisor
print(divide(10)) #it passes the dividend
