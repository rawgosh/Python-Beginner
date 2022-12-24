#if statement = a block of code will execute if its condition is true

age = int(input("Enter your age :"))

if age >= 100:
    print("You are too old geezer!")
elif age >= 18:
    print("Too much stress to be adult!")
elif age < 0:
    print("You are from another universe I guess.1")
else:
    print("Grow up child!")