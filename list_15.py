#list = used to store multiple items in a single variable

games = ["Valorant","Fortnite","GTAV","Assassins"]
print(games[0]) #accessing list data using index
print(games[3])
print()

games.append("Clash Of Clans")#adds to the list
games.remove("Assassins") #removes a data from the list
games.pop() #removes last data
games.insert(3,"PUBG") #inserts data to the desired index
games.sort() #arranges in ascending order
games.clear() #removes all the data


for i in games:
    print(i+" " ,end="")