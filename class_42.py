from car import Car

car_1 = Car("Bugati","Chiron",2020,"Black")
car_2 = Car("Audi","R8",2019,"Matte")

Car.wheels = 2 #changes all the instance variable
car_1.wheels = 2
print(car_1.wheels)#accesing class variable
print(car_2.wheels)
print(Car.wheels)