# zip(*iterables) = aggregate elements from teo or more iterables (list,tuple,sets,etc), it creates a zip object with paired elements stored in tuples for each element

usernames = ["Rawgosh","Inej","Man"]
passwords = ("ragosh","pure","woman")

users = list(zip(usernames, passwords))


print(type(users))
print()
print("(Username, Password)")
for i in users:
    print(i)


print()
usernames = ["Rawgosh","Inej","Man"]
passwords = ("ragosh","pure","woman")
users = dict(zip(usernames, passwords))


print(type(users))
print()
print("(Username, Password)")
for key,value in users.items():
    print(key+" : "+value)


print()
usernames = ["Rawgosh","Inej","Man"]
passwords = ("ragosh","pure","woman")
login_date = ["1/1/2022","1/2/2022","1/3/2023"]

users = zip(usernames,passwords,login_date)
print(type(users))
for i in users:
    print(i)