#sorting iterables 
#sort() method = used with lists
#sort() function = used with iterables
#sort() method can only be used for list data types


gamers = ["Tyson","Kaemi","Xirena","Flow","Average"]

gamers.sort() #alphabetical order
for i in gamers:
    print(i)
print()


gamers.sort(reverse=True) #reverse alphabetical order
for i in gamers:
    print(i,end=" ")
print()

gamers = ("Tyson","Kaemi","Xirena","Flow","Average")
sorted_gamers = sorted(gamers) #this method is for tuple datatype
for i in sorted_gamers:
    print(i)
print()

#for list of tuples
gamers = [("Tyson","N",25),("Kaemi","P",23),("Xirena","A",21),("Flow","U",26),("Average","C",27)]

gamers.sort() #Sorts alphabetically according to the given names
for i in gamers:
    print(i)
print()

#to sort passing a key.
address = lambda address:address[1]
gamers.sort(key = address,reverse=True)
for i in gamers:
    print(i)
print()


#for tuple of tuples
gamers = (("Tyson","N",25),("Kaemi","P",23),("Xirena","A",21),("Flow","U",26),("Average","C",27))

age = lambda age:age[2]
sorted_gamers = sorted(gamers,key = age)
for alpha in gamers:
    print(alpha)