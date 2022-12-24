#number.format() 

num = 999999

print("The number pi is {:.2f}".format(num)) #displays first two after decimal portion.
print("The number pi is {:,}".format(num)) #adds comma to thousands place
print("The number pi is {:b}".format(num)) #changes into binaray
print("The number pi is {:o}".format(num)) #changes into octal
print("The number pi is {:x}".format(num)) #changes into hexadecimal, lowercase 'x' to display in lowercase and vice versa.
print("The number pi is {:e}".format(num)) #changes into sintefic format
