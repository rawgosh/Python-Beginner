from tkinter import *
import random #used to access random function

def next_turn(row, column): #function for next turn
    
    global player #globalizing the variable to get access of it
    
    if buttons[row][column]['text'] == "" and check_winner() is False: #checking for the empty space and the winner

        if player == players[0]: #checking because random function is used 
        
            buttons[row][column]['text'] = player #setting the variable

            if check_winner() is False:
                player = players[1]
                label.config(text = (players[1]+" turn")) #displaying the turn of the player if the game is not finished
            
            elif check_winner() is True:
                label.config(text = (players[0]+" wins")) #displaying the name of the player that won
            
            elif check_winner() == "Tie":
                label.config(text = "Tie") #displaying if the game ended as a Tie

        else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text = (players[0]+" turn"))
            
            elif check_winner() is True:
                label.config(text = (players[1]+" wins"))
            
            elif check_winner() == "Tie":
                label.config(text = "Tie")

def check_winner():
    
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "": #checking if all elements in a row contains single player choice
            buttons[row][0].config(bg="green") #changes the background color if game is won by a player
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "": #checking if all elements in a column contains single player choice
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "": #checking if all elements in a diagonal contains single player choice
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif empty_spaces() is False: #this function is called if the defined function returns False

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie" #returns Tie if there is no empty space and the game is not won by a player

    else:
        return False


def empty_spaces():
    
    spaces = 9 #declaring the no of space 
    
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1 #reducing each empty space on each move
    
    if spaces == 0:
        return False
    else:
        return True

def new_game(): #to play a new game this function is called
    
    global player
    
    player = random.choice(players) #choosing a random name from the list
    
    label.config(text = player + " turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0") #setting the bg of the new window as light gray after restarting with all empty space


window = Tk()
window.title("Tic-Tac-Toe") 
players = ["x","o"] #players or their symbol
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]] #creating a 2D list

label = Label(text = player + " turn",  font = ("consolas",40))
label.pack(side = "top") #displays the label on the top

reset_button = Button(text = "restart", font = ("consolas",20), command = new_game)
reset_button.pack(side = "top") #displays the button on the top

frame = Frame(window) #keeping frame inside tthe window
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text = "", font = ("consolas",40), height = 2, width = 5, command = lambda row=row, column=column: next_turn(row,column)) #when a button is clicked the next_turn function is called
        buttons[row][column].grid(row = row, column = column) #arranging the button with row and column


window.mainloop()