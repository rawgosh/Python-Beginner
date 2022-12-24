#method overwriting

class Animal: #parent class

    def eat(self): #eat(self) is a method signature
        print("This animal is eating")


class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating carrot.")

rabbit = Rabbit()
rabbit.eat() # in python object will use the method which is closely accociated with itself first before relying on the class that it inherits from.