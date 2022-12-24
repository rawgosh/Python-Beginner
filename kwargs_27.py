# **kwargs = parameter that will pack all arguments into a dictionary, useful so that a function can accept a varying amount of keyword arguments.

def keyword_argu(**kwargs):
    for key,value in kwargs.items():
        print(value,end=" ")

keyword_argu(name = "Ragosh Shrestha", add = "Gorkha", age = 18) #keyword arguments