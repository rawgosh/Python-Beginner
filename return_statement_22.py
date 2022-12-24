#return statement = Functions sends Python values/objects back to the caller. These values/objects are known as the function's return value

def area(length,breadth):
    area = length * breadth
    return area #returns the value to the caller

length = int(input("Enter a length :"))
breadth = int(input("Enter a breadth :"))
a = area(length,breadth) #calls the function
print("Area is ",a)