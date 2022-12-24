#filter() = it creates a collection of elements from an iterable for which a function returns true
#filter(function,iterable)

#it is useful to search the results quickly


students = [("Killua",15),("Itachi",18),("Natsu",17),("Naruto",29),("Jiraiya",53)]

age = lambda data:data[1] >= 18
drink = list(filter(age,students))
for i in drink:
    print(i)