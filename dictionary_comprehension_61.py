#dictionary comprehension = it creates dictionaries using an expression, it can replace loops and certain lambda function

#dict = {key:expression for (key,value) in iterable}
#dict = {key:expression for (key,value) in iterable if conditional}
#dict = {key:(if/else) for (key,value) in iterable}
#dict = {key:function(value) for (key,value) in iterable}

cities_in_F = {'Gorkha':89, 'Kathmandu':95, 'Chitwan':105, 'Mustang':56}

cities_in_C = {key:round((value-32)*(5/9)) for (key,value) in cities_in_F.items()} #it converts the temperature into celsius
print(cities_in_C)

#if conditional method
weather = {'Gorkha':'Sunny','Kathmandu':'Foggy','Chitwan':'Sunny','Mustang':'Cloudy'}

district = {key:value for (key,value) in weather.items() if value=="Sunny"} #it creates a different dictionary ehich holds the desired value.
print(district)


#using if/else method
cities_in_F = {'Gorkha':89, 'Kathmandu':95, 'Chitwan':105, 'Mustang':56}

desc_cities = {key:("Warm" if value >=60 else "Cold") for (key,value) in cities_in_F.items()}
print(desc_cities)


#using function(value) method
def check_temp(value):
    if value >= 80:
        return "Hot"
    elif 79 >= value >= 60:
        return "Warm"
    else:
        return "Cold"
cities_in_F = {'Gorkha':89, 'Kathmandu':95, 'Chitwan':105, 'Mustang':56}

desc_cities = {key:check_temp(value) for (key,value) in cities_in_F.items()}
print(desc_cities)