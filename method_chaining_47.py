#method chaining = calling multiple methods sequentially, each call performs an action on the same object and returns self

class Car:

    def turn_on(self):
        print("You start the car.")
        return self
    def drive(self):
        print("You drive the car.")
        return self
    def brake(self):
        print("You step on the brake.")
        return self
    def turn_off(self):
        print("You stop the car.")
        return self


car = Car() #creating object
car.turn_on().drive().brake().turn_off() #python needs a return for chaining a function

