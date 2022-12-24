#walrus operator = assigns value to variables as part of a larger expression ( := )

"""happy = True
print(happy)

print(happy := True)""" #using the walrus operator


foods = list()
"""while True:
    food = input("Enter food name :")
    if food == "quit":
        break
    foods.append(food)"""

while food := input("What food do you like? :") != "quit": #same as above but in a single line.
    foods.append(food)