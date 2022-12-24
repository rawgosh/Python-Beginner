#lambda function = function written in one line using lambda keyword, accepts any number of arguments, useful if needed for a short period of time

#lambda parameters:expression

def double(x):
    return x*2

print(double(2))

double = lambda x:x*2 #same use as above but in one line
print(double(2)) #calls double function
print()

product = lambda x, y: x * y #for two or more than two parameters
print(product(2,3)) #passing two values in the function 
print()

full_name = lambda f_name, l_name: f_name +" "+ l_name #can be used for both string and numbers
print(full_name("Ragosh","Shrestha")) #passing string
print()

age_check = lambda age:True if age >= 18 else False
print(age_check(13))