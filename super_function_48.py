#super() = function used to give access to the methods of a parent class. returns a temporary object of a parent class when used.


class Rectangle: #parent class
    def __init__(self,length,breadth): #The self is used to represent the instance of the class
        self.length = length
        self.breadth = breadth

class Square(Rectangle):

    def __init__(self,length,breadth): #The self is used to represent the instance of the class
        super().__init__(length,breadth) #accessing the similarities using super function
    
    def area(self):
        return self.length * self.breadth

class Cube(Rectangle):
    def __init__(self,length,breadth,height):
        super().__init__(length,breadth)
        self.height = height
    
    def volume(self):
        return self.length * self.breadth * self.height

square = Square(2,2)
cube = Cube(3,3,3)

print(square.area()) #prints the returned value by the function
print(cube.volume())