#tuple = collection which are ordered and unchangeable, used to group together the related data

student = ("Ragosh",18,"Gorkha")

print(student.count("Ragosh")) #counts the data
print(student.index(18)) #returns the index of the data
print()

for x in student:
    print(str(x)+" ",end="")
print()

if 18 in student:
    print("Adult!")