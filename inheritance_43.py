#inheritance

class Animal: #parent class
    alive = True

    def eat(self):
        print("This animal is eating.")
    
    def sleep(self):
        print("This animal is sleeping.")

class Condor(Animal): #class condor will have access to the class animal
    def fly(self):
        print("This bird is flying ")

class Dog(Animal): #child class
    def run(self):
        print("This dog is running.")

class Elephant(Animal):
    def hide(self):
        print("This animal cant hide.")


condor = Condor()
dog = Dog()
elephant = Elephant()

print(condor.alive)
dog.sleep() #accessing the method
elephant.eat()
elephant.hide()