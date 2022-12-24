#multi-level inheritance = when a derived class inherits another derived class

class Organism: #parent class
    alive = True

class Animal(Organism): #child class

    def eat(self):
        print("This animal is eating")

class Dog(Animal): #grandchild class
    def bark(self):
        print("Barks!")

dog = Dog()
dog.bark()  #inherited from dog class
dog.eat()   #inherited from animal class
print(dog.alive)    #inherited from organism class