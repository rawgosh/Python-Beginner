#list comprehension = it is a way to create a new list with less syntax,it can mimic certain lambda functions, it is easier to read
#list = [expression for item in iterable]
#list = [expression for item in iterable if conditional]
#list = [expression if/else for item in iterable]

square = [] #empty list
for i in range (1,11): #looping
    square.append(i*i) #what the loop should do
print(square)


#same program as above but simple
square = [i*i for i in range(1,11)]
print(square)

#filtering student grade
students = [100,90,80,70,60,40,30]
passed_students = list(filter(lambda x:x>=40,students)) #checking the passed students
print(passed_students)

passed_students = [i if i >= 40 else "Failed" for i in students ] #using if/else statement in the list comprehension
print(passed_students)