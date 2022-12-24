from tkinter import *
import time

WIDTH = 800
HEIGHT = 533
xVelocity = 4 #speed to move x-axis and y-axis
yVelocity = 2

window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

background_image = PhotoImage(file = "ground.png")
ground = canvas.create_image(0,0,image = background_image,anchor=NW)

photo_image = PhotoImage(file = "ball.png")
photo_image = photo_image.subsample(15,15)
ball = canvas.create_image(int(WIDTH/2),int(HEIGHT/2),image = photo_image,anchor=NW)



ball_width = photo_image.width()
ball_height = photo_image.height()


while True:
    coordinates = canvas.coords(ball) #gets the coordinates of the canvas
    print(coordinates)
    if(coordinates[0] >= (WIDTH - ball_width) or coordinates[0]<0): #coordinates[0] gets the x coordinate
        xVelocity = -xVelocity #if the above condition satisfies the variable changes
    if(coordinates[1] >= (HEIGHT - ball_height) or coordinates[1]<0): #coordinates[0] gets the x coordinate
        yVelocity = -yVelocity
    canvas.move(ball,xVelocity,yVelocity) #moves the image inside the canvas with the defined distance to x-axis and y-axis
    window.update() #updates the window for each cycle
    time.sleep(0.01)

window.mainloop()

