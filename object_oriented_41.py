#object oriented programming

#object -> It is an instance of a class.

class Game:


    def play(self): #it refers to the object that is using this method
        print(game.name+" is fun to play!") #we can write the variable name or self method.
    def lag(self): #we need to pass self in order to execute the method
        print(self.name+" has lagged.")

    def __init__(self,name,mode,date,conn): #no need to pass in self because it is done automatically
        self.name = name
        self.mode = mode
        self.date = date
        self.conn = conn

game = Game("Valorant","Multiplayer","2020","Required") #it holds the class value

print(game.name)
print(game.mode)
print(game.date)
print(game.conn)

game.play()
game.lag()