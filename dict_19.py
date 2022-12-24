#dictionary = A changeable, unordered collection of unique key:value pairs, It allows us to access a value quickly.

capitals = {"Nepal":"Kathmandu","Japan":"Tokyo","England":"London","India":"Delhi"} #left side is key and right side is the value.

print(capitals["Nepal"]) #prints the value which has the key "Nepal"
capitals.update({"Germany":"Berlin"}) #adds a new key and value.
capitals.update({"England":"Amsterdam"}) #updates the value using key
capitals.pop("Japan") #removes a key value pair.

print(capitals.get('Germany')) #checks whether there is the key in the dict or not.
print(capitals.keys()) #prints only keys
print(capitals.values()) #prints values only
print(capitals.items()) #prints both keys and value

for key,value in capitals.items():
    print(key,value) #prints both key and value using loop.

capitals.clear() #clears the whole dictionary
print(capitals)