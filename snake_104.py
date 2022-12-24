from tkinter import *
import random

GAME_WIDTH = 700 #width of the canvas
GAME_HEIGHT = 600 #height of the canvas
SPEED = 50 #speed of the snake, how fast the canvas updates
SPACE_SIZE = 20 #how large are the item in the games like food, snake body parts.
BODY_PARTS = 3 #how many at the beginning
SNAKE_COLOR = "blue"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "green"

class Snake:
    
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0,0]) #starting point for the snake body
        
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x,y, x+SPACE_SIZE, y+SPACE_SIZE, fill = SNAKE_COLOR, tag = "snake") #creating a rectangular body of the snake
            self.squares.append(square) #adding new square in the list
        

class Food:
    
    def __init__(self):
        
        x = random.randint(0,int(GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE #range for the space where food can be placed, if (0,13) -> (0,1,2,3,4,5,6,7,8,9,10,11,12)
        y = random.randint(0,int(GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x,y] #gets a random coordinate
        
        canvas.create_oval(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=FOOD_COLOR, tag="food") #creating an oval food

def next_turn(snake, food):
    
    x, y = snake.coordinates[0] #unpacking the coordinate for the head of the snake
    
    if direction == 'up':
        y -= SPACE_SIZE
    elif direction == 'down':
        y += SPACE_SIZE
    elif direction == 'left':
        x -= SPACE_SIZE
    elif direction == 'right':
        x += SPACE_SIZE
    
    snake.coordinates.insert(0, (x,y)) #updating the coordinate for the head of the , "0" argument specifies the index at which the new coordinates should be inserted, so in this case they will be added as the first item in the list. The (x,y) argument specifies the coordinates of the new square that the snake will move to.
    
    square = canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE, fill=SNAKE_COLOR) #creates a new body part of the snake
    snake.squares.insert(0, square) #add the square object to the beginning of the list of squares. 
    
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        
        score += 1
        
        label.config(text="Score:{}".format(score))
        
        canvas.delete("food")
        
        food = Food()
    
    else:
    
        del snake.coordinates[-1] #deletes the last coordinate
    
        canvas.delete(snake.squares[-1]) #The -1 argument specifies the index of the item to be deleted, so in this case it will delete the last item in the list. 
    
        del snake.squares[-1] #This could be done, for example, when the snake needs to move and remove the last square in its body. 
    
    if check_collision(snake):
        game_over()
        
    else:
    
        window.after(SPEED, next_turn, snake, food) #calls function once after the given time

def change_direction(new_direction):
    
    global direction
    #CHANGING THE DIRECTION OF THE SNAKE
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collision(snake):
    x, y = snake.coordinates[0] #this code is trying to unpack the coordinates of the first element in a list called snake.coordinates. The values of x and y would be the first and second elements of the first tuple in the list, respectively.
    
    if x<0 or x>= GAME_WIDTH:
        return True
    if y<0 or y>= GAME_WIDTH:
        return True
    
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
        
    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font = ('consolas',70), text = "GAME OVER", fill = "red", tag = "game over")


window = Tk()
window.title("Snake Game")
window.resizable(False, False) #if you dont want your window to be resizable

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('consolas',20))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()
#TO CENTER THE CANVAS EACH TIME THE PROGRAM IS RUN
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}") #setting the geometry of the window

window.bind('<Left>',lambda event: change_direction('left')) #lambda function is used as an event handler
window.bind('<Right>',lambda event: change_direction('right'))
window.bind('<Up>',lambda event: change_direction('up'))
window.bind('<Down>',lambda event: change_direction('down'))

snake = Snake() #creating a object for the class
food = Food()

next_turn(snake,food)

window.mainloop()