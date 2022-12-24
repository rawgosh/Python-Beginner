#Duck typing = concept where the class of an object is less important than the methods/attributes, class type is not checked if minimum methods/attributes are present 

class Duck:

    def walk(self):
        print("This duck is walking.")

    def quack(self):
        print("This duck is quacking.")

class Chicken:

    def walk(self):
        print("This chicken is walking.")

    def quack(self):
        print("This chicken is chuckling.")

class Person:

    def catch(self,duck):
        duck.walk()
        duck.quack()
        print("You caught it!!")

duck = Duck()
chicken = Chicken()
person = Person()
person.catch(chicken)

#even though it is using duck.walk() it is printing from class Chicken which means class is not that important