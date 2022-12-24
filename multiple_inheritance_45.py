#multiple inheritance = when a child is derived from more than one parent class

class Prey:
    def flee(self):
        print("This animal flees")

class Predator:
    def hunt(self):
        print("This animal hunts")

class Rabbit(Prey):
    pass

class Fish(Prey,Predator): #derived from two class
    pass

class Hawk(Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
fish.hunt()
hawk.hunt()
fish.flee()
