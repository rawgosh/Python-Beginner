#set = collection which is unordered, unindexed, no duplicate

from re import sub


games = {"Valorant","GTAV","Clash Of Clans","GTAV","GTAV"} #only one GTAV gets print

for i in games:
    print(i)
print()


games.add("PUBG") #adds data to the set
games.remove("GTAV") #removes a data from the set
games.clear() #clears the whole set

for i in games:
    print(i)


games = {"Valorant","GTAV","Clash Of Clans","GTAV","GTAV"}
subject = {"English","Maths","Science","Computer"}
subject.update(games) #adds two sets together

print(subject)
print()

student = games.union(subject) #adds two sets into a new set
for i in student:
    print(i)
print()


print(subject.difference(games)) #checks what set subject has and not set games.
print(subject.intersection(games)) #checks what is common beetween two sets.


