#*args parameter = parameter that will pack all arguments into a tuple, useful so that a function can accept a varying amount of variable.



def multiple_variable(*args): #we can use any thing in place of args.
    sum = 0
    for i in args:
        sum += i
    return sum

print(multiple_variable(1,2,3,4,5,6))
