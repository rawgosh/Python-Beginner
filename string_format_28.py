# str.format()  = optional method that gives users more control when displaying output

name = "Ragosh Shrestha"
age = 18

print("My name is "+name+". I am "+str(age)+" years.")
print("My name is {}. I am {} years.".format(name,19)) # curly braces works as a placeholder for a value or a variable.
print("My name is {1}. I am {0} years.".format(name,"19")) # positional arguments, the variable or value gets into the place holder according to the index.
print("My name is {age}. I am {name} years.".format(name = "Cool",age = 19)) #keyword argument, we can use the same index multiple time.


text = "The {} sides of a {}."
print(text.format("bright","me"))

name = "Ragosh"
print("Hello! My name is {:10} Nice to know you".format("Ragosh")) #padding
print("Hello! My name is {:<10} Nice to know you".format("Ragosh")) #left aligns the  value, It is by defult
print("Hello! My name is {:>10} Nice to know you".format(name)) #right aligns the value.
print("Hello! My name is {:^10} Nice to know you".format(name)) #center align


#no space allowed inside the string variable.
