import random #accessing random module

x = random.randint(1,6) #random number from 1 - 6
y = random.random() #random number from 0 - 1
print(x)
print(y)

list = ["Rock","Paper","Scissors"]
z = random.choice(list) #chooses a random value from the list
print(z)

cards = ["A",2,3,4,5,6,7,8,9,"J","Q","K"]
random.shuffle(cards) #Shuffels the value inside of the list
print(cards)