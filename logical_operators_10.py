#logical operators (and,or,not) = used to check i two or more conditional statement

temp = int(input("What is the temperature outside?: "))

if not(temp >= 0 and temp <= 30):
    print("The temperature is really bad :(")
    print("Stay in!!!")
elif not(temp < 0 or temp > 30):
    print("Its normal I guess.")
    print("You can enjoy the day")