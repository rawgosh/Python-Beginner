from tkinter import *
from ball_module import *
import time


window = Tk()

WIDTH = 500
HEIGHT =  500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas,0,0,75,3,4,"yellow")
tennis_ball = Ball(canvas,0,0,25,5,3,"green")
foot_ball = Ball(canvas,0,0,100,2,3,"white")
cricket_ball = Ball(canvas,0,0,30,4,5,"red")
basket_ball = Ball(canvas,0,00,100,5,3,"orange")
tt_ball = Ball(canvas,0,0,25,2,1,"cyan")


while True:
    volley_ball.move()
    tennis_ball.move()
    foot_ball.move()
    cricket_ball.move()
    basket_ball.move()
    tt_ball.move()
    window.update()
    time.sleep(0.01)


window.mainloop()