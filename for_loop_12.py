#for loop = a statement that will execute its block of code a limited amount of times

import time #it provides time related functions

for i in range(10):
    print(i) #prints from 0 to 9

for i in range(50,100+1,2): #(starting point, ending point, step)
    print(i)

for i in "Ragosh Shrestha":
    print(i) #prints each character from the string

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1) #how long you want to sleep/pause in seconds
print("Sussy Baka!")