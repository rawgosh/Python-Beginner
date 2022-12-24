#abstract class = a class which contains one or more abstract methods.
#abstract method = a method that has a decleration butb does not have an implementation.

#it prevents a user from creating an object of that class, compels a user to override abstract methods in a child class.

from abc import ABC,abstractclassmethod

class Vehicle(ABC): #making abstract class
    @abstractclassmethod
    def go(self): #this function is required in ever child class that inherits the Vehicle class unless the code doesnt execute.  and passes "TypeError: Can't instantiate abstract class Car with abstract method go" such error
        pass
    
    @abstractclassmethod
    def stop(self):
        pass
class Car(Vehicle):
    def go(self):
        print("Wow! You are driving a car.")
    
    def stop(self):
        print("Your Car has stopped")


class Motorcycle(Vehicle):
    def go(self):
        print("Wow! You are driving a motorcycle.")
    
    def stop(self):
        print("Your motorcycle has stopped")

#vehicle = Vehicle() #cant create this object as Vehicle is an abstract class which is not present in real world.
car = Car()
motercycle = Motorcycle()

#vehicle.go() 
car.go()
motercycle.stop()
